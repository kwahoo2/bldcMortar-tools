# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Adrian Przekwas <adrian.v.przekwas@gmail.com>

# This Python file uses the following encoding: utf-8

# Motor Params
mpr_list = ['0.0000', '0.0097', '0.0193', '0.029', '0.0387', '0.0484', '0.058', '0.0677', '0.0774', '0.087', '0.0967', '0.106', '0.116', '0.126', '0.135', '0.145', '0.155', '0.174', '0.193', '0.213', '0.232', '0.251', '0.271', '0.29', '0.309', '0.348', '0.387', '0.426', '0.464', '0.503', '0.542', '0.58', '0.619', '0.696', '0.773', '0.851', '0.928', '1', '1.08', '1.16', '1.23', '1.39', '1.54', '1.7', '1.85', '2.01', '2.16', '2.32', '2.47', '2.78', '3.09', '3.4', '3.71', '4.02', '4.33', '4.64', '4.95', '5.57', '6.18', '6.8', '7.42', '8.04', '8.66', '9.28', '9.9', '11.1', '12.3', '13.6', '14.8', '16', '17.3', '18.5']
mpr_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f', '0x18', '0x19', '0x1a', '0x1b', '0x1c', '0x1d', '0x1e', '0x1f', '0x28', '0x29', '0x2a', '0x2b', '0x2c', '0x2d', '0x2e', '0x2f', '0x38', '0x39', '0x3a', '0x3b', '0x3c', '0x3d', '0x3e', '0x3f', '0x48', '0x49', '0x4a', '0x4b', '0x4c', '0x4d', '0x4e', '0x4f', '0x58', '0x59', '0x5a', '0x5b', '0x5c', '0x5d', '0x5e', '0x5f', '0x68', '0x69', '0x6a', '0x6b', '0x6c', '0x6d', '0x6e', '0x6f', '0x78', '0x79', '0x7a', '0x7b', '0x7c', '0x7d', '0x7e', '0x7f']
bemf_list = ['0', '0.92', '1.83', '2.75', '3.66', '4.58', '5.5', '6.42', '7.33', '8.25', '9.17', '10', '11', '11.9', '12.8', '13.7', '14.6', '16.5', '18.3', '20.1', '22', '23.8', '25.6', '27.5', '29.3', '33', '36.6', '40.3', '44', '47.7', '51.3', '55', '58.7', '66', '73.3', '80.7', '88', '95.4', '102', '110', '117', '132', '146', '161', '176', '190', '205', '220', '234', '264', '293', '322', '352', '381', '411', '440', '469', '528', '587', '645', '704', '763', '822', '880', '939', '1050', '1170', '1290', '1400', '1520', '1640', '1760']
bemf_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f', '0x18', '0x19', '0x1a', '0x1b', '0x1c', '0x1d', '0x1e', '0x1f', '0x28', '0x29', '0x2a', '0x2b', '0x2c', '0x2d', '0x2e', '0x2f', '0x38', '0x39', '0x3a', '0x3b', '0x3c', '0x3d', '0x3e', '0x3f', '0x48', '0x49', '0x4a', '0x4b', '0x4c', '0x4d', '0x4e', '0x4f', '0x58', '0x59', '0x5a', '0x5b', '0x5c', '0x5d', '0x5e', '0x5f', '0x68', '0x69', '0x6a', '0x6b', '0x6c', '0x6d', '0x6e', '0x6f', '0x78', '0x79', '0x7a', '0x7b', '0x7c', '0x7d', '0x7e', '0x7f']
tsetting_list = ['0', '2.5', '5', '7.5', '10', '12.5', '15', '17.5', '20', '22.5', '25', '27.5', '30', '32.5', '35', '37.5', '40', '45', '50', '55', '60', '65', '70', '75', '80', '90', '100', '110', '120', '130', '140', '150', '160', '180', '200', '220', '240', '260', '280', '300', '320', '360', '400', '440', '480', '520', '560', '600', '640', '720', '800', '880', '960', '1040', '1120', '1200', '1280', '1440', '1600', '1760', '1920', '2080', '2240', '2400', '2560', '2880', '3200', '3520', '3840', '4160', '4480', '4800']
tsetting_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0xa', '0xb', '0xc', '0xd', '0xe', '0xf', '0x18', '0x19', '0x1a', '0x1b', '0x1c', '0x1d', '0x1e', '0x1f', '0x28', '0x29', '0x2a', '0x2b', '0x2c', '0x2d', '0x2e', '0x2f', '0x38', '0x39', '0x3a', '0x3b', '0x3c', '0x3d', '0x3e', '0x3f', '0x48', '0x49', '0x4a', '0x4b', '0x4c', '0x4d', '0x4e', '0x4f', '0x58', '0x59', '0x5a', '0x5b', '0x5c', '0x5d', '0x5e', '0x5f', '0x68', '0x69', '0x6a', '0x6b', '0x6c', '0x6d', '0x6e', '0x6f', '0x78', '0x79', '0x7a', '0x7b', '0x7c', '0x7d', '0x7e', '0x7f']

