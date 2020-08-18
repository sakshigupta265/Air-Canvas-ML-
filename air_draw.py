import numpy as np 
import cv2

camera = cv2.VideoCapture(0)
_,old_frame=camera.read()
mask1 = np.zeros_like(old_frame)
counter = 0


frames = []
x1 = []
y1 = []

while camera.isOpened():
    ret, frame = camera.read()

    # flipping the frame
    frame = cv2.flip(frame,+1)

    # converting bgr to hsv
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv_frame,(11,11),0)

    # threshold value for yellow
    lower_val = np.array([0,100,100])
    higher_val = np.array([100,255,255])

    # mask: detecting only yellow color
    mask = cv2.inRange(hsv_frame,lower_val,higher_val)
    mask_blur = cv2.GaussianBlur(mask,(15,15),0)

    # refining image using morphology
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones([3,3], dtype = np.uint8), iterations = 2)
    mask_copy = mask
    # detecting contours 
    image, contours, heirarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # img = cv2.drawContours(frame, contours, -1,(0,255,0),3)

    # drawing image after detecting countours
    for contour in contours:
        if cv2.contourArea(contour) > 1500:
            cnt = contour
            M = cv2.moments(cnt)
            if M['m00']!=0:
                cx = int (M['m10']/M['m00'])
                cy = int (M['m01']/M['m00'])
                if (counter==0) :
                    cx1=cx
                    cy1=cy
                if(counter==0):
                    counter += 1

                # marking the centroid
                cv2.circle(frame, (cx, cy), 5, [0, 0, 0], -1)
                
                # ready to draw
                mask1 = cv2.circle(mask1,(cx,cy),5,(50,120,255),10)

                cx1=cx
                cy1=cy

                img=cv2.add(frame,mask1)

            cv2.imshow("orignal frame",img)
        cv2.imshow("drawing canvas",mask1)

    k=cv2.waitKey(1)
    if k==ord('q'):
        break

camera.release()
cv2.destroyAllWindows