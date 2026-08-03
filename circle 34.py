import numpy as np
import cv2

def create_circle_image(image_size):

    height, width = image_size

    # Create a white image
    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    # Define circle properties
    center = (width // 2, height // 2)

    # Radius is 1/4 of smallest dimension
    radius = min(width, height) // 4

    # Draw red circle
    cv2.circle(
        image,
        center,
        radius,
        (0, 0, 255),
        2
    )

    # Display image
    cv2.imshow("Circle Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get input from user
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))

create_circle_image((user_height, user_width))
