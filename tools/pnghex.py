from PIL import Image
import os
def png_to_hex(png_file):
    img =  Image.open(png_file).convert('1')
    width, height = img.size
    data = list(img.getdata())
    hex_string = ''
    for y in range(height):
        row = data[y*width:(y+1)*width]
        byte = ''
        for x in range(width):
            byte += '1' if row[x] == 0 else '0'
            if (x+1) % 8 == 0:
                hex_string += f'{int(byte, 2):02X}'
                byte = ''
    return hex_string

def hex_to_png(hex_string, png_file):
    width = 8 if len(hex_string) == 32 else 16
    height = 16
    data = []
    for i in range(0, len(hex_string), 2):
        byte = format(int(hex_string[i:i+2], 16), '08b')
        data.extend([0 if b == '0' else 255 for b in byte])
    img =  Image.new ('1', (width, height))
    img.putdata(data)
    img.save (png_file)

png_folder=r"C:\Users\Lakeus\Downloads\CESI\cjk-{}"
ext="bcdef"

for i in ext:
    hex_filename="cjk-{}.hex".format(i)
    hex_file = os.path.join(r"C:\Users\Lakeus\Downloads\CESI", hex_filename)
    with open(hex_file, "w", encoding="utf-8") as f:
        for filename in os.listdir(png_folder.format(i)):
            if filename.endswith(".png"):
                png_file=os.path.join(png_folder.format(i), filename)
                unicode_value = filename.split('u')[1].split(".")[0]
                f.write(unicode_value.upper()+":"+png_to_hex(png_file)+"\n")

