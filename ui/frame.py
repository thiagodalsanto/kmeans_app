import tkinter as tk
from config.configuration import Configuration
from utils.kmeans_utils import KMeansUtils

class Frame:
    def __init__(self, master):
        self.master = master

        self.bottons_frame_buttons = None
        self.top_frame_buttons = None
        self.button_load_image = None
        self.dropdown_button_cluster = None
        self.dropdown_button_dimension = None
        self.button_generate_kmeans_button = None

        self.frame_image = None
        self.label_original_image = None

        self.var_dimensions = None
        self.var_clusters = None

        self.KMeansUtils = None

        self.general_configuration()

    def general_configuration(self):
        self.master.title("Kmeans App Image")
        self.master.geometry("640x590")
        self.master.configure(bg="#121212")
        self.settings_buttons()
        self.image_configuration()
        self.send_and_kmeans_buttons()

    def image_configuration(self):
        self.frame_image = tk.Frame(self.master)
        self.frame_image.pack(side="bottom", expand=True, fill="both")
        self.frame_image.configure(bg="#121212")

    def send_and_kmeans_buttons(self):
        self.bottons_frame_buttons = tk.Frame(self.master)
        self.bottons_frame_buttons.configure(bg="#121212")
        self.bottons_frame_buttons.pack(side="bottom", pady=10)

        self.button_load_image = tk.Button(self.bottons_frame_buttons, text="Send Image", command=self.open_file, bg="light blue", fg="black")
        self.button_load_image.pack(side="left", padx=10)

        self.button_generate_kmeans_button = tk.Button(self.bottons_frame_buttons, text="KMeans", command=self.generate_kmeans, state="disabled", bg="light blue", fg="black")
        self.button_generate_kmeans_button.pack(side="left", padx=10)

    def settings_buttons(self):
        self.top_frame_buttons = tk.Frame(self.master)
        self.top_frame_buttons.configure(bg="#121212")
        self.top_frame_buttons.pack(side="top", pady=10)

        clusters = ["1", "2", "3", "4", "5", "6"]
        image_dimensions = ["1", "2", "3"]

        label_dimensions = tk.Label(self.top_frame_buttons, text="Dimension:", bg="#121212", fg="white")
        label_dimensions.pack(side="left")
        self.var_dimensions = tk.StringVar(self.master)
        self.var_dimensions.set("1")
        self.dropdown_button_dimension = tk.OptionMenu(self.top_frame_buttons, self.var_dimensions, *image_dimensions)
        self.dropdown_button_dimension.pack(side="left", padx=10)
        self.dropdown_button_dimension.config(bg="light blue", fg="black")

        label_clusters = tk.Label(self.top_frame_buttons, text="Centroids:", bg="#121212", fg="white")
        label_clusters.pack(side="left")
        self.var_clusters = tk.StringVar(self.master)
        self.var_clusters.set("1")
        self.dropdown_button_cluster = tk.OptionMenu(self.top_frame_buttons, self.var_clusters, *clusters)
        self.dropdown_button_cluster.pack(side="left", padx=10)
        self.dropdown_button_cluster.config(bg="light blue", fg="black")


    def open_file(self):
        config_file_frame = Configuration(self.frame_image, self.label_original_image)
        config_file_frame.open_file()

        self.label_original_image = config_file_frame.label_original_image
        self.KMeansUtils = KMeansUtils(config_file_frame.original_image, self.var_dimensions, self.var_clusters)
        self.button_generate_kmeans_button["state"] = "normal"

    def generate_kmeans(self):
        self.KMeansUtils.apply_kmeans_on_images()