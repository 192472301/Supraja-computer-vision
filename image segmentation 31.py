import cv2

def segment_image(image_path, threshold_value=127):

    # Read image in grayscale
    image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    # Check whether image is loaded
    if image is None:
        print("Image not found! Check the image path.")
        return

    # Apply thresholding
    _, segmented_image = cv2.threshold(
        image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# GIVE YOUR IMAGE PATH HERE
segment_image(
    r"C:\Users\SUPRAJA\OneDrive\Pictures\Screenshots\Screenshot 2026-07-21 112953.png",
    127
)
