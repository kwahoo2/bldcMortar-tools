# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Adrian Przekwas <adrian.v.przekwas@gmail.com>

import asyncio
from dataclasses import dataclass
from functools import cached_property

from PySide6.QtCore import QObject, Signal

from bleak import BleakClient
from bleak.backends.device import BLEDevice

SERVICE_UUID = "6d84a3d2-9a17-49bc-92f7-3bcc72de2137"
COM_CHAR_UUID = "6d84a3d2-9a17-49bc-92f7-3bcc72de2138"
ENC0_CHAR_UUID = "6d84a3d2-9a17-49bc-92f7-3bcc72de2139"
ENC1_CHAR_UUID = "6d84a3d2-9a17-49bc-92f7-3bcc72de2140"

@dataclass
class QBleakClient(QObject):
    device: BLEDevice

    comChanged = Signal(bytes)
    enc0Changed = Signal(bytes)
    enc1Changed = Signal(bytes)

    def __post_init__(self):
        super().__init__()

    @cached_property
    def client(self) -> BleakClient:
        return BleakClient(self.device, disconnected_callback=self._handle_disconnect)

    async def start(self):
        await self.client.connect()
        await self.client.start_notify(COM_CHAR_UUID, self._handle_read_com)
        await self.client.start_notify(ENC0_CHAR_UUID, self._handle_read_enc0)
        await self.client.start_notify(ENC1_CHAR_UUID, self._handle_read_enc1)


    async def stop(self):
        await self.client.disconnect()

    async def write(self, data):
        await self.client.write_gatt_char(COM_CHAR_UUID, data)
        print("sent:", data)

    # def _handle_disconnect(self) -> None:
    def _handle_disconnect(self, device_client):
        # cancelling all tasks effectively ends the program
        for t in [t for t in asyncio.all_tasks() if not (t.done() or t.cancelled())]:
            # t.cancel() # already cancelled?
            pass
            # give canceled tasks the last chance to run
        print("Device was disconnected, goodbye.")

    def _handle_read_com(self, _: int, data: bytearray) -> None:
        print("received com:", data)
        self.comChanged.emit(data)

    def _handle_read_enc0(self, _: int, data: bytearray) -> None:
        print("received enc0:", data)
        self.enc0Changed.emit(data)

    def _handle_read_enc1(self, _: int, data: bytearray) -> None:
        print("received enc1:", data)
        self.enc1Changed.emit(data)

