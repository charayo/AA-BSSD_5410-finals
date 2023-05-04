from PIL import Image, ImageOps
import math


def convolve(img, sz, step):
    # if the pixels are an odd size, we need a whole number
    start = math.floor(sz / 2)
    con_pixels = []
    for x in range(start, img.size[0] - 1, step):
        for y in range(start, img.size[1] - 1, step):
            # top row
            tl = img.getpixel((y - 1, x - 1))
            tc = img.getpixel((y - 1, x))
            tr = img.getpixel((y - 1, x + 1))

            # center row
            lc = img.getpixel((y, x - 1))
            cc = img.getpixel((y, x))
            rc = img.getpixel((y, x + 1))

            # bottom row
            bl = img.getpixel((y + 1, x - 1))
            bc = img.getpixel((y + 1, x))
            br = img.getpixel((y + 1, x + 1))

            sum = tl * 3 + tc * 10 + tr * 3 + lc * 0 + cc * 0 + rc * 0 + bl * -3 + bc * -10 + br * -3
            div = 1
            y_ave = math.floor(sum / div)

            sum = tl * 3 + tc * 0 + tr * -3 + lc * 10 + cc * 0 + rc * -10 + bl * 3 + bc * 0 + br * -3
            div = 1
            x_ave = math.floor(sum / div)

            sum = tl * -3 + tc * -10 + tr * -3 + lc * 0 + cc * 0 + rc * 0 + bl * 3 + bc * 10 + br * 3
            div = 1
            n_y_ave = math.floor(sum / div)
            #
            sum = tl * -3 + tc * 0 + tr * 3 + lc * -10 + cc * 0 + rc * 10 + bl * -3 + bc * 0 + br * 3
            div = 1
            n_x_ave = math.floor(sum / div)

            ave = max(y_ave, n_y_ave, n_x_ave, x_ave)
            con_pixels.append(ave)
    # our new image is smaller than original and needs to be a whole number
    dims = (math.floor(img.size[0] / step) - 1, math.floor(img.size[1] / step) - 1)
    output = Image.new('L', dims)
    print(len(con_pixels))
    output.putdata(con_pixels)
    output.show()

# end def convolve.py (img, sz, step):


kernel = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]
kernel_sum = sum(sum(row) for row in kernel)


def blur_image(img, sz, step):
    # if the pixels are an odd size, we need a whole number
    start = math.floor(sz / 2)
    con_pixels = []
    for x in range(start, img.size[0] - 1, start):
        for y in range(start, img.size[1] - 1, start):
            # calculate weighted average using Gaussian kernel
            pixels = [
                img.getpixel((y + j, x + i)) for i in range(-1, 2) for j in range(-1, 2)
            ]
            ave = sum(pixels[k] * kernel[i][j] for i in range(3) for j in range(3) for k in range(9))
            ave //= kernel_sum
            con_pixels.append(ave)
    # our new image is smaller than original and needs to be a whole number
    # dims = (math.floor(img.size[0] / step) - 1, math.floor(img.size[1] / step) - 1)
    output = Image.new('L', img.size)
    print(len(con_pixels))
    output.putdata(con_pixels)
    output.show()


kernel_x = [[-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
            ]

kernel_y = [[-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
            ]


def edge(img, sz, step):
    # ...
    start = math.floor(sz / 2)
    con_pixels = []
    for x in range(start, img.size[0] - 1, step):
        for y in range(start, img.size[1] - 1, step):
            # ...
            # apply Sobel filter
            pixels = [
                img.getpixel((y + j, x + i)) for i in range(-1, 2) for j in range(-1, 2)
            ]
            x_ave = sum(pixels[k] * kernel_x[i][j] for i in range(3) for j in range(3) for k in range(9))
            y_ave = sum(pixels[k] * kernel_y[i][j] for i in range(3) for j in range(3) for k in range(9))
            ave = math.sqrt(x_ave ** 2 + y_ave ** 2)
            con_pixels.append(int(ave))
    # our new image is smaller than original and needs to be a whole number
    dims = (math.floor(img.size[0] / step) - 1, math.floor(img.size[1] / step) - 1)
    output = Image.new('L', dims)
    print(len(con_pixels))
    output.putdata(con_pixels)
    output.show()
