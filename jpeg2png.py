from PIL import Image
import os

def convert_jpg_to_png(input_folder, output_folder)
    if not os.path.exists(output_folder)
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder)
        if filename.lower().endswith('.jpg')
            img = Image.open(os.path.join(input_folder, filename))
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            img.save(output_path, 'PNG')
            print(f'Konwersja {filename} zakończona.')

input_folder = 'input/path'
output_folder = 'output/path'

convert_jpg_to_png(input_folder, output_folder)
