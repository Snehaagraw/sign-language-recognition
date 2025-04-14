import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import tkinter as tk
from PIL import Image, ImageTk

# Load model
model = load_model("models/sign_model.keras")

# List of class labels (A–Z)
labels = [chr(i) for i in range(65, 91)]

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# GUI setup
window = tk.Tk()
window.title("Sign Language Recognition")

label = tk.Label(window, text="", font=("Arial", 24))
label.pack()

canvas = tk.Label(window)
canvas.pack()

cap = cv2.VideoCapture(0)

def detect():
    ret, frame = cap.read()
    if not ret:
        return

    img = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    prediction = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            landmarks = np.array(landmarks).reshape(1, -1)

            # Predict
            probs = model.predict(landmarks)[0]
            prediction = labels[np.argmax(probs)]

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    label.config(text=f"Detected: {prediction}")
    img = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
    canvas.imgtk = img
    canvas.configure(image=img)
    canvas.after(10, detect)

# Close the window when any key is pressed (specifically 'q' key)
def close_on_key(event):
    if event.char == 'q':
        cap.release()
        window.quit()

# Bind key press event to close the window on 'q' key
window.bind("<KeyPress>", close_on_key)

detect()
window.mainloop()
