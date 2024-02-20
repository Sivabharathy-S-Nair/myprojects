import cv2
img=cv2.imread('lena.jpg',1)
cv2.line(img,(0,0),(550,550),(230, 255, 255),5)
cv2.line(img,(510,0),(0,510),(230, 255, 255),5)
cv2.circle(img,(50,50),50,(0, 102, 102),-1)
cv2.circle(img,(461,461),50,(0, 102, 102),-1)
cv2.circle(img,(461,50),50,(0, 102, 102),-1)
cv2.circle(img,(50,461),50,(0, 102, 102),-1)
cv2.rectangle(img,(350,300),(180,200),(26, 0, 0),5)
font=cv2.FONT_HERSHEY_PLAIN
cv2.putText(img,"Hai",(210,275),font,5,((0, 0, 0)))
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
