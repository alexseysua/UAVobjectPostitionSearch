import cv2
import os

def loadUserPhotos(folder_path):
  photos = []
  for i in range(len(os.listdir(folder_path))):
    path = f'{folder_path}probka{i+1}.png'
    photos.append(path)
  return photos

def loadTiles(folder_path):
  tileMap = []
  for i in range(len(os.listdir(folder_path))):
    path = f'{folder_path}{i+1}.png'
    photo = cv2.imread(path,cv2.IMREAD_COLOR)
    tileMap.append([path, photo, 0])
  return tileMap

def printFormattedMatches(result):
  print(f'''
  Foto with object: {result['photo_path']}
  Highest-ratio match: 
    photo: {result['highest_ratio_match'][0]}
    ratio: {round(result['highest_ratio_match'][1],3)}
  Lowest-ratio match:
    photo: {result['lowest_ratio_match'][0]}
    ratio: {round(result['lowest_ratio_match'][1],3)}
        ''')