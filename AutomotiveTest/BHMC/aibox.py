# -*- coding: utf-8 -*-
import time
from ctypes import *


class AIBOX():
    aibox = windll.LoadLibrary('.\data\PCI-Dask64.dll')
    print(aibox)

    aibox.Register_Card(31, 0)
    aibox.DIO_PortConfig(0, 10, 2)

    def connect(self):
        print("Connecting AIBOX")
        self.aibox.Register_Card(31, 0)
        self.aibox.DIO_PortConfig(0, 10, 2)

    def disconnect(self):
        self.aibox.Release_Card(0)

    def bat_off(self):
        self.aibox.DO_WriteLine(0, 10, 0, 0)

    def bat_on(self):
        self.aibox.DO_WriteLine(0, 10, 0, 1)

    def acc_off(self):
        self.aibox.DO_WriteLine(0, 10, 1, 0)

    def acc_on(self):
        print("ACC ON")
        self.aibox.DO_WriteLine(0, 10, 1, 1)

    def ill1_off(self):
        self.aibox.DO_WriteLine(0, 10, 2, 0)

    def ill1_on(self):
        self.aibox.DO_WriteLine(0, 10, 2, 1)

    def ill2_off(self):
        self.aibox.DO_WriteLine(0, 10, 3, 0)

    def ill2_on(self):
        self.aibox.DO_WriteLine(0, 10, 3, 1)

    def ign_off(self):
        self.aibox.DO_WriteLine(0, 10, 4, 0)

    def ign_off(self):
        self.aibox.DO_WriteLine(0, 10, 4, 1)

aibox = AIBOX()