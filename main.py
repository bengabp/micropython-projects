import random

import network
import time
import machine


class BoardManager:
    def __init__(self):
        self.home_wifi_ssid = 'natmini'
        self.home_widi_pass = 'I9pReli93nYIerjnO5'
        self.wifi = network.WLAN(network.STA_IF)


    def connect_wifi(self):
        self.wifi.active(True)
        if not self.wifi.isconnected():
            print(f"Connecting to WIFI network -> {self.home_wifi_ssid}... ")
            self.wifi.connect(self.home_wifi_ssid, self.home_widi_pass)

            # Wait until connected
            while not self.wifi.isconnected():
                time.sleep(1)
            print(f"Connected to WIFI network -> {self.home_wifi_ssid}")


    def create_hotspot(self, ssid='esp32 board', password='password12345'):
        ap = network.WLAN(network.AP_IF)
        ap.active(True)

        try:
            ap.config(essid=ssid,
                      password=password,
                      authmode=network.AUTH_WPA2_PSK)

            while not ap.active():
                pass

            print('Access Point Created')
            print(f'SSID: {ssid}')
            print(f'Password: {password}')
            print(f'IP Address: {ap.ifconfig()[0]}')

        except OSError as e:
            print(f"Error: {e}")
            print("Make sure password is at least 8 characters long")


    def blink_onboard_led(self):
        pins = [
            machine.Pin(i, machine.Pin.OUT)
            for i in [2,32]
        ]
        wait_time = random.randint(20, 980)/1000
        while True:
            [pin.on() for pin in pins]
            time.sleep(wait_time)
            [pin.off() for pin in pins]
            time.sleep(wait_time)

    def start(self):
        self.connect_wifi()
        self.blink_onboard_led()


if __name__ == '__main__':
    board = BoardManager()
    board.start()

