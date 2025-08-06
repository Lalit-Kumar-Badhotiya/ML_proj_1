
import cv2
import numpy as np

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the dog nose and ears images with transparency
dog_nose = cv2.imread(r'C:\Users\lalit\OpenCV proj\dog_nose.png', cv2.IMREAD_UNCHANGED)
dog_ears = cv2.imread(r'C:\Users\lalit\OpenCV proj\dog_ears.png', cv2.IMREAD_UNCHANGED)


def overlay_image(background, overlay, x, y):
    h, w = overlay.shape[:2]
    if overlay.shape[2] == 4:  # If overlay has an alpha channel
        for i in range(h):
            for j in range(w):
                if y + i >= background.shape[0] or x + j >= background.shape[1]:
                    continue
                alpha = overlay[i, j][3] / 255.0
                background[y + i, x + j] = (1 - alpha) * background[y + i, x + j] + alpha * overlay[i, j][:3]
    else:  # If overlay has no alpha channel, just paste it
        for i in range(h):
            for j in range(w):
                if y + i >= background.shape[0] or x + j >= background.shape[1]:
                    continue
                background[y + i, x + j] = overlay[i, j]

# Start webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Overlay nose at the center-bottom of face
        nose_x = x + w // 2 - dog_nose.shape[1] // 2
        nose_y = y + int(h * 0.7) - dog_nose.shape[0] // 2

        # Overlay ears above the face
        ear_x = x + w // 2 - dog_ears.shape[1] // 2
        ear_y = y - dog_ears.shape[0] // 2

        overlay_image(frame, dog_nose, nose_x, nose_y)
        overlay_image(frame, dog_ears, ear_x, ear_y)

    cv2.imshow('Dog Filter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
