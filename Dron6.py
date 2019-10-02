from PIL import Image

r = 30

def get_main_color(file):
    img = Image.open(file)
    colors = img.getcolors(2560) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

img = Image.open("Photo.png")
imgwidth, imgheight = img.size
#img.crop((30, 30, w-80, h-40)).save("file.png")
amount = 1;
width, length = 20, 20

for i in range(0,imgheight,length):
    for j in range(0,imgwidth,width):
        if j+width > imgwidth:
            w = imgwidth
        else:
            w = j+width
        if i+length > imgheight:
            h = imgheight
        else:
            h = i+length
        
        img.crop((j, i, w, h)).save("images/file"+str(amount)+".png")
        amount=amount+1
print(amount)
       


for q in range(1,amount,1):
    a, b, c = (get_main_color("images/file"+str(q)+".png"))
    max=a
    if(b>max):
        max =b
    if(c>max):
        max =c
    if(a==b and a==c and c==b and a<=56):
        print("wet")
    elif (a==b and a==c and c==b and a>56 and a<209):
        print("woter")
    elif(max>209 and max-b<=r and max-c<=r):
        print("sky")
    elif(max<=56 and max-b<=r and max-c<=r):
        print("wet")
    elif(max<=209 and max-b<=r and max-c<=r):
        print("woter")
    else:
        print("isn't sky and isn't field ")
