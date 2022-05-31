# Arduino_DoorLock_OpenCV

This project attempts to simulate a door lock system in Proteus using facial recognition. The facial recognition component is handled in Python and uses serial communication
to establish a connection with the Arduinon module in proteus using the **COMPIM** component.

## Requirements

You need to have the following installed before you should attempt to run anything in this repo. Else, you'll have a lot of errors.
* Python 2 or 3
* Virtual Serial Port Driver
* Proteus 8 Application Framework
* Arduino IDE
* A reliable general purpose IDE, like sublime text

Similarly, you need the following dependencies, assuming you've installed [npm](https://nodejs.org/en/download/) and [pip](https://pip.pypa.io/en/stable/installation/)
* OpenCV : `pip install opencv-contrib-python`
* imutils : `pip install imutils` 
* CMake : `pip install cmake`
* dlib : `pip install dlib`
* face_recognition: `pip install face-recognition`
* PySerial : `pip install pyserial`

Once those dependencies are installed, you're good to go!

## How to use
### Step One
The folder _`Images`_ constains a set of images(ordered in folders by corresponding name), insert your own set of dummy images to train the model with. (For example [LFW - People (Face Recognition)](https://www.kaggle.com/datasets/atulanandjha/lfwpeople?resource=download)).
### Step Two
Subsequently run the _`facial_detect_recognize.py`_ module to scan through all the images in the _`Images`_ folder and train the model with.
### Step Three
Once you've trained your model, a _`face_enc`_ file should be created.
### Step Four
Launch the Proteus Simulation Application and open the _`door_face_detect`_ Proteus Project file
### Step Five
Simultaneously launch the Arduino IDE and run the _`door_lock_face_detect.ino`_ file and export the compiled binary (hex) file
### Step Six
Return to the Proteus window and click on the Arduino UNO component and upload the path of the exported hex file
### Step Seven
Ensure the Virstual Serial Port Driver is launched as well and create a pair between `COM1` and `COM3` virtual ports
### Step Eight
Run the Proteus simulation
### Step Nine
Now, run the _`facial_detection.py`_ module
### Step Ten
Select an image you'd like to predict from the dialog boxz
If the face is recognized, the name of the person will be displayed on the LCD, and the motor will turn(door open)z
Otherwise, the LCD will let you know that the input face has not been recognized and the door will not open\
