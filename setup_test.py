# the webcam +pyttsx3 test you created earlier.
import cv2

cap=cv2.VideoCapture(0) #open webcam

while True:
    ret, frame= cap.read()
    if not ret:
        break

    frame=cv2.resize(frame,(640,480))  #resize frame to 640x480 for consistency

    #DIP Part:
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert to grayscale
    blur= cv2.GaussianBlur(gray,(5,5),0) #apply Gaussian blur
    _, thresh=cv2.threshold(blur,100,255,cv2.THRESH_BINARY) #apply binary thresholding

    cv2.imshow('Original Frame', frame) #show original frame
    cv2.imshow('Grayscale', gray) #show grayscale frame 
    cv2.imshow('Blurred', blur) #show blurred frame
    cv2.imshow('Thresholded', thresh) #show thresholded frame

    if cv2.waitKey(1) & 0xFF == ord('q'): #exit on 'q' key press
        break

cap.release() #release webcam
cv2.destroyAllWindows() #close all OpenCV windows