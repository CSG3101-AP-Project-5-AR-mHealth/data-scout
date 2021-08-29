# Data Scout Repo
Collect vital data using wearable sensors to determine the users situation

## Pi setup

Hardware Requirements:

```
Raspberry Pi 4 4GB Starter Kit
Stainless Steel Housing Waterproof DS18B20 Temperature Probe
4k7 0.25W 5% Carbon Film Resistor
Arduino Compatible Breadboard with 400 Tie Points
```
Temperature probe wiring for correct operations:
![correct wiring for temperature probe](images/tempProbe.png)

Wiring for the Raspberry Pi:
![simple wiring diagram with all the components](images/example.png)

Pin mapping for pi 4:
![correct wiring for temperature probe](images/pi4map.png)

Installed Software on Pi Requirements:

```
twister os (most likely and linux os)
OneWire - Enabled
```
1. Open Edit config file `sudo nano /boot/config.txt`
2. Copy paste `dtoverlay=w1-gpio` save & exit by pressing ctrl x and then y
3. Restart `sudo reboot`
4. Run the following to enable probe
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls
```
5. Change Directory to probes device folder `cd 28*`
6. Test by running `cat w1_slave`


## Ant+ Setup on Pi

Hardware Requirements:

```
Dynastream Innovations ANTUSB-m
Heart rate monitor strap with Ant+
```

Software Requirements:

```
Python3
```

This repo uses an open source repository: [OpenAnt](https://github.com/Tigge/openant)
1. Clone OpenAnt repo
```
git clone https://github.com/Tigge/openant.git
```
2. Follow the instructions for setup in read me

## Setup for converting raw csv files

Place converted fit csv files into the `data-formatter/data/` directory

## Run Converter

Change directory into data-formatter and run 

```python
python convertRawFiles.py
```