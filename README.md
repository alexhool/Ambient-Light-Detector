# Ambient Light Detector
My internship project at **<a href="https://www.osioptoelectronics.com/" target="_blank">OSI Optoelectronics</a>**.

## How to Run:
1. Download the source code either from the zip or by cloning the repository
2. Navigate into the "Ambient Light Detector" folder
3. Upload <a href="https://github.com/alexhool/Ambient-Light-Detector/blob/master/Ambient%20Light%20Detector/light_serial/light_serial.ino" target="_blank">light_serial.ino</a> to an Arduino IDE compatible board
   - Located in the "light_serial" folder
5. Either run the executable <a href="https://github.com/alexhool/Ambient-Light-Detector/blob/master/Ambient%20Light%20Detector/Ambient%20Light%20Detector.exe" target="_blank">Ambient Light Detector.exe</a> or skip to step 5
6. Install required dependencies from "requirements.txt"
   - Prerequisite: <a href="https://www.python.org/downloads/" target="_blank">Python 3.8+</a>
   - Using pip: `pip install -r "requirements.txt"` 
8. Run <a href="https://github.com/alexhool/Ambient-Light-Detector/blob/master/Ambient%20Light%20Detector/light_gui.py" target="_blank">light_gui.py</a>

## Design Files:
- STEP files are included for 3D printing or basic CAD
  - Files were designed specifically for the parts listed 
- For High Quality CAD models use <a href="https://github.com/alexhool/Ambient-Light-Detector/blob/master/Design%20Files/assembly.f3z" target="_blank">assembly.f3z</a>
  - The *.f3z file extension is a Fusion 360 Zip Archive which contains every part file as a *.f3d file

## Parts List:
- Arduino Nano*
- OSD60-0*
- OPA341*
- 12-Pin SMT Breakout PCB*
- 5mm LED
- 100 Ω Resistor†
- 50 kΩ Resistor†
- 15 pF Capacitor†

*\*Similar component types can be used (compatibility with 3D models not ensured)*\
†*Values can be ±25% of those specified*
