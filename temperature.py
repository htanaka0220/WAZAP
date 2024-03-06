# -*- coding: utf-8 -*-

# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
#ネット使う用
import urllib , json,requests
# I2Cデバイスからの読み取りに必要なライブラリを呼び出す
import os
import struct
import RPi.GPIO as GPIO

LED_NUM = 18

#LEDの初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_NUM,GPIO.OUT)

# I2Cのインスタンスを作成
wiringpi.wiringPiSetup()
i2c = wiringpi.I2C()
x
# I2Cの設定
# 通信する機器のI2Cアドレスを指定
temperature_dev = i2c.setup(0x48)

# 温度を16ビットのデータ取得
# その他めレジスタ0x03に設定
i2c.writeReg8(temperature_dev, 0x03, 0x80)

while True:
    
    #LEDピカピカ
    if(temperature > 30):
        GPIO.output(LED_NUM,True)
    else:
        GPIO.output(LED_NUM,False)
        

    # 1秒ごと
    time.sleep(5)
    
    #URL
    url = "https://maker.ifttt.com/trigger/test_0_py/with/key/"
    
    # IFTTT Key
    IFTTT_KEY = 'bno7Y7pjzfkj3rh5PEtT3i5yo_fvLa2r1ZK5s0xebQE'

    # Log
    requests.post(url + IFTTT_KEY, json = {'value1':temperature})
