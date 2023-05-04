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


def blur_image(img, kernel_size=3):
    # Define a kernel for blurring
    kernel = [[1 / kernel_size ** 2] * kernel_size for i in range(kernel_size)]
    print(kernel)
    # Define image dimensions and create output image
    width, height = img.size
    output = Image.new('RGB', (width, height))

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            # Apply the kernel to the pixel and its neighbors
            pixel_sum = [0, 0, 0]
            for i in range(-kernel_size // 2, kernel_size // 2 + 1):
                for j in range(-kernel_size // 2, kernel_size // 2 + 1):
                    # Get the pixel value and kernel weight
                    px, py = x + i, y + j
                    if px < 0 or py < 0 or px >= width or py >= height:
                        # Ignore pixels outside the image boundaries
                        continue
                    weight = kernel[i + kernel_size // 2][j + kernel_size // 2]
                    r, g, b = img.getpixel((px, py))
                    pixel_sum[0] += int(r * weight)
                    pixel_sum[1] += int(g * weight)
                    pixel_sum[2] += int(b * weight)
            # Set the output pixel to the blurred value
            output.putpixel((x, y), tuple(pixel_sum))

    return output
