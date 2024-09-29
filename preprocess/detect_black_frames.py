import cv2
import numpy as np


def is_image_all_black(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Check if image is None
    if image is None:
        print(f"Error: Could not read image '{image_path}'.")
        return False

    # Convert the image to grayscale (if it's not already)
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image  # It's already grayscale

    # Check if all pixels are black (zero)
    if np.all(gray_image == 0):
        return True
    else:
        return False


# Example usage:
image_path = "train/arrest/Arrest002/Arrest002_x264_110.png"
if is_image_all_black(image_path):
    print("The image contains only black pixels.")
else:
    print("The image contains pixels other than black.")