mpr_reg = '0x20'
bemf_reg = '0x21'
tsetting_reg = '0x22'

mpr_mask = 0b01111111
double_freq_mask = 0b10000000
double_freq_bitshift = 7
bemf_mask = 0b01111111
adj_mode_mask = 0b10000000
adj_mode_bitshift = 7
tsetting_mask = 0b01111111
var_adv_mask = 0b10000000
var_adv_bitshift = 7


soCombos = []
soCombos.append(['isdthr', 'ipdadvcagl', 'rvsdrthr']) # SysOpt1
soCombos.append(['openlcurr', 'oplcurrrt', 'brkdonethr'])
soCombos.append(['ctrlcoef', 'staccel2', 'staccel'])
soCombos.append(['op2clsthr', 'aligntime'])
soCombos.append([])
soCombos.append(['swilimitthr', 'hwilimitthr'])
soCombos.append(['clslpaccel', 'deadtime'])
soCombos.append(['ipdcurrthr', 'ipdclk'])
soCombos.append(['fgolsel', 'fgcycle', 'ktlckthr'])

soCheckboxes = []
soCheckboxes.append(['isden', 'rvsdren'])
soCheckboxes.append([])
soCheckboxes.append([])
soCheckboxes.append([])
soCheckboxes.append(['faulten3', 'locken2', 'locken1', 'locken0', 'avsmen', 'avsmmd', 'ipdrismd'])
soCheckboxes.append([])
soCheckboxes.append(['locken5'])
soCheckboxes.append(['locken4', 'vregsel'])
soCheckboxes.append(['spdctrlmd', 'cloopdis'])

sysoptsCombos = [j for sub in soCombos for j in sub] # flatten version of soCombos
sysoptsCheckboxes = [j for sub in soCheckboxes for j in sub]

# sysoptsCombos = ['isdthr', 'ipdadvcagl', 'rvsdrthr','openlcurr', 'oplcurrrt', 'brkdonethr', 'ctrlcoef', 'staccel2', 'staccel', 'op2clsthr', 'aligntime', 'swilimitthr', 'hwilimitthr', 'clslpaccel', 'deadtime', 'ipdcurrthr', 'ipdclk', 'fgolsel', 'fgcycle', 'ktlckthr']
# sysoptsCheckboxes = ['isden', 'rvsdren', 'faulten3', 'locken2', 'locken1', 'locken0', 'avsmen', 'avsmmd', 'ipdrismd', 'locken5', 'locken4', 'vregsel', 'spdctrlmd', 'cloopdis']

sysopt_regs = []
# SysOpt1
sysopt1_reg = '0x23'
sysopt_regs.append(sysopt1_reg)

isdthr_list = ['6 Hz 80 ms', '3 Hz 160 ms', '1.6 Hz 320 ms', '0.8 Hz 640 ms']
isdthr_hex = ['0x00', '0x01', '0x02', '0x03']
isdthr_mask = 0b11000000
isdthr_bitshift = 6

ipdadvcagl_list = ['30 deg', '60 deg', '90 deg', '120 deg']
ipdadvcagl_hex = ['0x00', '0x01', '0x02', '0x03']
ipdadvcagl_mask = 0b00110000
ipdadvcagl_bitshift = 4

isden_mask = 0b00001000
isden_bitshift = 3

rvsdren_mask = 0b00000100
rvsdren_bitshift = 2

