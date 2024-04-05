import cv2
import numpy as np
from google.colab import drive

sift = cv2.SIFT_create()
bf = cv2.BFMatcher()
drive.mount('/content/drive')

userPhotoPath = '/content/probka4.png'
userPhoto = cv2.imread(userPhotoPath, cv2.IMREAD_COLOR)
keypointsUser, descriptorsUser = sift.detectAndCompute(userPhoto, None)

kafelki = []
for i in range(32):
  path = f'/content/drive/MyDrive/dane/{i+1}.png'
  photo = cv2.imread(path,cv2.IMREAD_COLOR)
  kafelki.append([path, photo, 0])

for p in kafelki:
  keypoints_p, descriptors_p = sift.detectAndCompute(p[1], None)
  matches = bf.knnMatch(descriptorsUser, descriptors_p, k=2)

  good_matches = []
  for m, n in matches:
    if m.distance < 0.5 * n.distance:
      good_matches.append(m)
  matching_ratio = len(good_matches) / len(keypointsUser)
  p[2] = matching_ratio

sorted_data = sorted(kafelki, key=lambda x: x[2])
print('najlepszy match:', sorted_data[-1][0], sorted_data[-1][2])
print('najsłabszy match:', sorted_data[0][0], sorted_data[0][2])


