import cv2
import numpy as np
from google.colab import drive

#paths to files with photos with object you want to determine location
userPhotos = ['/content/probka3.png', '/content/probka4.png']

sift = cv2.SIFT_create()
bf = cv2.BFMatcher()
drive.mount('/content/drive')

for path in userPhotos:
  userPhoto = cv2.imread(path, cv2.IMREAD_COLOR)
  keypointsUser, descriptorsUser = sift.detectAndCompute(userPhoto, None)

  tiles = []
  for i in range(32):
    path = f'/content/drive/MyDrive/dane/{i+1}.png'
    photo = cv2.imread(path,cv2.IMREAD_COLOR)
    tiles.append([path, photo, 0])

  for p in tiles:
    keypoints_p, descriptors_p = sift.detectAndCompute(p[1], None)
    matches = bf.knnMatch(descriptorsUser, descriptors_p, k=2)

    good_matches = []
    for m, n in matches:
      if m.distance < 0.5 * n.distance:
        good_matches.append(m)
    matching_ratio = len(good_matches) / len(keypointsUser)
    p[2] = matching_ratio

  sorted_data = sorted(tiles, key=lambda x: x[2])
  print('Foto with object: ', path)
  print('Highest-ratio match:', sorted_data[-1][0], sorted_data[-1][2])
  print('Lowest-ratio match:', sorted_data[0][0], sorted_data[0][2], '\n')