rvsdrthr_list = ['6.3 Hz', '13 Hz', '26 Hz', '51 Hz']
rvsdrthr_hex = ['0x00', '0x01', '0x02', '0x03']
rvsdrthr_mask = 0b00000011
rvsdrthr_bitshift = 0

# SysOpt2
sysopt2_reg = '0x24'
sysopt_regs.append(sysopt2_reg)

openlcurr_list = ['0.2 A', '0.4 A', '0.8 A', '1.6 A']
openlcurr_hex = ['0x00', '0x01', '0x02', '0x03']
openlcurr_mask = 0b11000000
openlcurr_bitshift = 6

oplcurrrt_list = ['6 Vcc/s', '3 Vcc/s', '1.5 Vcc/s', '0.7 Vcc/s', '0.34 Vcc/s', '0.16 Vcc/s', '0.07 Vcc/s', '0.023 Vcc/s']
oplcurrrt_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
oplcurrrt_mask = 0b00111000
oplcurrrt_bitshift = 3

brkdonethr_list = ['No brake', '2.7 s', '1.3 s', '0.67 s', '0.33 s', '0.16 s', '0.08 s', '0.04 s']
brkdonethr_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
brkdonethr_mask = 0b00000111
brkdonethr_bitshift = 0

# SysOpt3
sysopt3_reg = '0x25'
sysopt_regs.append(sysopt3_reg)

ctrlcoef_list = ['0.25', '0.5', '0.75', '1']
ctrlcoef_hex = ['0x00', '0x01', '0x02', '0x03']
ctrlcoef_mask = 0b11000000
ctrlcoef_bitshift = 6

staccel2_list = ['57 Hz/s2', '29 Hz/s2', '14 Hz/s2', '6.9 Hz/s2', '3.3 Hz/s2', '1.6 Hz/s2', '0.66 Hz/s2', '0.22 Hz/s2']
staccel2_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
staccel2_mask = 0b00111000
staccel2_bitshift = 3

staccel_list = ['76 Hz/s', '38 Hz/s', '19 Hz/s', '9.2 Hz/s', '4.5 Hz/s', '2.1 Hz/s', '0.9 Hz/s', '0.3 Hz/s']
staccel_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
staccel_mask = 0b00000111
staccel_bitshift = 0

# SysOpt4
sysopt4_reg = '0x26'
sysopt_regs.append(sysopt4_reg)

op2clsthr_list = ['0.8 Hz', '1.6 Hz', '2.4 Hz', '3.2 Hz', '4.0 Hz', '4.8 Hz', '5.6 Hz', '6.4 Hz', '7.2 Hz', '8.0 Hz', '8.8 Hz', '9.6 Hz', '10.4 Hz', '11.2 Hz', '12.0 Hz', '12.8 Hz', '25.6 Hz', '38.4 Hz', '51.2 Hz', '64.0 Hz', '76.8 Hz', '89.6 Hz', '102.4 Hz', '115.2 Hz', '128.0 Hz', '140.8 Hz', '153.6 Hz', '166.4 Hz', '179.2 Hz', '192.0 Hz', '204.8 Hz']
op2clsthr_hex = ['0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f', '0x10', '0x11', '0x12', '0x13', '0x14', '0x15', '0x16', '0x17', '0x18', '0x19', '0x1a', '0x1b', '0x1c', '0x1d', '0x1e', '0x1f']
op2clsthr_mask = 0b11111000
op2clsthr_bitshift = 3

aligntime_list = ['5.3 s', '2.7 s', '1.3 s', '0.67 s', '0.33 s', '0.16 s', '0.08 s', '0.04 s']
aligntime_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
aligntime_mask = 0b00000111
aligntime_bitshift = 0

# SysOpt5
sysopt5_reg = '0x27'
sysopt_regs.append(sysopt5_reg)

faulten3_mask = 0b10000000
faulten3_bitshift = 7

locken2_mask = 0b01000000
locken2_bitshift = 6

locken1_mask = 0b00100000
locken1_bitshift = 5

locken0_mask = 0b00010000
locken0_bitshift = 4

avsmen_mask = 0b00000100
avsmen_bitshift = 2

avsmmd_mask = 0b00000010
avsmmd_bitshift = 1

ipdrismd_mask = 0b00000001
ipdrismd_bitshift = 0

