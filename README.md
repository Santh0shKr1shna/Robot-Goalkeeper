# Robot-Goalkeeper

This project is designed for Arduino Uno micro controller to identify the position of a ball (any object of green colour), then predict the possible path and then instruct the arduino module to move to the position to accurately save the ball from the goal post.

## Working

For identifying the ball, we used real-time incoming IP camera streams processed using Hough transforms. This is done at python script provided. The movement of the goalkeeper is handled by the Arduino IDE. These two independent scripts communicate via serial communication. Before executing, the Python module require the pyserial package to be installed (it will be automatically be installed if you run the below command).

### Execution

Install the required python modules using `$ pip install -r requirements.txt`

Now, execute the **Arduino** file fter assembling the goalkeeper.
`Compile and upload serial.ino via COMx`

**Simultaneously**, copy the port details and execute the python file. 
`$ python3 main.py`

**Do not open the serial monitor in the Arduino IDE.** The python script cannot access the serial ports if done so.

There might be some delay in the working, use better equipments and wired connections for better results.
