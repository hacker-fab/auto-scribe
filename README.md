# auto-scribe
Code for controlling the automatic scriber that is in development.

The following files are for running the desktop GUI that will eventually interface with the scribe machine:
- main.py
- GUI_runner.py
- GUI_functions.py

  You will need to have Python 3 installed to run these. You will also need the tkinter Python library installed. You can install this library using the command line through pip or conda. Run the main file `main.py` on the command line to run the GUI.

  There is also a folder called stepper_test whic contains arduino code for testing the steppers. The file within that folder called steppeer_test.ino controlls the stepper motors using an input integer sent through the serial port to know how many steps to take. To run, you must install the Arduino IDE and run it through there. You will need an Arduino to connect to via USB.

  The end goal is for the GUI to become an `.exe` file that can be run on any Windows device that can communicate with the Arduino through the serial port.
