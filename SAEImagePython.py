from PIL import Image

# B.1
def B1(image):
    i = Image.open(image)
    sortie = i.copy()
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            c = i.getpixel((x, y))
            sortie.putpixel((y, x), c)
    sortie.save("Imageout0.bmp")

B1("Imagetest.bmp")

# B.2
def B2(image):
    i = Image.open(image)
    sortie = i.copy()
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            sortie.putpixel((x, y), i.getpixel((abs(x - i.size[0]) - 1, y)))
    sortie.save("Imageout1.bmp")

B2("hall-mod_0.bmp")

# B.3

def B3(image):
    i = Image.open(image)
    sortie = i.copy()
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            r, v, b = i.getpixel((x, y))
            gris = int((r + v + b) / 3)
            sortie.putpixel((x, y), (gris, gris, gris))
    sortie.save("Imageout2.bmp")

B3("IUT-Orleans.bmp")

# B.4

def B4(image):
    i = Image.open(image)
    sortie = i.copy()
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            r, v, b = i.getpixel((x, y))
            if (r*r + v*v + b*b) > (255*255*3/2):
                sortie.putpixel((x, y), (255, 255, 255))
            else:
                sortie.putpixel((x, y), (0, 0, 0))
    sortie.save("Imageout3.bmp")

B4("IUT-Orleans.bmp")