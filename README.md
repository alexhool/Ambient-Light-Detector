# Ambient Light Detector
My internship project at OSI Optoelectronics.

## How to Run:
1. Download and extract source code from assets below
2. Upload [serial_voltage.ino](https://github.com/alexhool/OSI-Projects/tree/master/Ambient%20Light%20Detector/serial_voltage/serial_voltage.ino) to an Arduino IDE compatible board
3. Install required dependencies from "requirements.txt"
   - Using pip: `pip3 install -r "requirements.txt"` 
4. Run [voltage_gui.py](https://github.com/alexhool/OSI-Projects/tree/master/Ambient%20Light%20Detector/voltage_gui.py)

## Design Files:
- STL files are included for 3D printing
  - Files were designed specifically for the parts listed 
- For 3D models use [Assembly.f3z](https://github.com/alexhool/Ambient-Light-Detector/tree/master/Design%20Files/Assembly.f3z)
  - The *.f3z file extension is a Fusion 360 Zip Archive which contains every part file as a *.f3d file

## Parts List:
- Arduino Nano*
- OSD60-0*
- LMP7721*
- 12-Pin SMT Breakout PCB
- 50 kΩ Resistor†
- 15 pF Capacitor†
- 5mm LED
- 100 Ω Resistor†

*\*Similar component types can be used (compatibility with 3D models not ensured)*\
†*Values can be ±25% of those specified*
