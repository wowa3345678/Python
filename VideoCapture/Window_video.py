import cv2

clicked = False
def onMouse(event, x, y, flags, param):
	global clicked
	if event == cv2.EVENT_LBUTTONDOWN:
		clicked == True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)



success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
	cv2.imshow('myWindow', frame)
	success, frame = cameraCapture.read()
   
cv2.destroyWindow('myWindow')
cameraCapture.release()