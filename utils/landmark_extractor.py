import cv2
import mediapipe as mp
import numpy as np
import csv
import os

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Folder to store data
DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

# Ask for the label of the sign (like 'A', 'B', etc.)
label = input("Enter the sign label you want to collect data for (e.g., A, B, C): ").upper()
file_path = os.path.join(DATA_DIR, 'asl_data.csv')

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Unable to access the camera.")
    exit()

print(f"\n✅ Ready to collect 15 samples for '{label}'...")
print("➡ Press 's' to save the sample | Press 'q' to quit.\n")

count = 0
landmarks = []

with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        # 🔍 DIP Part: Convert BGR to RGB for MediaPipe processing
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # 🔄 Convert back to BGR for OpenCV display
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        current_landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract hand landmarks as a flat list
                hand = []
                for lm in hand_landmarks.landmark:
                    hand.extend([lm.x, lm.y, lm.z])
                current_landmarks = hand  # Store only one set for simplicity

        # 🖼️ Show webcam window
        cv2.imshow("Sign Language Data Collector", image)

        key = cv2.waitKey(1)

        if key == ord('s') and current_landmarks:
            with open(file_path, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([label] + current_landmarks)
            count += 1
            print(f"✅ Sample {count}/15 for '{label}' saved.")
            if count >= 15:
                break

        elif key == ord('q'):
            print("👋 Quitting data collection.")
            break

cap.release()
cv2.destroyAllWindows()
print("\n🎉 Data collection completed!")
