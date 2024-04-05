from google.colab import drive
from object_matcher import findMatches
from script_utils import loadTiles, printFormattedMatches

drive.mount('/content/drive')

#paths to files with photos with object you want to determine location
userPhotos = loadUserPhotos('/content/drive/MyDrive/user_photos_data/')
tileMap = loadTiles('/content/drive/MyDrive/map_data_n_png/')

for path in userPhotos:
  printFormattedMatches(findMatches(path, tileMap))