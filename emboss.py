def emboss(image, level=1.0):
    # convert image to grayscale

    # define kernel
    kernel = ((-3, -3, 0), (-3, 0, 3), (0, 3, 3))

    # apply convolution
    output = image.copy()
    width, height = output.size
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            conv = 0
            for i in range(3):
                for j in range(3):
                    pixel = image.getpixel((x + i - 1, y + j - 1))
                    conv += pixel * kernel[i][j]
                    # adjust emboss level
            conv *= level
            conv = max(0, min(conv, 255))
            output.putpixel((x, y), int(conv))
    return output


def emboss2(image, level=1.0):
    # define kernel
    kernel = (
        (-2, -1, 0),
        (-1, 1, 1),
        (0, 1, 2)
    )

    # apply convolution
    output = image.copy()
    width, height = output.size
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            conv_r, conv_g, conv_b = 0, 0, 0
            for i in range(3):
                for j in range(3):
                    pixel_r, pixel_g, pixel_b = image.getpixel((x + i - 1, y + j - 1))
                    conv_r += pixel_r * kernel[i][j]
                    conv_g += pixel_g * kernel[i][j]
                    conv_b += pixel_b * kernel[i][j]

            # adjust emboss level
            conv_r *= level
            conv_g *= level
            conv_b *= level

            conv_r = max(0, min(conv_r, 255))
            conv_g = max(0, min(conv_g, 255))
            conv_b = max(0, min(conv_b, 255))

            output.putpixel((x, y), (int(conv_r), int(conv_g), int(conv_b)))
    return output
