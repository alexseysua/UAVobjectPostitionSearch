from google.colab import drive
from object_matcher import findMatches
from script_utils import loadTiles

drive.mount('/content/drive')

#paths to files with photos with object you want to determine location
userPhotos = ['/content/probka3.png', '/content/probka4.png']

tileMap = loadTiles('/content/drive/MyDrive/dane/')

for path in userPhotos:
  print(findMatches(path, tileMap))