import cv2
import numpy as np

def subtract_background(image_path, lower_color, upper_color):

    # Read the image
    image = cv2.imread(image_path)

    # Check image
    if image is None:
        print("Image not found!")
        return

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color range
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract foreground
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Subtracted Image", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Image path
image_path = r"C:\Users\SUPRAJA\OneDrive\Pictures\Screenshots\Screenshot 2026-07-21 112953.png"

lower_color = [30, 30, 30]
upper_color = [255, 255, 255]

subtract_background(image_path, lower_color, upper_color)
