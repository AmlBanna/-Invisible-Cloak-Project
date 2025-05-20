import cv2 
import numpy as np 
import matplotlib.pyplot as plt

import cv2
import numpy as np

# Function to remove the cloak from the frame
def invisible_cloak(frame, background):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of color for the cloak (red as an example)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Generate a mask for the cloak
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2

    # Perform morphological operations to remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((5, 5), np.uint8))

    # Invert the mask to get the cloak area
    mask_inv = cv2.bitwise_not(mask)

    # Extract the cloak part from the frame
    cloak = cv2.bitwise_and(frame, frame, mask=mask)

    # Extract the background part from the captured background
    background = cv2.bitwise_and(background, background, mask=mask_inv)

    # Combine the cloak and background
    output = cv2.add(background, cloak)

    return output

# Initialize the camera
cap = cv2.VideoCapture(0)

# Allow the system to sleep for 3 seconds before the webcam starts
import time
time.sleep(3)

# Capture the background
for i in range(30):
    ret, background = cap.read()

while True:
    # Capture the current frame
    ret, frame = cap.read()
    if not ret:
        break

    # Remove the cloak from the frame
    output = invisible_cloak(frame, background)

    # Display the output
    cv2.imshow("Invisible Cloak", output)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
