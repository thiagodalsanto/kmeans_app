from tkinter import filedialog
import tkinter as tk
import cv2
from PIL import Image, ImageTk

class ConfigFileFrame:
    def __init__(self, frame_image, label_original_image):
        self.frame_image = frame_image
        self.image_path = None
        self.original_image = None
        self.label_original_image = label_original_image

    def open_file(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.load_image()

    def load_image(self):
        self.original_image = cv2.imread(self.image_path)
        self.visualize_loaded_image(self.original_image.copy())

    def visualize_loaded_image(self, img):
        if self.label_original_image:
            self.label_original_image.destroy()
        
        resized_image = cv2.resize(img, (640, 480))
        resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(resized_image_rgb)
        tk_image = ImageTk.PhotoImage(image=pil_image)

        self.label_original_image = tk.Label(self.frame_image, image=tk_image)
        self.label_original_image.image = tk_image
        self.label_original_image.pack(expand=True, fill="both")
        self.label_original_image.configure(bg="#121212")

        self.frame_image.update_idletasks()