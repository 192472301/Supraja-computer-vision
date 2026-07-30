import cv2

# Load the Haar Cascade XML file
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")

# Check if the cascade loaded successfully
if watch_cascade.empty():
    print("Error: watch_cascade.xml not found or could not be loaded.")
    exit()

# Read the image
image = cv2.imread("watch.jpg")

# Check if image is loaded
if image is None:
    print("Error: watch.jpg not found.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches
watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw bounding boxes around detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image
cv2.imshow("Detected Watch", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