# SysOpt6
sysopt6_reg = '0x28'
sysopt_regs.append(sysopt6_reg)

swilimitthr_list = ['No limit', '0.2 A', '0.4 A', '0.6 A', '0.8 A', '1.0 A', '1.2 A', '1.4 A', '1.6 A', '1.8 A', '2.0 A', '2.2 A', '2.4 A', '2.6 A', '2.8 A', '3.0 A']
swilimitthr_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f']
swilimitthr_mask = 0b11110000
swilimitthr_bitshift = 4

hwilimitthr_list = ['0.4 A', '0.8 A', '1.2 A', '1.6 A', '2 A', '2.4 A', '2.8 A', '3.2 A']
hwilimitthr_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
hwilimitthr_mask = 0b00001110
hwilimitthr_bitshift = 1

# SysOpt7
sysopt7_reg = '0x29'
sysopt_regs.append(sysopt7_reg)

locken5_mask = 0b10000000
locken5_bitshift = 7

clslpaccel_list = ['Inf fast', '48 Vcc/s', '48 Vcc/s', '0.77 Vcc/s', '0.37 Vcc/s', '0.19 Vcc/s', '0.091 Vcc/s', '0.045 Vcc/s']
clslpaccel_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07']
clslpaccel_mask = 0b01110000
clslpaccel_bitshift = 4

deadtime_list = ['40 ns', '80 ns', '120 ns', '160 ns', '200 ns', '240 ns', '280 ns', '320 ns', '360 ns', '400 ns', '440 ns', '480 ns', '520 ns', '560 ns', '600 ns', '640 ns']
deadtime_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f']
deadtime_mask = 0b00001111
deadtime_bitshift = 0

# SysOpt8
sysopt8_reg = '0x2a'
sysopt_regs.append(sysopt8_reg)

ipdcurrthr_list = ['Align and Go', '0.4 A', '0.6 A', '0.8 A', '1.0 A', '1.2 A', '1.4 A', '1.6 A', '1.8 A', '2.0 A', '2.2 A', '2.4 A', '2.6 A', '2.8 A', '3.0 A', '3.2 A']
ipdcurrthr_hex = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f']
ipdcurrthr_mask = 0b11110000
ipdcurrthr_bitshift = 4

locken4_mask = 0b00001000
locken4_bitshift = 3

vregsel_mask = 0b00000100
vregsel_bitshift = 2

ipdclk_list = ['12 Hz', '24 Hz', '47 Hz', '95 Hz']
ipdclk_hex = ['0x00', '0x01', '0x02', '0x03']
ipdclk_mask = 0b00000011
ipdclk_bitshift = 0

# SysOpt9
sysopt9_reg = '0x2b'
sysopt_regs.append(sysopt9_reg)

fgolsel_list = ['FG outputs in both open loop and closed loop', 'FG outputs only in closed loop', 'FG outputs closed loop and the first open loop']
fgolsel_hex = ['0x00', '0x01', '0x02']
fgolsel_mask = 0b11000000
fgolsel_bitshift = 6

fgcycle_list = ['1 pulse output per electrical cycle', '2 pulses output per 3 electrical cycles', '1 pulse output per 2 electrical cycles', '1 pulse output per 3 electrical cycles']
fgcycle_hex = ['0x00', '0x01', '0x02', '0x03']
fgcycle_mask = 0b00110000
fgcycle_bitshift = 4

ktlckthr_list = ['Kt_high = 3/2Kt. Kt_low = 3/4Kt', 'Kt_high = 2Kt. Kt_low = 3/4Kt', 'Kt_high = 3/2Kt. Kt_low = 1/2Kt', 'Kt_high = 2Kt. Kt_low = 1/2Kt']
ktlckthr_hex = ['0x00', '0x01', '0x02', '0x03']
ktlckthr_mask = 0b00001100
ktlckthr_bitshift = 2

spdctrlmd_mask = 0b00000010
spdctrlmd_bitshift = 1

cloopdis_mask = 0b00000001
cloopdis_bitshift = 0

# fault codes
fault_reg = '0x1e'
lock5_bit = 0b00100000
lock4_bit = 0b00010000
fault3_bit = 0b0000100
lock2_bit = 0b00000100
lock1_bit = 0b00000010
lock0_bit = 0b00000001
