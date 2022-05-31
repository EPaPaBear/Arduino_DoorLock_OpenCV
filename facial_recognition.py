#  -----------------------------------------------------------------------------------------------------
# |	IMPORTANT!!!!!!										    	|
# |												    	|
# |	You need to have										| 
# |		-Opencv, imutils, CMake, face_recognition and serial libraries installed            	|
# |										    		    	|
# |	IMPORTANT!!!!!!										    	|
# |													|
#  -----------------------------------------------------------------------------------------------------

import face_recognition
import imutils #imutils includes opencv functions
import pickle
import time
import cv2
import os
import tkinter as tk
from tkinter import filedialog
import serial
import time
	
def upload_image():
	root = tk.Tk()
	root.withdraw()

	#storing image path
	file_types = [('Jpg Files', '*.jpg'), ('Jpeg Files', '*.jpeg')]
	img_path = filedialog.askopenfilename(filetypes=file_types)

	return img_path


def recognize_face():
	'''
	This function implements the facial recognition operation using the OpenCV library
	@authr Unknown - Remains to be credited
	@params Void function
	'''

	#to find path of xml file containing haarCascade file
	cfp = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
	# load the harcaascade in the cascade classifier
	fc = cv2.CascadeClassifier(cfp)
	# load the known faces and embeddings saved in last file
	data = pickle.loads(open('face_enc', "rb").read())

	#Find path to the image you want to detect face and pass it here
	get_image = upload_image()
	image = cv2.imread(get_image)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	#convert image to Greyscale for HaarCascade
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = fc.detectMultiScale(gray,
	scaleFactor=1.1,
	minNeighbors=6,
	minSize=(60, 60),
	flags=cv2.CASCADE_SCALE_IMAGE)

	# the facial embeddings for face in input
	encodings = face_recognition.face_encodings(rgb)
	names = []
	name = "na"

	# loop over the facial embeddings incase
	# we have multiple embeddings for multiple fcaes
	for encoding in encodings:
		#Compare encodings with encodings in data["encodings"]
		#Matches contain array with boolean values True and False
		matches = face_recognition.compare_faces(data["encodings"],encoding)
		
		#set name = unknown if no encoding matches
		name = "Unknown"
		
		# check to see if we have found a match
		if True in matches:
			#Find positions at which we get True and store them
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			count = {}
		
		# loop over the matched indexes and maintain a count for
		# each recognized face face
		for i in matchedIdxs:
			#Check the names at respective indexes we stored in matchedIdxs
			name = data["names"][i]
			
			#increase count for the name we got
			count[name] = count.get(name, 0) + 1
			#set name which has highest count
			name = max(count, key=count.get)
			# will update the list of names
			names.append(name)

			# do loop over the recognized faces
			for ((x, y, w, h), name) in zip(faces, names):
				# rescale the face coordinates
				# draw the predicted face name on the image
				cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
				cv2.putText(image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)
				cv2.imshow("Frame", image)
				cv2.waitKey(0)
				print(name + " returned")
				return name


def main():

	port = serial.Serial(port='COM3', baudrate=9600)
	port.timeout = 1

	while True:
		datum = recognize_face().strip()
		print("Detected face: " + datum)
		port.write(datum.encode())
		time.sleep(0.5)
	
	port.close()
	

if __name__ == '__main__':
        main()
