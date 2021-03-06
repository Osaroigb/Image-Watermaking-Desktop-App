from tkinter import Tk, filedialog, Label, Button
from PIL import Image, ImageTk, ImageDraw, ImageFont

# create the main window of an application
window = Tk()
window.minsize(width=600, height=600)
window.config(padx=40, pady=20)
window.title("Image Watermarking App")


def upload_image():
    """a function that uploads an image from the local file system and watermarks it with predefined text"""

    path = filedialog.askopenfilename(filetypes=[("Image File", ".jpeg", ".png")])

    # open an image and create an image object from it
    img = Image.open(path)

    # getting initial image dimensions
    width, height = img.size

    # (width, height) resize the uploaded image to fit the tkinter window
    img = img.resize((500, 500), Image.ANTIALIAS)

    # create a draw object
    draw = ImageDraw.Draw(img)

    # create a predefined text and font object
    logo = "OSAROIGB"
    img_font = ImageFont.truetype(font="arial.ttf", size=36)

    # position the text in the top right corner by calculating the x and y coordinates
    text_width, text_height = draw.textsize(text=logo, font=img_font)
    resize_width, resize_height = img.size

    x = resize_width - text_width - 10
    y = 0

    # draw watermark on image via draw object
    draw.text(xy=(x, y), text=logo, fill="purple", font=img_font)

    # create a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object
    tk_image = ImageTk.PhotoImage(img)

    # use the Label widget to display the image on the screen
    img_label = Label(window, image=tk_image)
    img_label.image = tk_image
    img_label.pack()

    # resizing the image back to it's original dimensions
    img = img.resize((width, height), Image.ANTIALIAS)

    # save the watermarked image in the working directory
    img.save("watermarked.jpeg")


img_button = Button(text="Open an image", command=upload_image)
img_button.pack(pady=20)

# start the GUI
window.mainloop()
