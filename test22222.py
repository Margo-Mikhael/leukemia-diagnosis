import cv2
import numpy as np
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
import matplotlib.pyplot as plt
import math

img1 = cv2.imread('Im001_1.jpg')
img = cv2.resize(img1, (500, 500))
cv2.waitKey(0)
cv2.imshow("original",img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
filtro = cv2.pyrMeanShiftFiltering(img, 20, 40)
gray = cv2.cvtColor(filtro, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.waitKey(0)
cv2.imshow("thresholding",thresh)
cv2.waitKey(0)
######median filter
median = cv2.medianBlur(thresh, 5)
cv2.waitKey(0)
cv2.imshow("after median filtering",median)
cv2.waitKey(0)

#####

kernel = np.ones((5,5),np.uint8)
#Now we need to remove any small white noises in the image. 
#For that we can use morphological opening.
opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
cv2.waitKey(0)
cv2.imshow("after morphology",opening)
cv2.waitKey(0)

contornos, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
buracos = []
min_area = 1300
average_cell_area = 650
connected_cell_area = 1000
cells = 0

dist = ndi.distance_transform_edt(thresh)

dist_visual = dist.copy()
local_max = peak_local_max(dist, indices=False, min_distance=20, labels=thresh)
markers = ndi.label(local_max, structure=np.ones((3, 3)))[0]
labels = watershed(-dist, markers, mask=thresh)

for con in contornos:
    area = cv2.contourArea(con)
    if area > min_area:
        cv2.drawContours(thresh, buracos, -1, 255, -1)## image -- list--
        buracos.append(con)
        if area > connected_cell_area:
            cells += math.ceil(area / average_cell_area)
        else:
            cells += 1
print('Cells: {}'.format(cells))

titulos = ['Original image', 'Binary Image', 'Distance Transform', 'Watershed']
imagens = [img, thresh, dist_visual, labels]
fig = plt.gcf()
fig.set_size_inches(16, 12)  
for i in range(4):
    plt.subplot(2,2,i+1)
    if (i == 3):
      cmap = "jet"
    else:
       cmap = "gray"
    plt.imshow(imagens[i], cmap)
    plt.title(titulos[i]) 
    plt.xticks([]),plt.yticks([])     
plt.show()
area = cv2.contourArea(con)
hull = cv2.convexHull(con)
#print("the hull",hull)
hull_area = cv2.contourArea(hull)
print("hull area",hull_area)
solidity = float(area)/hull_area
print("solidity",solidity)
area = cv2.contourArea(con)
print("areaa",area)
perimeter = cv2.arcLength(con,True)
print("the perimeter",perimeter)
formfactor= int((4*math.pi*area/perimeter))
print("Form factor",formfactor)
compactness=pow(perimeter,2)/area
print("compactness",compactness)


