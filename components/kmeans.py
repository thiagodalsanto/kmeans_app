import cv2
import numpy as np
import os
import shutil

class KMeans:
    def __init__(self, original_image, image_dimensions, centroid_value):
        self.centroid = centroid_value

        self.image_dimensions = image_dimensions
        self.centroid = centroid_value
        self.values_configuration()

        self.image = original_image.copy()
        self.height, self.width, self.channels = self.image.shape

        self.pixels = self.image.reshape((-1, self.image_dimensions)).astype(np.float32)

        self.run()

    def values_configuration(self):
        for i in range(1, 7):
            if self.centroid == f"{i}":
                self.centroid = i
        for i in range(1, 4):
            if self.image_dimensions == f"{i}":
                self.image_dimensions = i

    def run(self):
        if os.path.exists('results/'):
            shutil.rmtree('results/')
        else:
            os.makedirs('results/')

        for k in range(1, self.centroid + 1):
            criteria_for_stop = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 80, 0.25)
            _, labels, centers = cv2.kmeans(self.pixels, k, None, criteria_for_stop, 10, cv2.KMEANS_RANDOM_CENTERS)
            
            centers = np.uint8(centers)
            centroid_image = centers[labels.flatten()]
            centroid_image = centroid_image.reshape(self.image.shape)

            output_filename = os.path.join('results/', f'centroid_{k}.jpg')
            cv2.imwrite(output_filename, centroid_image)

        cv2.waitKey(5)
        cv2.destroyAllWindows()
