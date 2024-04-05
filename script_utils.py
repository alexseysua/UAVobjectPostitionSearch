import cv2

def loadTiles(folder_path):
  tileMap = []
  for i in range(32):
    path = f'{folder_path}{i+1}.png'
    photo = cv2.imread(path,cv2.IMREAD_COLOR)
    tileMap.append([path, photo, 0])
  return tileMap