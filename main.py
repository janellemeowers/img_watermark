from tkinter import *
from tkinter.filedialog import askopenfilename
import PIL.Image, PIL.ImageTk, PIL.ImageDraw,PIL.ImageFont

window = Tk()



final_img = None

def upload_img():
    #access image to update canvas
    global final_img
    #get entered watermark text. ex: @janellemeowers
    text = watermark_entry.get()
    #get uploaded file
    uploaded_img = askopenfilename()
    #open PIL.Image
    img = PIL.Image.open(uploaded_img)
    # drawing object
    drawing = PIL.ImageDraw.Draw(img)
    black = (3, 8, 12)
    #specify font path
    font = PIL.ImageFont.truetype("/Library/Fonts/Arial.ttf", 20)
    #top left
    drawing.text((20,20), text, fill=black, font=font)
    #post image
    final_img = PIL.ImageTk.PhotoImage(image=img)
    canvas = Canvas(window, width=250, height=250)
    canvas.pack()
    canvas.create_image(100,100, image=final_img)
    #for downloading
    img.show()


window.title("Image Watermarker")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

watermark_text = Label(text="Enter your watermark:", fg="blue")
watermark_text.pack()

watermark_entry = Entry(width=20)
watermark_entry.pack()

upload_btn = Button(text='Upload Image',
   width=20, command=upload_img)
upload_btn.pack()




window.mainloop()