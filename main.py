from tkinter import Tk, filedialog, Label, Button
from PIL import Image, ImageTk, ImageDraw, ImageFont

# create the main window of an application
window = Tk()
window.minsize(width=320, height=20)
window.config(padx=40, pady=20)
window.title("Image Watermarking App")


def upload_image():
    """a function that uploads an image from the local file system and watermarks it with predefined text"""

    path = filedialog.askopenfilename(filetypes=[("Image File", ".jpeg", ".png")])

    # open an image and create an image object from it
    img = Image.open(path)

    # create a draw object
    draw = ImageDraw.Draw(img)

    # create a predefined text and font object
    logo = "OSAROIGB"
    img_font = ImageFont.truetype(font="arial.ttf", size=36)

    # position the text by calculating the x and y coordinates
    text_width, text_height = draw.textsize(text=logo, font=img_font)
    width, height = img.size

    x = width - text_width - 10
    y = height / 3

    # draw watermark on image via draw object
    draw.text(xy=(x, y), text=logo, fill="purple", font=img_font)

    # save the watermarked image in the working directory
    img.save("watermark.png")

    # create a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object
    tk_image = ImageTk.PhotoImage(img)

    # use the Label widget to display the image on the screen
    img_label = Label(window, image=tk_image)
    img_label.image = tk_image
    img_label.pack()


img_button = Button(text="Open an image", command=upload_image)
img_button.pack()

# start the GUI
window.mainloop()
