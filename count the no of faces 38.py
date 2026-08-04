import cv2

def count_faces(image_path):

    # Load the image
    image = cv2.imread(image_path)

    # Check if image loaded
    if image is None:
        print("Image not found! Check the image path.")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Count faces
    face_count = len(faces)

    print("Number of faces detected:", face_count)

    # Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display result
    cv2.imshow("Face Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return face_count


# Give your image path here
image_path = r"C:\Users\SUPRAJA\OneDrive\Pictures\Screenshots\Screenshot 2026-08-03 113904.png"

count_faces(image_path)
