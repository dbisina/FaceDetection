"""
1. Get a shitload of faces
2. make em black and white
3. Train the algorithm to detect faces
"""

import cv2

#Loading a pre-trained data on facefrontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_Frontalface_alt.xml')

"""
#choosing an image to detect faces in
img = cv2.imread('celebrities-support-johnny-depp.jpg')

#converting to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates) = [[45, 63, 172, 172]]  

#drawing a recangle on the face
#this can be used for a single faced photo

#(x, y, w, h) = face_coordinates[0]  #face_coordinates holds an array inside an array so we pick the position [0] since it signifies the array


#this would loop through multiple photos
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#this is hard coding it manually
#cv2.rectangle(img, (45, 63), (45 + 172, 63 + 172), (0, 255, 0), 2), the (0, 255, 0) is (B, G, R) for the color nof the rectangle, the 2 is the thickness





#displays the image
cv2.imshow('Face detector', img)
#when image pops up this terminates it if any key is pressed, it waits till a key is pressed
cv2.waitKey()

"""

#to capture video for webcam
webcam = cv2.VideoCapture(0)
#webcam = cv2.VideoCapture(something.mp4)

#iterate forever over frames
while True:

    #read the current frame
    frame_read, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Face detector', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

#release the videocapture object
webcam.release()

print('             ~lyon98.dbios')
