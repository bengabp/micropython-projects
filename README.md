Building awesome microcontroller projects with micropython

## Installing the library
```bash
pip install adafruit-ampy
```

## Running code
```bash
ampy --port <YOUR-ESP32-COM-PORT> run blink_led.py
```

## Uploading code to esp32 board to run on board boot
So the esp32 runs a script boot.py once it boots but you can rename 
your script as main.py and upload to the board, it will run the script after booting.

### Uploading script to board using ampy
```bash
ampy --port <YOUR-ESP32-COM-PORT> put main.py
```
After uploading, reboot the esp by unplugging power and plugging back