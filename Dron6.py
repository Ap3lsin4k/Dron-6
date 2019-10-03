from PIL import Image

r = 50
def name(color):
    a, b, c = color
    max=a
    if(b>max):
        max =b
    if(c>max):
        max =c
    if(c-a>=50 or c-b>=50):
        return "sky"
    elif (a>=135 and a<=165 and b>=105 and b<=130 and c<95):
        return "woter"
    elif(max>209 and max-b<=r and max-c<=r):
        return "sky"
    elif(max<=100 and max-b<=r and max-c<=r):
        return "wet"
    elif(max<=209 and max-b<=r and max-c<=r):
        return "woter"
    else:
        return "isn't"
def imposition(img1,img2):
    im1 = img1
    im2 = img2
    im1.paste(im2, (j,i), im2) # Последний параметр — альфаканал, используемый для наложения
    im1.save("img1.png")

def get_main_color(img):
    colors = img.getcolors(25600) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")
img=Image.open("Photo.jpg")
imgwidth, imgheight = img.size
#img.crop((30, 30, w-80, h-40)).save("file.png")
amount = 1;
width, length = 15, 15
img2 = Image.open("kapli.png")
img2 = img2.resize((width,length), Image.ANTIALIAS)
img2.save("kaphotosavepli.png")
Photosave=Image.open("Photo.jpg")
for i in range(0,imgheight,length):
    for j in range(0,imgwidth,width):
        imgmain = Image.open("Photo.jpg")
        if j+width > imgwidth:
            w = imgwidth
        else:
            w = j+width
        if i+length > imgheight:
            h = imgheight
        else:
            h = i+length
        
        #img.crop((j, i, w, h)).save("images/file"+str(amount)+".png")
        cropimages=imgmain.crop((j, i, w, h))
        color = get_main_color(cropimages)
        imagename=name(color)
        if(imagename=="woter"):
            imposition(Photosave,img2)
        #cropimages.save("images/"+str(amount)+str(imagename)+str(color)+".png")
        amount=amount+1
print(amount)
Photosave.save("Save.jpg")
       

