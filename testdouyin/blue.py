import Image

img = Image.open("blueBlack.JPG")

for i in xrange(300):
    for j in xrange(300):

        r, g, b = img.getpixel((i, j))
        if (b > g and b > r):  # 对蓝色进行判断
            b = 127
            g = 127
            r = 127

        img.putpixel((i, j), (r, g, b))

img.show()