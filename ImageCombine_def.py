import os
from PIL import Image

MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
# from math import abs

# def image_combine(images):
#     for image in images:
#         xy = image.split("(")[0].split(")")[0].split(",")
#         x, y = int(xy[0]),int(xy[1])

def vertical(up_path, down_path, output_path):
    up = Image.open(MainPath + "/temp/" + up_path)
    up_x = int(up_path.split("(")[1].split(")")[0].split(",")[0])
    up_y = int(up_path.split("(")[1].split(")")[0].split(",")[1])
    down = Image.open(MainPath + "/temp/" + down_path)
    down_x = int(down_path.split("(")[1].split(")")[0].split(",")[0])
    down_y = int(down_path.split("(")[1].split(")")[0].split(",")[1])
    left = max(up_x, down_x)
    # top_right = max(up_x + up.width, down_x + down.width)
    combined_width = max(up_x + up.width, down_x + down.width) - min(up_x, down_x)
    combined_height = up.height + down.height
    combined_image = Image.new('RGBA', (combined_width, combined_height))
    combined_image.paste(up, (0, 0))
    combined_image.paste(down, (abs(up_x - down_x), up.height))
    combined_image.save(output_path.split("(")[0]+"(" + str(left) + "," + str(up_y) + ")" + ".png")

def horizontal(left_path, right_path, output_path):
    left = Image.open(MainPath + "/temp/" + left_path)
    left_x = int(left_path.split("(")[1].split(")")[0].split(",")[0])
    left_y = int(left_path.split("(")[1].split(")")[0].split(",")[1])
    right = Image.open(MainPath + "/temp/" + right_path)
    right_x = int(right_path.split("(")[1].split(")")[0].split(",")[0])
    right_y = int(right_path.split("(")[1].split(")")[0].split(",")[1])
    top = max(left_y, right_y)
    # top_right = max(left_x + left.width, right_x + right.width)
    combined_height = max(left_y + left.height, right_y + right.height) - min(left_y, right_y)
    combined_width = left.width + right.width
    combined_image = Image.new('RGBA', (combined_width, combined_height))
    combined_image.paste(left, (0, 0))
    combined_image.paste(right, (left.width, abs(left_y - right_y)))
    combined_image.save(output_path.split("(")[0]+"(" + str(left_x) + "," + str(top) + ")" + ".png")
def combine(images):
    #ln = images[0].find("_")+1
    #rn = images[0].find("-")-1
    #comma = images[0].find(",")
    #rp = images[0].find(")")
    output_path = MainPath + "/temp/" + images[0].split(".")[0]
    # images = sorted(images, key = lambda x: (x[ln:rn], x[rn+2:comma-1], -x[comma+1:rp-1]))
    combined = []
    for image_path in images:
        image = Image.open(MainPath + "/temp/" + image_path)
        x = int(image_path.split("(")[1].split(")")[0].split(",")[0])
        y = int(image_path.split("(")[1].split(")")[0].split(",")[1])
        for subimage_path in images:
            subimage = Image.open(MainPath + "/temp/" + subimage_path)
            # if combined.index(subimage_path) >= 0: continue
            if subimage_path not in combined: continue
            
            sx = int(subimage_path.split("(")[1].split(")")[0].split(",")[0])
            sy = int(subimage_path.split("(")[1].split(")")[0].split(",")[1])
            if x == (sx+subimage.width): #left
                horizontal(subimage_path, image_path, output_path)
                print(image_path.split("(")[1].split(")")[0], 
                      subimage_path.split("(")[1].split(")")[0],
                      output_path.split("(")[1].split(")")[0]
                )
                combined.append(subimage_path)
            if sy == (x+image.height): #down
                vertical(image_path, subimage_path, output_path)
                print(image_path.split("(")[1].split(")")[0], 
                      subimage_path.split("(")[1].split(")")[0],
                      output_path.split("(")[1].split(")")[0]
                )
                combined.append(subimage_path)
            if y == (sy+subimage.height): #up
                vertical(subimage_path, image_path, output_path)
                print(image_path.split("(")[1].split(")")[0], 
                      subimage_path.split("(")[1].split(")")[0],
                      output_path.split("(")[1].split(")")[0]
                )
                combined.append(subimage_path)
            if sx == (x+image.width): #right
                horizontal(image_path, subimage_path, output_path)
                print(image_path.split("(")[1].split(")")[0], 
                      subimage_path.split("(")[1].split(")")[0],
                      output_path.split("(")[1].split(")")[0]
                )
                combined.append(subimage_path)

    return os.listdir(MainPath + "/temp/")

# Example usage
# image1_path = 'website.v3\japanese(0,0).jpg'
# image2_path = 'website.v3\japanese(1,2).jpg'
# output_path = 'website.v3\japanese('

# vertical(image1_path, image2_path, output_path)
# horizontal(image1_path, image2_path, output_path)

