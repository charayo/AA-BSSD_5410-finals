from tkinter import *
import tkinter as tk

from PIL import ImageTk

from convolve import *
from emboss import *

current_image = Image.open("boids.png")


def handle_emboss(the_img):
    global current_image
    my_image = Image.open(the_img)
    current_image = my_image
    # convert the image to RGB mode to ensure that getpixel() always returns a tuple of three values
    my_image = my_image.convert("RGB")
    embossed_image = emboss2(my_image, 1)
    return embossed_image


def handle_blurr(the_img):
    global current_image
    my_image = Image.open(the_img)
    current_image = my_image
    return blur_image(my_image)


def change_image(image):
    global photo_image
    image_width, image_height = image.size
    if image_width > 900:
        new_image_height = int((900 / image_width) * image_height)
        image = image.resize((900, new_image_height), Image.ANTIALIAS)
    photo_image = ImageTk.PhotoImage(image)
    image_label.config(image=photo_image)


page_height = "1300"

root = Tk()

# create the left frame for the image
left_frame = tk.Frame(root, width=900, height=1300, bg="black")
left_frame.grid(row=0, column=0, sticky="nsew")

# create the right frame for the buttons
right_frame = tk.Frame(root, width=400, height=1300, bg="white")
right_frame.grid(row=0, column=1, sticky="nsew")

# open the image file and resize it to fit within the left frame
image = Image.open("sample.png")
image_width, image_height = image.size
if image_width > 900:
    new_image_height = int((900 / image_width) * image_height)
    image = image.resize((900, new_image_height), Image.ANTIALIAS)
photo_image = ImageTk.PhotoImage(image)

# create the image widget and add it to the left frame
image_label = tk.Label(left_frame, image=photo_image)
image_label.pack(fill="both", expand=False, pady=20, padx=20)

# create four buttons in the right frame
button1 = tk.Button(right_frame, text="Emboss", command=lambda: change_image(handle_emboss("sample.png")))
button1.pack(side="top", pady=20, padx=40)

button2 = tk.Button(right_frame, text="Blur", command=lambda: change_image(handle_blurr("new.jpeg")))
button2.pack(side="top", pady=20, padx=40)

button3 = tk.Button(right_frame, text="Detect Edge")
button3.pack(side="top", pady=20, padx=40)

button4 = tk.Button(right_frame, text="Reset", command=lambda: change_image(current_image))
button4.pack(side="top", pady=20, padx=40)

root.mainloop()


def main():
    og_image = Image.open("ayo.jpeg")
    # blur_image(og_image).show()
    # convolve2(gray_image, 3, 1)


# end def main):

if __name__ == "__main__":
    main()
