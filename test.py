import matplotlib.pyplot as plt
import numpy as np
import cv2

sample_image = cv2.imread('Im001_1.jpg')
#print("test")
img = cv2.cvtColor(sample_image,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(500,500))

cv2.imshow("original",img)
cv2.waitKey(0)


plt.axis('off')


gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
_,thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)

plt.axis('off')
cv2.waitKey(0)
cv2.imshow("thresholding",thresh)
cv2.waitKey(0)

edges = cv2.dilate(cv2.Canny(thresh,0,255),None)

cv2.imshow(" dilation",edges)
cv2.waitKey(0)

plt.axis('off')
cnt = sorted(cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2], key=cv2.contourArea)[-1]
mask = np.zeros((256,256), np.uint8)
masked = cv2.drawContours(mask, [cnt],-1, 255, -1)

plt.axis('off')
cv2.imshow(" masked",masked)
cv2.waitKey(0)
dst = cv2.bitwise_and(img, img, mask=mask)
segmented = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)