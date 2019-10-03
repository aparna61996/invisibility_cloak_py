import cv2 as cv
import time
import numpy as np

cap = cv.VideoCapture(0)

time.sleep(1)

#define which color you want to mask out using the given plot of HSV. It's green here.
lower_range = np.array([40,30,80])
upper_range = np.array([45,255,255])

for x in range(60):
	ret,background=cap.read()
	if not ret:
		continue

while(cap.isOpened()):
	return_val,image = cap.read()
	if not return_val:
		break
	#if the image is flipped, use image = np.flip(image, axis = 1)
	hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
	mask = cv.inRange(hsv,lower_range,upper_range)
	mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.opes((3,3),np.uint8),iterations = 2)
	mask = cv.dilate(mask, np.ones((3,3),np.uint8),iterations = 1)
	mask1 = mask.bitwise_not(mask)

	result1 = cv.bitwise_and(bvackground, background, mask = mask)
	result2 = cv.bitwise_and(image, image, mask = mask1)
	output = cv.addWeighted(result1, 1, result2, 1, 0)
	
	cv.imshow("Result",output)
	if cv.waitKey(10) == ord('q'):
		break
cap.release()
cv.destroyAllWindows()

