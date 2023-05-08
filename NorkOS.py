# Import modules to use it in future / Импортируем модули, чтобы использовать их в будуещем

import time
import colorama
import os
from playsound import playsound

def BIOS_SETTINGS():
    time.sleep(2)
    print('NorkBIOS v1.00 Build 4')
    print("\nSystem time: 22/08/2023 12:28 Sat.")
    print("CPU: IT 815P 0.8Hz")
    print("GPU: IT 20350 64MB")
    print("RAM: IT DDR1 8MB")
    print("HDD: IT 51200 512MB")

class SYSTEM():
    print('NorkBIOS 1.0')
    print("\n=============================================")
    BIOS_SETTINGS()
    BIOSExity = input('\nTo exit BIOS, enter "0": ')
    if BIOSExity == "0":
        print("\nLoading RAM...")
        time.sleep(1)
        print("RAM: 8MB")

        print("\nLoading HDD...")
        time.sleep(2)
        print("ROM: 512MB")

        print("\nNorkOS Loading...")
        time.sleep(3)

        print("=================================================================")
        print('\nNorkOS 1.0 Load Successfully. Enter "help" for NorkOS help.')

        while True:
            ENTER = input("0/> ")
            if ENTER == "help":
                print("\n===================================================")
                print('Enter "info" to show information about yor computer; \nEnter "norkpad" to open NotePad app;')
                print('Enter "filem" to show files in disk 0/>;\nEnter "player" to open MediaPlayer;')
                print('Enter "time" to show system time;\nEnter "livezone" to show where you live.')
            if ENTER == "norkpad":
                print("\nNorkPad 1.0")
                print("===========================================")
                NAME = input("How do you wanna name this file?: ")
                FILE = input()
                print("\nSaving...")
                time.sleep(1)
                print("\nChanges saved. To open this file, open filem, then enter the file name.")
                ENTER = True
            if ENTER == "filem":
                print("\nNorkOS File Manager 1.0")
                print("=================================")
                print("File name: OS.exe")
                print("File name: KEYB.dll")
                print("File name: SCREENR.ini")
                print("File name: SYS.ini")
                OTFILE = input("\nIf you need to open other file, enter it's name here: ")
                if OTFILE == NAME:
                    OPENFILE = input("\nFile name: " + NAME + ". To open this file, enter 1: ")
                    if OPENFILE == "1":
                        print("\n" + FILE)
                        ENTER = True
            if ENTER == "player":
                print("\nNorkOS MediaPlayer 1.0")
                print("====================================")
                print("\nSorry, this app couldn't be run :(\n")
                ENTER = True
            if ENTER == "time":
                print()
                print("\n" + time.time)
                print()
            if ENTER == "livezone":
                LIVEZ = input("\nYou live in Russia. To change, enter your country: ")
                print("\nYou live in " + LIVEZ)
                ENTER = True
            if ENTER == "video":
                VIDEO = int(input("\nChoose video: 1 - виндовс кыля229: "))
                if VIDEO == "1":
                    print("\nSorry, an error has been founed(")
                    ENTER = True