# -*- coding: utf-8 -*-
import time
from ctypes import *
import platform


oks = windll.LoadLibrary('.\data\PCI-Dask64.dll')
print(oks)

#oks.Register_Card(31, 0)
#oks.DIO_PortConfig(0, 10, 2)

def connect():
    oks.Register_Card(31, 0)
    oks.DIO_PortConfig(0, 10, 2)

def disconnect():
    oks.Release_Card(0)

def bat_off():
    oks.DO_WriteLine(0, 10, 0, 0)

def bat_on():
    oks.DO_WriteLine(0, 10, 0, 1)

def acc_off():
    oks.DO_WriteLine(0, 10, 1, 0)

def acc_on():
    oks.DO_WriteLine(0, 10, 1, 1)

def ill1_off():
    oks.DO_WriteLine(0, 10, 2, 0)

def ill1_on():
    oks.DO_WriteLine(0, 10, 2, 1)

def ill2_off():
    oks.DO_WriteLine(0, 10, 3, 0)

def ill2_on():
    oks.DO_WriteLine(0, 10, 3, 1)

def ign_off():
    oks.DO_WriteLine(0, 10, 4, 0)

def ign_off():
    oks.DO_WriteLine(0, 10, 4, 1)


connect()
time.sleep(1)
#bat_off()
#time.sleep(5)
bat_on()
time.sleep(1)
#disconnect()

