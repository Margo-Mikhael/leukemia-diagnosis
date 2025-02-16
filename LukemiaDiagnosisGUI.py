import tkinter as tk
from tkinter import filedialog, Label, Button
import cv2
from PIL import Image, ImageTk
import numpy as np

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = process_image(image)
    
    display_image(image, original_label)
    display_image(processed_image, processed_label)

def process_image(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

def display_image(image, label):
    image = cv2.resize(image, (250, 250))
    im = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=im)
    label.config(image=imgtk)
    label.image = imgtk

# GUI Setup
root = tk.Tk()
root.title("ALL Diagnosis Tool")
root.geometry("600x400")

Button(root, text="Load Image", command=load_image).pack()
original_label = Label(root)
original_label.pack()
processed_label = Label(root)
processed_label.pack()

root.mainloop()
