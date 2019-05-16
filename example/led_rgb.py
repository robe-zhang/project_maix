from fpioa_manager import *
from Maix import GPIO
import time ,lcd

#import utime
#utime.sleep(1), utime.sleep_ms(), utime.sleep_us()

lcd.init()

fm.register(board_info.LED_R, fm.fpioa.GPIO0)
fm.register(board_info.LED_G, fm.fpioa.GPIO1)
fm.register(board_info.LED_B, fm.fpioa.GPIO2)

led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
led_g=GPIO(GPIO.GPIO1,GPIO.OUT)
led_b=GPIO(GPIO.GPIO2,GPIO.OUT)

led_r.value(1)
led_g.value(1)
led_b.value(1)

lcd.clear()

while(True):
    lcd.clear()
    lcd.draw_string(100, 100, "red", lcd.RED, lcd.BLACK)
    led_r.value(0)
    led_g.value(1)
    led_b.value(1)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "green", lcd.RED, lcd.BLACK)
    led_r.value(1)
    led_g.value(0)
    led_b.value(1)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "blue", lcd.RED, lcd.BLACK)
    led_r.value(1)
    led_g.value(1)
    led_b.value(0)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "color 1", lcd.RED, lcd.BLACK)
    led_r.value(1)
    led_g.value(0)
    led_b.value(0)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "yellow", lcd.RED, lcd.BLACK)
    led_r.value(0)
    led_g.value(0)
    led_b.value(1)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "color 2", lcd.RED, lcd.BLACK)
    led_r.value(0)
    led_g.value(1)
    led_b.value(0)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "white", lcd.RED, lcd.BLACK)
    led_r.value(0)
    led_g.value(0)
    led_b.value(0)
    time.sleep(1)
    lcd.clear()
    lcd.draw_string(100, 100, "black", lcd.RED, lcd.BLACK)
    led_r.value(1)
    led_g.value(1)
    led_b.value(1)
    time.sleep(1)