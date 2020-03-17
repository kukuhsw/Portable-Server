#!/usr/bin/python

import socket
import fcntl
import struct
from i2clibraries import i2c_lcd_smbus

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd = i2c_lcd_smbus.i2c_lcd(0x27,1, 2, 1, 0, 4, 5, 6, 7, 3)

lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn()

lcd.writeString( "e0 " )
lcd.writeString( get_ip_address('eth0' ) )
lcd.setPosition( 2, 0 )
lcd.writeString( "e1 " )
lcd.writeString( get_ip_address('eth1' ) )