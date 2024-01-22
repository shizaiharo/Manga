import os, math, random
from PIL import Image
from _keras import check_img_for_word
# from tfJS_Selenium_def import tfJS

MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
class Quadtree:
    def __init__(self):
        self.images = []
        # self.content = ""
    
    def check_img(self, path, image):
        w = image.width
        h = image.height
        length = 75
        if image.format == "PNG":
            image = image.convert("RGB")
        image.save(path + ".jpg")
        stack = [path]
        
        
        level = 0
        count = 0
        s = len(stack)
        x,  y = 0, 0
        while stack:
            current_path = stack.pop()
            # print(current_path)
            current_image = Image.open(current_path+".jpg")
            w, h = current_image.size
            # if  tfJS(current_path+".jpg")> 0.5 or w <= length or h <= length:
            if check_img_for_word(current_path+".jpg") > 0.5 or w <= length or h <= length:
                self.images.append(current_path[len(MainPath + "/temp/"):]+".jpg") 
            else:
                devided_images = self.subdivide(current_image,x,y)
                for j in range(0,len(devided_images)):
                    x, y = int(devided_images[j][1]), int(devided_images[j][2])
                    pure_name = current_path.split('_')[1].split('-')[0]
                    newimg_path = current_path.split('_')[0] +"_"+ str(self.naming(s,int(pure_name),j))+"-("+str(x)+","+str(y)+")"
                    devided_images[j][0].save(newimg_path + ".jpg")
                    stack.append(newimg_path)
                count += 1 
                os.remove(current_path+".jpg")
                
            if count == s :
                s = len(stack)
        # self.coment = str(self.images)

    def subdivide(self,image,x,y):
        w, h = image.size
        
        new_images = []
        new_images.append([image.crop((w/2, 0,w,h/2)), x+w/2, y]) #up right 1
        #new_images.append([image.crop((w/2, 0,w,h/4)),x+w/2, y]) #2
        #new_images.append([image.crop((w*3/4, h/4,w,h/2)),x+w*3/4, h/4]) #3
        #new_images.append([image.crop((w/2, h/4,w*3/4,h/2)),x+w/2, h/4]) #4
        
        new_images.append([image.crop((0, 0, w/2, h/2)), x, y]) #up left 5
        #new_images.append([image.crop((0, 0, w/2, h/2)),x,y]) #6
        #new_images.append([image.crop((0, 0, w/2, h/2)),x,y]) #7
        #new_images.append([image.crop((0, 0, w/2, h/2)),x,y]) #8

        new_images.append([image.crop((w/2, h/2, w, h)), x+w/2, y+h/2]) #down right
        new_images.append([image.crop((0, h/2, w/2, h)), x, y+h/2]) # down left

        
        return new_images
    
    def get_images(self):
        return self.images
    
    def naming(self,s, c, i):
        n = math.log(s, 4)
        w = int(pow(2, n + 1))

        a = 0
        si = math.sqrt(s)
        counter = 0
        for k in range(c):
            if counter < si - 1:
                a += 2
                counter += 1
            else:
                a += 2 + w
                counter = 0
        a = int(a)

        if i == 0: return a
        if i == 1: return a + 1
        if i == 2: return a + w
        if i == 3: return a + w + 1


def check_img_for_word(img):
    return 0
    return round(random.random(),1)

# tree = Quadtree()
# image = Image.open(MainPath + "/003.png")
# tree.check_img(MainPath + "/temp/" + "003"+"_0", image)