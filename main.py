import cv2

image=cv2.imread('amir.jpg',0)
inverted=255-image
blered=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blured=255-blered
sketch=image/inverted_blured
sketch=sketch*255
cv2.imwrite('paint.jpg',sketch)