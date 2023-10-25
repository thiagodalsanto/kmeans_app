import os
import time
import cv2
from components.kmeans import KMeans

class KMeansUtils:
    def __init__(self, original_image, dimensions_variable, clusters_variables):
        self.original_image = original_image
        self.dimensions_variable = dimensions_variable
        self.clusters_variables = clusters_variables

    def apply_kmeans_on_images(self):
        KMeans(self.original_image, self.dimensions_variable.get(), self.clusters_variables.get())

        images_directory = '../results'
        image_files = os.listdir(images_directory)
        image_files = [os.path.join(images_directory, file) for file in image_files if file.endswith('.jpg')]
        
        for image_file in image_files:
            image = cv2.imread(image_file)
            if image is not None:
                cv2.namedWindow(os.path.basename(image_file), cv2.WINDOW_NORMAL)
                cv2.imshow(os.path.basename(image_file), image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()