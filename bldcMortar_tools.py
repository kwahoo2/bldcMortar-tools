# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Adrian Przekwas <adrian.v.przekwas@gmail.com>

# This Python file uses the following encoding: utf-8
import os, csv
from pathlib import Path
import struct
from functools import cached_property

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, QTimer

import qasync
import asyncio
from bleak import BleakScanner
import qBleak_client
import drv10983_const as drv_const

from form import Ui_Widget

class Widget(QWidget):
    @qasync.asyncSlot()
    async def send_speed_command(self, id):
        if id == 0:
            if self.dir_0_is_fwd is True:
                dir_byte = b'F'
            else:
                dir_byte = b'B'

            bytearr = b'SP' + dir_byte + b'\x00' + struct.pack("<l", self.speed_mot_0)
            # await self.handle_send(bytearr)
            self.append_command(bytearr)
            self.m_ui.logEdit.insertPlainText("Send command: (" + bytearr[0:3].decode("utf-8")+") " + bytearr.hex(' ') + "\n")

        if id == 1:
            if self.dir_1_is_fwd is True:
                dir_byte = b'F'
            else:
                dir_byte = b'B'

            bytearr = b'SP' + dir_byte + b'\x01' + struct.pack("<l", self.speed_mot_1)
            # await self.handle_send(bytearr)
            self.append_command(bytearr)
            self.m_ui.logEdit.insertPlainText("Send command: (" + bytearr[0:3].decode("utf-8")+") "+ bytearr.hex(' ') + "\n")

    @qasync.asyncSlot()
    async def send_write_reg(self, bytearr):
        self.append_command(bytearr)
        self.m_ui.logEdit.insertPlainText("Send command: (" + bytearr[0:3].decode("utf-8")+") " + bytearr.hex(' ') + "\n")

    @qasync.asyncSlot()
    async def send_write_reg_now(self, bytearr):
        await self.handle_send(bytearr)
        self.m_ui.logEdit.insertPlainText("Send command: (" + bytearr[0:3].decode("utf-8")+") " + bytearr.hex(' ') + "\n")

    @qasync.asyncSlot()
    async def send_command(self):
        bytearr = self.command_buffer[self.buffer_tail]
        if self.buffer_tail != self.buffer_head:
            if bytearr == b'\x00\x00\x00\x00\x00\x00\x00\x00':
                await self.handle_send(bytearr)
                self.command_buffer[self.buffer_tail] = b'\x00\x00\x00\x00\x00\x00\x00\x00' # reset value to give info that the bytes were already sent
            self.buffer_tail += 1
            if self.buffer_tail >= self.buffer_size:
                self.buffer_tail = 0
        else:
            if bytearr != b'\x00\x00\x00\x00\x00\x00\x00\x00':
                await self.handle_send(bytearr)
                self.command_buffer[self.buffer_tail] = b'\x00\x00\x00\x00\x00\x00\x00\x00'

    @Slot()
    def append_command(self, bytearr):
        oldbytearr = self.command_buffer[self.buffer_head]
        if oldbytearr[:4] != bytearr[:4]: # do not push forward buffer hear if command type and drive id are unchanged, overwrite old buffer
            self.buffer_head +=1
        if self.buffer_head >= self.buffer_size:
            self.buffer_head = 0
        self.command_buffer[self.buffer_head] = bytearr

    @Slot()
    def dir_0_set_fwd(self):
        self.dir_0_is_fwd = True
        self.send_speed_command(0)

    @Slot()
    def dir_0_set_bwd(self):
        self.dir_0_is_fwd = False
        self.send_speed_command(0)

    @Slot()
    def dir_1_set_fwd(self):
        self.dir_1_is_fwd = True
        self.send_speed_command(1)

    @Slot()
    def dir_1_set_bwd(self):
        self.dir_1_is_fwd = False
        self.send_speed_command(1)

    @Slot()
    # def speed_0_changed(self, val):
    def speed_0_changed(self):
        val = self.m_ui.speedSlider0.value()
        self.speed_mot_0 = int(val)
        # self.speed_mot_0 = int(val)  # 9 bits, 0-511
        self.m_ui.speedValLabel0.setText(str(val))
        self.send_speed_command(0)

    @Slot()
    # def speed_1_changed(self, val):
    def speed_1_changed(self):
        val = self.m_ui.speedSlider1.value()
        self.speed_mot_1 = int(val)
        # self.speed_mot_1 = int(val)  # 9 bits, 0-511
        self.m_ui.speedValLabel1.setText(str(val))
        self.send_speed_command(1)

    @Slot()
    def mpr_0_select(self, idx):
        self.mpr_select(idx, 0)

    @Slot()
    def mpr_1_select(self, idx):
        self.mpr_select(idx, 1)

    def mpr_select(self, idx, motor_id):
        mpr_val = int(drv_const.mpr_hex[idx], 16)
        reg_val = (mpr_val & drv_const.mpr_mask) | (self.read_reg_from_tab(motor_id, drv_const.mpr_reg) & drv_const.double_freq_mask)
        print(drv_const.mpr_reg, f"{mpr_val:02x}", f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(drv_const.mpr_reg[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, drv_const.mpr_reg, f"0x{reg_val:02x}")

    @Slot()
    def double_freq_0_select(self, state):
        self.double_freq_select(self.is_checked(state), 0)

    @Slot()
    def double_freq_1_select(self, state):
        self.double_freq_select(self.is_checked(state), 1)

    def double_freq_select(self, checked, motor_id):
        reg_val = (checked << drv_const.double_freq_bitshift) | (self.read_reg_from_tab(motor_id, drv_const.mpr_reg) & drv_const.mpr_mask)
        print(drv_const.mpr_reg, str(checked), f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(drv_const.mpr_reg[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, drv_const.mpr_reg, f"0x{reg_val:02x}")

    @Slot()
    def bemf_0_select(self, idx):
        bemf_val = drv_const.bemf_hex[idx]
        print(drv_const.bemf_reg, bemf_val)
        bytearr = b'WRG' + b'\x00\x00\x00' + bytes.fromhex(drv_const.bemf_reg[2:]) + bytes.fromhex(bemf_val[2:])
        self.send_write_reg(bytearr)

    @Slot()
    def bemf_1_select(self, idx):
        bemf_val = drv_const.bemf_hex[idx]
        print(drv_const.bemf_reg, bemf_val)
        bytearr = b'WRG' + b'\x01\x00\x00' + bytes.fromhex(drv_const.bemf_reg[2:]) + bytes.fromhex(bemf_val[2:])
        self.send_write_reg(bytearr)

    def bemf_select(self, idx, motor_id):
        bemf_val = int(drv_const.bemf_hex[idx], 16)
        reg_val = (bemf_val & drv_const.bemf_mask) | (self.read_reg_from_tab(motor_id, drv_const.bemf_reg) & drv_const.adj_mode_mask)
        print(drv_const.bemf_reg, f"{bemf_val:02x}", f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(drv_const.bemf_reg[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, drv_const.bemf_reg, f"0x{reg_val:02x}")

    @Slot()
    def adj_mode_0_select(self, state):
        self.adj_mode_select(self.is_checked(state), 0)

    @Slot()
    def adj_mode_1_select(self, state):
        self.adj_mode_select(self.is_checked(state), 1)

    def adj_mode_select(self, checked, motor_id):
        reg_val = (checked << drv_const.adj_mode_bitshift) | (self.read_reg_from_tab(motor_id, drv_const.bemf_reg) & drv_const.bemf_mask)
        print(drv_const.bemf_reg, str(checked), f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(drv_const.bemf_reg[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, drv_const.bemf_reg, f"0x{reg_val:02x}")

    @Slot()
    def tsetting_0_select(self, idx):
        self.tsetting_select(idx, 0)

    @Slot()
    def tsetting_1_select(self, idx):
        self.tsetting_select(idx, 1)

    def tsetting_select(self, idx, motor_id):
        tsetting_val = int(drv_const.tsetting_hex[idx], 16)
        reg_val = (tsetting_val & drv_const.tsetting_mask) | (self.read_reg_from_tab(motor_id, drv_const.tsetting_reg) & drv_const.var_adv_mask)
        print(drv_const.tsetting_reg, f"{tsetting_val:02x}", f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(drv_const.tsetting_reg[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, drv_const.tsetting_reg, f"0x{reg_val:02x}")

    @Slot()
    def var_adv_0_select(self, state):
        self.var_adv_select(self.is_checked(state), 0)

    @Slot()
    def var_adv_1_select(self, state):
        self.var_adv_select(self.is_checked(state), 1)

    def var_adv_select(self, checked, motor_id):
        reg_val = (checked << drv_const.var_adv_bitshift) | (self.read_reg_from_tab(motor_id, drv_const.tsetting_reg) & drv_const.tsetting_mask)
        print(drv_const.tsetting_reg, str(checked), f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(drv_const.tsetting_reg[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, drv_const.tsetting_reg, f"0x{reg_val:02x}")

    def sysopt_combobox_select(self, idx, reg_addr, val, mask, bitshift):
        if self.is_checked(self.m_ui.motor1RadioButton.isChecked()):
            motor_id = 1
        else:
            motor_id = 0
        reg_val = ((val << bitshift) & mask) | (self.read_reg_from_tab(motor_id, reg_addr) & ~mask)
        print(reg_addr, f"{val:02x}", f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(reg_addr[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, reg_addr, f"0x{reg_val:02x}")

    def sysopt_checkbox_select(self, reg_addr, state, mask, bitshift):
        if self.is_checked(self.m_ui.motor1RadioButton.isChecked()):
            motor_id = 1
        else:
            motor_id = 0
        reg_val = ((self.is_checked(state) << bitshift) & mask) | (self.read_reg_from_tab(motor_id, reg_addr) & ~mask)
        print(reg_addr, str(self.is_checked(state)), f"{reg_val:02x}")
        bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(reg_addr[2:]) + bytes.fromhex(f"{reg_val:02x}")
        self.send_write_reg(bytearr)
        self.fill_tab_reg(motor_id, reg_addr, f"0x{reg_val:02x}")

    def is_checked(self, state): #checkbox may have 3 states, 1 - partially checked, 2 - checked
        checked = 0
        if state > 0:
            checked = 1
        return checked

# SysOpts

    @Slot()
    def motor_0_select(self, radiobutton):
        if radiobutton.isChecked() is True:
            self.motor_select(0)

    @Slot()
    def motor_1_select(self, radiobutton):
        if radiobutton.isChecked() is True:
            self.motor_select(1)

    def motor_select(self,motor_id):
        bytearr = b'RDR' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00\x00\x00'
        self.send_write_reg_now(bytearr)

# SysOpt1

    def isdthr_select(self, idx):
        reg_addr = drv_const.sysopt1_reg
        val = int(drv_const.isdthr_hex[idx], 16)
        mask = drv_const.isdthr_mask
        bitshift = drv_const.isdthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def ipdadvcagl_select(self, idx):
        reg_addr = drv_const.sysopt1_reg
        val = int(drv_const.ipdadvcagl_hex[idx], 16)
        mask = drv_const.ipdadvcagl_mask
        bitshift = drv_const.ipdadvcagl_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def isden_select(self, state):
        reg_addr = drv_const.sysopt1_reg
        mask = drv_const.isden_mask
        bitshift = drv_const.isden_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def rvsdren_select(self, state):
        reg_addr = drv_const.sysopt1_reg
        mask = drv_const.rvsdren_mask
        bitshift = drv_const.rvsdren_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def rvsdrthr_select(self, idx):
        reg_addr = drv_const.sysopt1_reg
        val = int(drv_const.rvsdrthr_hex[idx], 16)
        mask = drv_const.rvsdrthr_mask
        bitshift = drv_const.rvsdrthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt2

    def openlcurr_select(self, idx):
        reg_addr = drv_const.sysopt2_reg
        val = int(drv_const.openlcurr_hex[idx], 16)
        mask = drv_const.openlcurr_mask
        bitshift = drv_const.openlcurr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def oplcurrrt_select(self, idx):
        reg_addr = drv_const.sysopt2_reg
        val = int(drv_const.oplcurrrt_hex[idx], 16)
        mask = drv_const.oplcurrrt_mask
        bitshift = drv_const.oplcurrrt_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def brkdonethr_select(self, idx):
        reg_addr = drv_const.sysopt2_reg
        val = int(drv_const.brkdonethr_hex[idx], 16)
        mask = drv_const.brkdonethr_mask
        bitshift = drv_const.brkdonethr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt3

    def ctrlcoef_select(self, idx):
        reg_addr = drv_const.sysopt3_reg
        val = int(drv_const.ctrlcoef_hex[idx], 16)
        mask = drv_const.ctrlcoef_mask
        bitshift = drv_const.ctrlcoef_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def staccel2_select(self, idx):
        reg_addr = drv_const.sysopt3_reg
        val = int(drv_const.staccel2_hex[idx], 16)
        mask = drv_const.staccel2_mask
        bitshift = drv_const.staccel2_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def staccel_select(self, idx):
        reg_addr = drv_const.sysopt3_reg
        val = int(drv_const.staccel_hex[idx], 16)
        mask = drv_const.staccel_mask
        bitshift = drv_const.staccel_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt4

    def op2clsthr_select(self, idx):
        reg_addr = drv_const.sysopt4_reg
        val = int(drv_const.op2clsthr_hex[idx], 16)
        mask = drv_const.op2clsthr_mask
        bitshift = drv_const.op2clsthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def aligntime_select(self, idx):
        reg_addr = drv_const.sysopt4_reg
        val = int(drv_const.aligntime_hex[idx], 16)
        mask = drv_const.aligntime_mask
        bitshift = drv_const.aligntime_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt5

    def faulten3_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.faulten3_mask
        bitshift = drv_const.faulten3_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def locken2_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.locken2_mask
        bitshift = drv_const.locken2_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def locken1_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.locken1_mask
        bitshift = drv_const.locken1_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def locken0_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.locken0_mask
        bitshift = drv_const.locken0_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def avsmen_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.avsmen_mask
        bitshift = drv_const.avsmen_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def avsmmd_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.avsmmd_mask
        bitshift = drv_const.avsmmd_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def ipdrismd_select(self, state):
        reg_addr = drv_const.sysopt5_reg
        mask = drv_const.ipdrismd_mask
        bitshift = drv_const.ipdrismd_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    # SysOpt6
    def swilimitthr_select(self, idx):
        reg_addr = drv_const.sysopt6_reg
        val = int(drv_const.swilimitthr_hex[idx], 16)
        mask = drv_const.swilimitthr_mask
        bitshift = drv_const.swilimitthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def hwilimitthr_select(self, idx):
        reg_addr = drv_const.sysopt6_reg
        val = int(drv_const.hwilimitthr_hex[idx], 16)
        mask = drv_const.hwilimitthr_mask
        bitshift = drv_const.hwilimitthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt7

    def locken5_select(self, state):
        reg_addr = drv_const.sysopt7_reg
        mask = drv_const.locken5_mask
        bitshift = drv_const.locken5_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def clslpaccel_select(self, idx):
        reg_addr = drv_const.sysopt7_reg
        val = int(drv_const.clslpaccel_hex[idx], 16)
        mask = drv_const.clslpaccel_mask
        bitshift = drv_const.clslpaccel_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def deadtime_select(self, idx):
        reg_addr = drv_const.sysopt7_reg
        val = int(drv_const.deadtime_hex[idx], 16)
        mask = drv_const.deadtime_mask
        bitshift = drv_const.deadtime_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt8

    def ipdcurrthr_select(self, idx):
        reg_addr = drv_const.sysopt8_reg
        val = int(drv_const.ipdcurrthr_hex[idx], 16)
        mask = drv_const.ipdcurrthr_mask
        bitshift = drv_const.ipdcurrthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def locken4_select(self, state):
        reg_addr = drv_const.sysopt8_reg
        mask = drv_const.locken4_mask
        bitshift = drv_const.locken4_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def vregsel_select(self, state):
        reg_addr = drv_const.sysopt8_reg
        mask = drv_const.vregsel_mask
        bitshift = drv_const.vregsel_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def ipdclk_select(self, idx):
        reg_addr = drv_const.sysopt8_reg
        val = int(drv_const.ipdclk_hex[idx], 16)
        mask = drv_const.ipdclk_mask
        bitshift = drv_const.ipdclk_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    # SysOpt9

    def fgolsel_select(self, idx):
        reg_addr = drv_const.sysopt9_reg
        val = int(drv_const.fgolsel_hex[idx], 16)
        mask = drv_const.fgolsel_mask
        bitshift = drv_const.fgolsel_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def fgcycle_select(self, idx):
        reg_addr = drv_const.sysopt9_reg
        val = int(drv_const.fgcycle_hex[idx], 16)
        mask = drv_const.fgcycle_mask
        bitshift = drv_const.fgcycle_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def ktlckthr_select(self, idx):
        reg_addr = drv_const.sysopt9_reg
        val = int(drv_const.ktlckthr_hex[idx], 16)
        mask = drv_const.ktlckthr_mask
        bitshift = drv_const.ktlckthr_bitshift
        self.sysopt_combobox_select(idx, reg_addr, val, mask, bitshift)

    def spdctrlmd_select(self, state):
        reg_addr = drv_const.sysopt9_reg
        mask = drv_const.spdctrlmd_mask
        bitshift = drv_const.spdctrlmd_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

    def cloopdis_select(self, state):
        reg_addr = drv_const.sysopt9_reg
        mask = drv_const.cloopdis_mask
        bitshift = drv_const.cloopdis_bitshift
        self.sysopt_checkbox_select(reg_addr, state, mask, bitshift)

# End of SysOpt part
    @Slot()
    def read_0_register(self):
        reg_addr = self.m_ui.readRegEdit0.text()
        bytearr = b'RRG' + b'\x00\x00\x00\x00' + bytes.fromhex(reg_addr[2:])
        self.send_write_reg(bytearr)

    @Slot()
    def write_0_register(self):
        reg_addr = self.m_ui.writeRegEdit0.text()
        reg_val = self.m_ui.valRegEdit0.text()
        bytearr = b'WRG' + b'\x00\x00\x00' + bytes.fromhex(reg_addr[2:]) + bytes.fromhex(reg_val[2:])
        self.send_write_reg(bytearr)

    @Slot()
    def read_1_register(self):
        reg_addr = self.m_ui.readRegEdit1.text()
        bytearr = b'RRG' + b'\x01\x00\x00\x00' + bytes.fromhex(reg_addr[2:])
        self.send_write_reg(bytearr)

    @Slot()
    def write_1_register(self):
        reg_addr = self.m_ui.writeRegEdit1.text()
        reg_val = self.m_ui.valRegEdit1.text()
        bytearr = b'WRG' + b'\x01\x00\x00' + bytes.fromhex(reg_addr[2:]) + bytes.fromhex(reg_val[2:])
        self.send_write_reg(bytearr)

    @Slot()
    def read_copy_0_flash(self):
        bytearr = b'RCF' + b'\x00\x00\x00\x00\x00'
        self.send_write_reg(bytearr)

    @Slot()
    def write_0_flash(self):
        bytearr = b'WFL' + b'\x00\x00\x00\x00\x00'
        self.send_write_reg(bytearr)

    @Slot()
    def read_copy_1_flash(self):
        bytearr = b'RCF' + b'\x01\x00\x00\x00\x00'
        self.send_write_reg(bytearr)

    @Slot()
    def write_1_flash(self):
        bytearr = b'WFL' + b'\x01\x00\x00\x00\x00'
        self.send_write_reg(bytearr)

    @Slot()
    def verb_val_select(self, val):
        bytearr = b'SDV' + b'\x00\x00\x00\x00' + val.to_bytes(1, 'little')
        self.send_write_reg(bytearr)

    @Slot()
    def fg_div_select(self, val):
        self.fg_divider = val
        print ("FG divider: " +str(val))

    @Slot()
    def enc_div_select(self, val):
        self.enc_divider = val
        print ("Encoder divider: " +str(val))

    @Slot()
    def reset_0_fault(self):
        bytearr = b'RLF' + b'\x00\x00\x00\x00\x00'
        self.send_write_reg(bytearr)

    @Slot()
    def reset_1_fault(self):
        bytearr = b'RLF' + b'\x01\x00\x00\x00\x00'
        self.send_write_reg(bytearr)

    @Slot()
    def save_all_regs(self):
        path, ok = QFileDialog.getSaveFileName(
            self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if ok:
            columns = range(self.m_ui.regValsTable.columnCount())
            header = [self.m_ui.regValsTable.horizontalHeaderItem(column).text() for column in columns]
            with open(path, 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel', lineterminator='\n')
                writer.writerow(header)
                for row in range(self.m_ui.regValsTable.rowCount()):
                    row_data = []
                    for column in columns:
                        item = self.m_ui.regValsTable.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append("")
                    writer.writerow(row_data)

    @Slot()
    def load_all_regs(self):
        print("readin")
        path, ok = QFileDialog.getOpenFileName(
            self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if ok:
            with open(path) as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                if header == self.headers:
                    self.m_ui.regValsTable.clearContents()
                    self.m_ui.regValsTable.setRowCount(0)
                    # self.regValsTable.setColumnCount(len(header))
                    # self.regValsTable.setHorizontalHeaderLabels(header)
                    for row, values in enumerate(reader):
                        self.m_ui.regValsTable.insertRow(row)
                        for column, value in enumerate(values):
                            self.m_ui.regValsTable.setItem(row, column, QTableWidgetItem(value))
                else:
                    self.csvErrMsgBox.show()

    @Slot()
    def send_0_all_regs(self):
        self.send_all_regs(0)

    @Slot()
    def send_1_all_regs(self):
        self.send_all_regs(1)

    @Slot()
    def send_all_regs(self, motor_id):
        for row in range(self.m_ui.regValsTable.rowCount()):  # row id is equal to registry adress
            reg_addr = "0x{:02x}".format(row)
            reg_val = self.read_reg_from_tab(motor_id, reg_addr)
            bytearr = b'WRG' + bytes.fromhex(f"{motor_id:02x}") + b'\x00\x00' + bytes.fromhex(reg_addr[2:]) + bytes.fromhex(f"{reg_val:02x}")
            self.send_write_reg(bytearr)
            self.handle_com_changed(bytearr)  # to fill combo and checkboxes

    @Slot()
    def reload_0_regs(self):
        bytearr = b'LOA' + b'\x00\x00\x00\x00\x00'
        self.send_write_reg_now(bytearr)

    @Slot()
    def reload_1_regs(self):
        bytearr = b'LOA' + b'\x01\x00\x00\x00\x00'
        self.send_write_reg_now(bytearr)

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.m_ui = Ui_Widget()
        self.m_ui.setupUi(self)
        self._client = None

        # the circular buffer is used as workaround to
        # [org.bluez.Error.InProgress] Operation already in progress
        # error when commands are send too fast
        self.buffer_size = 1000
        self.command_buffer = [b'\x00\x00\x00\x00\x00\x00\x00\x00'] * self.buffer_size
        self.buffer_head = 0
        self.buffer_tail = 0
        self.command_interval = 200 # ms

        self.commandTimer = QTimer(self)
        self.commandTimer.timeout.connect(self.send_command)

        self.headers = ["Adress", "Drv Reg 0", "Flash 0", "Drv Reg 1", "Flash 1"]
        self.m_ui.csvErrMsgBox = QMessageBox()
        self.m_ui.csvErrMsgBox.setText('Wrong file loaded, table not changed')
        self.m_ui.regValsTable.setHorizontalHeaderLabels(self.headers)

        self.m_ui.mprComboBox0.clear()
        self.m_ui.mprComboBox0.addItems(drv_const.mpr_list)
        self.m_ui.mprComboBox0.currentIndexChanged.connect(self.mpr_0_select)
        self.m_ui.dfreqCheckBox0.stateChanged.connect(self.double_freq_0_select)
        self.m_ui.bemfComboBox0.clear()
        self.m_ui.bemfComboBox0.addItems(drv_const.bemf_list)
        self.m_ui.bemfComboBox0.currentIndexChanged.connect(self.bemf_0_select)
        self.m_ui.hcAdjCheckBox0.stateChanged.connect(self.adj_mode_0_select)
        self.m_ui.tsettingComboBox0.clear()
        self.m_ui.tsettingComboBox0.addItems(drv_const.tsetting_list)
        self.m_ui.tsettingComboBox0.currentIndexChanged.connect(self.tsetting_0_select)
        self.m_ui.varAdvCheckBox0.stateChanged.connect(self.var_adv_0_select)

        self.m_ui.mprComboBox1.clear()
        self.m_ui.mprComboBox1.addItems(drv_const.mpr_list)
        self.m_ui.mprComboBox1.currentIndexChanged.connect(self.mpr_1_select)
        self.m_ui.dfreqCheckBox1.stateChanged.connect(self.double_freq_1_select)
        self.m_ui.bemfComboBox1.clear()
        self.m_ui.bemfComboBox1.addItems(drv_const.bemf_list)
        self.m_ui.bemfComboBox1.currentIndexChanged.connect(self.bemf_1_select)
        self.m_ui.hcAdjCheckBox1.stateChanged.connect(self.adj_mode_1_select)
        self.m_ui.tsettingComboBox1.clear()
        self.m_ui.tsettingComboBox1.addItems(drv_const.tsetting_list)
        self.m_ui.tsettingComboBox1.currentIndexChanged.connect(self.tsetting_1_select)
        self.m_ui.varAdvCheckBox1.stateChanged.connect(self.var_adv_1_select)

        # SysOpts
        self.m_ui.motor0RadioButton.toggled.connect(lambda: self.motor_0_select(self.m_ui.motor0RadioButton))
        self.m_ui.motor1RadioButton.toggled.connect(lambda: self.motor_1_select(self.m_ui.motor1RadioButton))

        for i, soCombo in enumerate(drv_const.sysoptsCombos):
            exec("self.m_ui."+drv_const.sysoptsCombos[i]+"ComboBox.clear()")
            exec("self.m_ui."+drv_const.sysoptsCombos[i]+"ComboBox.addItems(drv_const."+drv_const.sysoptsCombos[i]+"_list)")
            exec("self.m_ui."+drv_const.sysoptsCombos[i]+"ComboBox.currentIndexChanged.connect(self."+drv_const.sysoptsCombos[i]+"_select)")

        for i, soCheckbox in enumerate(drv_const.sysoptsCheckboxes):
            exec("self.m_ui."+drv_const.sysoptsCheckboxes[i]+"CheckBox.stateChanged.connect(self."+drv_const.sysoptsCheckboxes[i]+"_select)")

        self.m_ui.scanButton.clicked.connect(self.handle_scan)
        self.m_ui.connectButton.clicked.connect(self.handle_connect)
        self.m_ui.fwdButton0.clicked.connect(lambda: self.dir_0_set_fwd())
        self.m_ui.bwdButton0.clicked.connect(lambda: self.dir_0_set_bwd())
        self.m_ui.readRegButton0.clicked.connect(lambda: self.read_0_register())
        self.m_ui.writeRegButton0.clicked.connect(lambda: self.write_0_register())
        self.m_ui.speedSlider0.valueChanged.connect(self.speed_0_changed)
        # self.speedSlider0.sliderReleased.connect(self.speed_0_changed) # to avoid flooding bluetooth
        self.m_ui.readCopyFlashButton0.clicked.connect(lambda: self.read_copy_0_flash())
        self.m_ui.writeFlashButton0.clicked.connect(lambda: self.write_0_flash())
        self.speed_mot_0 = 0
        self.dir_0_is_fwd = True
        self.m_ui.resetFaultButton0.clicked.connect(lambda: self.reset_0_fault())
        self.m_ui.sendRegsButton0.clicked.connect(lambda: self.send_0_all_regs())
        self.m_ui.reloadRegsButton0.clicked.connect(lambda: self.reload_0_regs())

        self.m_ui.fwdButton1.clicked.connect(lambda: self.dir_1_set_fwd())
        self.m_ui.bwdButton1.clicked.connect(lambda: self.dir_1_set_bwd())
        self.m_ui.readRegButton1.clicked.connect(lambda: self.read_1_register())
        self.m_ui.writeRegButton1.clicked.connect(lambda: self.write_1_register())
        self.m_ui.speedSlider1.valueChanged.connect(self.speed_1_changed)
        self.m_ui.readCopyFlashButton1.clicked.connect(lambda: self.read_copy_1_flash())
        self.m_ui.writeFlashButton1.clicked.connect(lambda: self.write_1_flash())
        self.m_ui.verbSpinBox.valueChanged.connect(self.verb_val_select)
        self.m_ui.fgSpinBox.valueChanged.connect(self.fg_div_select)
        self.m_ui.encSpinBox.valueChanged.connect(self.enc_div_select)
        self.speed_mot_1 = 0
        self.dir_1_is_fwd = True
        self.m_ui.resetFaultButton1.clicked.connect(lambda: self.reset_1_fault())
        self.m_ui.sendRegsButton1.clicked.connect(lambda: self.send_1_all_regs())
        self.m_ui.reloadRegsButton1.clicked.connect(lambda: self.reload_1_regs())

        self.enc_divider = 600.0
        self.fg_divider = 11.0  # 11 pole pairs
        self.first_fg0 = ""
        self.second_fg0 = ""
        self.first_fg1 = ""
        self.second_fg1 = ""

        self.latitude = [b'\x00\x00\x00\x00\x00\x00'] * 2 # 2 * (max)6 bytes
        self.longitude = [b'\x00\x00\x00\x00\x00\x00'] * 2

        self.m_ui.saveAllRegsButton.clicked.connect(lambda: self.save_all_regs())
        self.m_ui.loadAllRegsButton.clicked.connect(lambda: self.load_all_regs())

    @property
    def current_client(self):
        return self._client

    @cached_property
    def devices(self):
        return list()

    async def build_client(self, device):
        if self._client is not None:
            await self._client.stop()
        self._client = qBleak_client.QBleakClient(device)
        self._client.enc0Changed.connect(self.handle_enc0_changed)
        self._client.enc1Changed.connect(self.handle_enc1_changed)
        self._client.comChanged.connect(self.handle_com_changed)
        await self._client.start()

    @qasync.asyncSlot()
    async def handle_connect(self):
        self.m_ui.logEdit.insertPlainText("try connect\n")
        device = self.m_ui.devicesComboBox.currentData()
        if isinstance(device, qBleak_client.BLEDevice):
            self.m_ui.connectButton.setEnabled(False)
            await self.build_client(device)
            self.m_ui.logEdit.insertPlainText("connected\n")
            bytearr = b'RAR' + b'\x00\x00\x00\x00\x00'
            self.send_write_reg_now(bytearr)  # ask for all registers read
            self.m_ui.connectButton.setEnabled(True)
            self.m_ui.connectButton.clicked.disconnect(self.handle_connect)
            self.m_ui.connectButton.clicked.connect(self.handle_disconnect)
            self.m_ui.connectButton.setText("Disconnect")
            self.commandTimer.start(self.command_interval)

    @qasync.asyncSlot()
    async def handle_disconnect(self):
        if self._client is not None:
            await self._client.stop()
        self.m_ui.connectButton.clicked.disconnect(self.handle_disconnect)
        self.m_ui.connectButton.clicked.connect(self.handle_connect)
        self.m_ui.connectButton.setText("Connect")

    @qasync.asyncSlot()
    async def handle_scan(self):
        self.m_ui.logEdit.insertPlainText("Started scanner\n")
        # print("Started scanner")
        self.devices.clear()
        devices = await BleakScanner.discover()
        self.devices.extend(devices)
        self.m_ui.devicesComboBox.clear()
        for i, device in enumerate(self.devices):
            self.m_ui.devicesComboBox.insertItem(i, device.name, device)
            self.m_ui.logEdit.insertPlainText(str(i) + ", " + str(device.name) + ", " + str(device) + "\n")
            print(i, device.name, device)
        self.m_ui.logEdit.insertPlainText("Finish scanner\n")

    @qasync.asyncSlot()
    async def handle_send(self, message):
        if self.current_client is None:
            return
        if message:
            await self.current_client.write(message)

    def handle_enc0_changed(self, message):
        enc0_int = struct.unpack("<q", message)[0]
        enc0_float = float(enc0_int) / self.enc_divider
        self.m_ui.enc0StepsLabel.setText(str(enc0_int))
        self.m_ui.enc0RevsLabel.setText(str("%.2f" % enc0_float) + " rev")

    def handle_enc1_changed(self, message):
        enc1_int = struct.unpack("<q", message)[0]
        enc1_float = float(enc1_int) / self.enc_divider
        self.m_ui.enc1StepsLabel.setText(str(enc1_int))
        self.m_ui.enc1RevsLabel.setText(str("%.2f" % enc1_float) + " rev")

    def handle_com_changed(self, message):
        bytearr = struct.unpack("<3sBBBBB", message) # BLDC driver info
        motor_id = bytearr[1]
        if bytearr[0] == b"VRG":  # registry value reading
            addr = hex(bytearr[4])
            value = hex(bytearr[5])
            self.decode_received_registry(motor_id, addr, value)
        if bytearr[0] == b"VRF":  # registry flash reading
            addr = hex(bytearr[4])
            value = hex(bytearr[5])
            print("Registry flash " + addr + " is " + value)
            self.fill_tab_fls(motor_id, addr, value)
        if bytearr[0] == b"MSP":  # motor speed reading
            bytearr = struct.unpack("<3sBBBH", message)
            if bytearr[1] == 0:
                self.m_ui.gotSpeedLabel0.setText(str(bytearr[4]/10) + " Hz")
            if bytearr[1] == 1:
                self.m_ui.gotSpeedLabel1.setText(str(bytearr[4]/10) + " Hz")
        if bytearr[0] == b"FGR":  # FG Pin counter reading, first part of value
            bytearr = struct.unpack("<3sBBBBB", message)
            if bytearr[1] == 0:
                self.first_fg0 = message[4:]
            if bytearr[1] == 1:
                self.first_fg1 = message[4:]
        if bytearr[0] == b"FGr":  # FG Pin counter reading, second part of value
            bytearr = struct.unpack("<3sBBBBB", message)
            if bytearr[1] == 0:
                self.second_fg0 = message[4:]
                fg0_str = self.second_fg0 + self.first_fg0
                fg0 = struct.unpack("<q", fg0_str)[0]
                fg0_float = float(fg0) / self.fg_divider
                self.m_ui.fg0RevsLabel.setText(str("%.2f" % fg0_float) + " rev")
            if bytearr[1] == 1:
                self.second_fg1 = message[4:]
                fg1_str = self.second_fg1 + self.first_fg1
                fg1 = struct.unpack("<q", fg1_str)[0]
                fg1_float = float(fg1) / self.fg_divider
                self.m_ui.fg1RevsLabel.setText(str("%.2f" % fg1_float) + " rev")

        bytearr = struct.unpack("<cB6s", message) #GPS info
        if bytearr[0] == b"G":
            info_type = bytearr[1]
            s = bytearr[2].decode("utf-8")
            if info_type == 0:
                self.m_ui.fixLabel.setText(s)
            if info_type == 1:
                self.m_ui.dateLabel.setText(s[0:2] + "-" + s[2:4] + "-20" + s[4:6])
            if info_type == 2:
                self.m_ui.timeLabel.setText(s[0:2] + "h " + s[2:4] + "m " + s[4:6] + "s")
            if info_type == 3: # 3 and 4: 2 parts of latitude
                self.latitude[0] = bytearr[2]
            if info_type == 4:
                self.latitude[1] = bytearr[2]
                s = self.latitude[0].decode("utf-8") + "." + self.latitude[1].decode("utf-8")
                self.m_ui.latiLabel.setText(s)
            if info_type == 5:
                self.longitude[0] = bytearr[2]
            if info_type == 6:
                self.longitude[1] = bytearr[2]
                s = self.longitude[0].decode("utf-8") + "." + self.longitude[1].decode("utf-8")
                self.m_ui.longiLabel.setText(s)

    def decode_received_registry(self, motor_id, addr, value):
        print("Registry " + addr + " is " +value)
        self.fill_tab_reg(motor_id, addr, value)
        if motor_id == 0:
            self.m_ui.gotRegLabel0.setText(value)
            self.m_ui.readRegEdit0.setText(addr)
        if motor_id == 1:
            self.m_ui.gotRegLabel1.setText(value)
            self.m_ui.readRegEdit0.setText(addr)
        if (addr == drv_const.mpr_reg):
            mpr_val = int(value, 16) & drv_const.mpr_mask
            checked = (int(value, 16) & drv_const.double_freq_mask) >> drv_const.double_freq_bitshift
            indices = [i for i, s in enumerate(drv_const.mpr_hex) if f"0x{mpr_val:02x}" in s]
            if (indices):
                if motor_id == 0:
                    self.m_ui.mprComboBox0.currentIndexChanged.disconnect(self.mpr_0_select)
                    self.m_ui.mprComboBox0.setCurrentIndex(indices[0])
                    self.m_ui.mprComboBox0.currentIndexChanged.connect(self.mpr_0_select)
                    self.m_ui.dfreqCheckBox0.stateChanged.disconnect(self.double_freq_0_select)
                    self.m_ui.dfreqCheckBox0.setChecked(checked)
                    self.m_ui.dfreqCheckBox0.stateChanged.connect(self.double_freq_0_select)
                if motor_id == 1:
                    self.m_ui.mprComboBox1.currentIndexChanged.disconnect(self.mpr_1_select)
                    self.m_ui.mprComboBox1.setCurrentIndex(indices[0])
                    self.m_ui.mprComboBox1.currentIndexChanged.connect(self.mpr_1_select)
                    self.m_ui.dfreqCheckBox1.stateChanged.disconnect(self.double_freq_1_select)
                    self.m_ui.dfreqCheckBox1.setChecked(checked)
                    self.m_ui.dfreqCheckBox1.stateChanged.connect(self.double_freq_1_select)
        if (addr == drv_const.bemf_reg):
            bemf_val = int(value, 16) & drv_const.mpr_mask
            checked = (int(value, 16) & drv_const.adj_mode_mask) >> drv_const.adj_mode_bitshift
            indices = [i for i, s in enumerate(drv_const.bemf_hex) if f"0x{bemf_val:02x}" in s]
            if (indices):
                if motor_id == 0:
                    self.m_ui.bemfComboBox0.currentIndexChanged.disconnect(self.bemf_0_select)
                    self.m_ui.bemfComboBox0.setCurrentIndex(indices[0])
                    self.m_ui.bemfComboBox0.currentIndexChanged.connect(self.bemf_0_select)
                    self.m_ui.hcAdjCheckBox0.stateChanged.disconnect(self.adj_mode_0_select)
                    self.m_ui.hcAdjCheckBox0.setChecked(checked)
                    self.m_ui.hcAdjCheckBox0.stateChanged.connect(self.adj_mode_0_select)
                if motor_id == 1:
                    self.m_ui.bemfComboBox1.currentIndexChanged.disconnect(self.bemf_1_select)
                    self.m_ui.bemfComboBox1.setCurrentIndex(indices[0])
                    self.m_ui.bemfComboBox1.currentIndexChanged.connect(self.bemf_1_select)
                    self.m_ui.hcAdjCheckBox1.stateChanged.disconnect(self.adj_mode_1_select)
                    self.m_ui.hcAdjCheckBox1.setChecked(checked)
                    self.m_ui.hcAdjCheckBox1.stateChanged.connect(self.adj_mode_1_select)
        if (addr == drv_const.tsetting_reg):
            tsetting_val = int(value, 16) & drv_const.mpr_mask
            checked = (int(value, 16) & drv_const.var_adv_mask) >> drv_const.var_adv_bitshift
            indices = [i for i, s in enumerate(drv_const.tsetting_hex) if f"0x{tsetting_val:02x}" in s]
            if (indices):
                if motor_id == 0:
                    self.m_ui.tsettingComboBox0.currentIndexChanged.disconnect(self.tsetting_0_select)
                    self.m_ui.tsettingComboBox0.setCurrentIndex(indices[0])
                    self.m_ui.tsettingComboBox0.currentIndexChanged.connect(self.tsetting_0_select)
                    self.m_ui.varAdvCheckBox0.stateChanged.disconnect(self.var_adv_0_select)
                    self.m_ui.varAdvCheckBox0.setChecked(checked)
                    self.m_ui.varAdvCheckBox0.stateChanged.connect(self.var_adv_0_select)
                if motor_id == 1:
                    self.m_ui.tsettingComboBox1.currentIndexChanged.disconnect(self.tsetting_1_select)
                    self.m_ui.tsettingComboBox1.setCurrentIndex(indices[0])
                    self.m_ui.tsettingComboBox1.currentIndexChanged.connect(self.tsetting_1_select)
                    self.m_ui.varAdvCheckBox1.stateChanged.disconnect(self.var_adv_1_select)
                    self.m_ui.varAdvCheckBox1.setChecked(checked)
                    self.m_ui.varAdvCheckBox1.stateChanged.connect(self.var_adv_1_select)
        # SysOpts

        for j, reg in enumerate(drv_const.sysopt_regs):
            if (addr == reg):
                if motor_id == 0:
                    self.m_ui.motor0RadioButton.blockSignals(True)
                    self.m_ui.motor0RadioButton.setChecked(True)
                    self.m_ui.motor0RadioButton.blockSignals(False)
                if motor_id == 1:
                    self.m_ui.motor1RadioButton.blockSignals(True)
                    self.m_ui.motor1RadioButton.setChecked(True)
                    self.m_ui.motor1RadioButton.blockSignals(False)
                combos = drv_const.soCombos[j]  # 2D, not flatten one
                checkboxes = drv_const.soCheckboxes[j]
                for checkbox_name in checkboxes:
                    mask = eval("drv_const." + checkbox_name + "_mask")
                    bitshift = eval("drv_const." + checkbox_name + "_bitshift")
                    checkbox_obj = eval("self.m_ui." + checkbox_name + "CheckBox")
                    checkbox_slot = eval("self." + checkbox_name + "_select")
                    checkbox_checked = (int(value, 16) & mask) >> bitshift
                    checkbox_obj.stateChanged.disconnect(checkbox_slot)
                    checkbox_obj.setChecked(checkbox_checked)
                    checkbox_obj.stateChanged.connect(checkbox_slot)
                for combo_name in combos:
                    mask = eval("drv_const." + combo_name + "_mask")
                    bitshift = eval("drv_const." + combo_name + "_bitshift")
                    combo_slot = eval("self." + combo_name + "_select")
                    combo_obj = eval("self.m_ui." + combo_name + "ComboBox")
                    combo_hex = eval("drv_const." + combo_name + "_hex")
                    combo_val = (int(value, 16) & mask) >> bitshift
                    combo_indices = [i for i, s in enumerate(combo_hex) if f"0x{combo_val:02x}" in s]
                    combo_obj.currentIndexChanged.disconnect(combo_slot)
                    combo_obj.setCurrentIndex(combo_indices[0])
                    combo_obj.currentIndexChanged.connect(combo_slot)
                break
        # Fault codes
        if (addr == drv_const.fault_reg):
            lock5_checked = self.is_checked((int(value, 16) & drv_const.lock5_bit))
            lock4_checked = self.is_checked((int(value, 16) & drv_const.lock4_bit))
            fault3_checked = self.is_checked((int(value, 16) & drv_const.fault3_bit))
            lock2_checked = self.is_checked((int(value, 16) & drv_const.lock2_bit))
            lock1_checked = self.is_checked((int(value, 16) & drv_const.lock1_bit))
            lock0_checked = self.is_checked((int(value, 16) & drv_const.lock0_bit))
            if motor_id == 0:
                self.m_ui.lock5Ind0CheckBox.setChecked(lock5_checked)
                self.m_ui.lock4Ind0CheckBox.setChecked(lock4_checked)
                self.m_ui.fault3Ind0CheckBox.setChecked(fault3_checked)
                self.m_ui.lock2Ind0CheckBox.setChecked(lock2_checked)
                self.m_ui.lock1Ind0CheckBox.setChecked(lock1_checked)
                self.m_ui.lock0Ind0CheckBox.setChecked(lock0_checked)
            if motor_id == 1:
                self.m_ui.lock5Ind1CheckBox.setChecked(lock5_checked)
                self.m_ui.lock4Ind1CheckBox.setChecked(lock4_checked)
                self.m_ui.fault3Ind1CheckBox.setChecked(fault3_checked)
                self.m_ui.lock2Ind1CheckBox.setChecked(lock2_checked)
                self.m_ui.lock1Ind1CheckBox.setChecked(lock1_checked)
                self.m_ui.lock0Ind1CheckBox.setChecked(lock0_checked)

    def fill_tab_reg(self, motor_id, addr, val):  # drv registers table
        if motor_id == 0:
            self.m_ui.regValsTable.setItem(int(addr, 16), 0, QTableWidgetItem(str(addr)))
            self.m_ui.regValsTable.setItem(int(addr, 16), 1, QTableWidgetItem(str(val)))
        if motor_id == 1:
            self.m_ui.regValsTable.setItem(int(addr, 16), 0, QTableWidgetItem(str(addr)))
            self.m_ui.regValsTable.setItem(int(addr, 16), 3, QTableWidgetItem(str(val)))

    def fill_tab_fls(self, motor_id, addr, val):  # flash registers table
        if motor_id == 0:
            self.m_ui.regValsTable.setItem(int(addr, 16), 0, QTableWidgetItem(str(addr)))
            self.m_ui.regValsTable.setItem(int(addr, 16), 2, QTableWidgetItem(str(val)))
        if motor_id == 1:
            self.m_ui.regValsTable.setItem(int(addr, 16), 0, QTableWidgetItem(str(addr)))
            self.m_ui.regValsTable.setItem(int(addr, 16), 4, QTableWidgetItem(str(val)))

    def read_reg_from_tab(self, motor_id, addr):
        item_int = 0
        if motor_id == 0:
            item = self.m_ui.regValsTable.item(int(addr, 16), 1)
        if motor_id == 1:
            item = self.m_ui.regValsTable.item(int(addr, 16), 3)
        if item is not None:
            item_int = int(item.text(), 16)
        return item_int


if __name__ == "__main__":
    app = QApplication([])
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)
    widget = Widget()
    widget.show()
    try:
        loop.run_forever()
    finally:
        loop.close()
    # sys.exit(app.exec()) # not needed with qasync
