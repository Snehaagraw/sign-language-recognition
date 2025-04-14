import os
import cv2
import mediapipe as mp
import pandas as pd

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Path to your dataset (update if needed)
dataset_path = "data"  # Ensure 'train' folder is in the same directory
output_csv = "asl_data.csv"

# Setup hands module
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)

# Store all landmarks here
data = []
labels = []

for label in os.listdir(dataset_path):
    label_folder = os.path.join(dataset_path, label)

    if not os.path.isdir(label_folder):
        continue  # Skip non-folder files

    print(f"Processing label: {label}")

    for image_name in os.listdir(label_folder):
        image_path = os.path.join(label_folder, image_name)
        image = cv2.imread(image_path)

        if image is None:
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            landmarks = []
            for hand_landmarks in results.multi_hand_landmarks:
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])
                break  # Only one hand
            data.append(landmarks)
            labels.append(label)

hands.close()

# Create DataFrame
columns = [f'x{i}' for i in range(21)] + [f'y{i}' for i in range(21)] + [f'z{i}' for i in range(21)]
df = pd.DataFrame(data, columns=columns)
df['label'] = labels

# Save to CSV
df.to_csv(output_csv, index=False)
print(f"CSV file saved as {output_csv}")
