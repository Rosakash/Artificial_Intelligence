import cv2
import numpy as np
# Read the current frame from the video capture object

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('jim.mp4',0)

    
    # until the user hits the 'Esc' key
while True:
# Grab the current frame
    ret, frame = cap.read()

    
    # Convert the image to HSV colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of skin color in HSV
    lower = np.array([0, 70, 60])
    upper = np.array([50, 150, 255])
    # Define range of blue color in HSV
    '''lower = np.array([110, 50, 50])
    upper = np.array([130, 255, 255])'''    
    
    # Threshold the HSV image to get only skin color
    mask = cv2.inRange(hsv, lower, upper)
    
    # Bitwise-AND between the mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # Run median blurring
    
    # Display the input and output
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    # Check if the user hit the 'Esc' key
    c = cv2.waitKey(5) & 0xff
    if c == 27:
        break
cap.release()    # Close all the windows
cv2.destroyAllWindows()


