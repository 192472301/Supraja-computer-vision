import cv2
from tkinter import Tk, filedialog

# Hide tkinter main window
Tk().withdraw()

# Select video
video_path = filedialog.askopenfilename(
    title="Select Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

print("Selected video:", video_path)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video cannot be opened!")
else:
    print("Video opened successfully!")

    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Playing in reverse slow motion...")

    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
