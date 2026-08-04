import cv2
import pytesseract

# Tesseract location
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video cannot be opened!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract text
        text = pytesseract.image_to_string(gray)

        if text.strip():
            print("Detected Text:")
            print(text)

        # Show video
        cv2.imshow("Text Extraction from Video", frame)

        # Press Q to stop
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


extract_text_from_video(
    r"C:\Users\SUPRAJA\Downloads\traffic video.mp4.mp4"
)
