from PIL import Image

img = Image.open("/Users/andresfernandez/Desktop/ImageToAscii/images/example2.jpeg").convert('L')

img = img.resize(((img.width // 2), int(img.height // 2)))


brightness_thresholds = [160, 130, 100, 70, 40, 25, 10, 5, 0]
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

ascii_art = []
for y in range(img.height):
    row = ''
    for x in range(img.width):
        brightness = img.getpixel((x, y))
        for i, threshold in enumerate(brightness_thresholds):
            if brightness >= threshold:
                row += ascii_chars[i]
                break
    ascii_art.append(row)

with open("ascii_image.txt", 'w') as file:
    for row in ascii_art:
        file.write(row + '\n')






        


        









