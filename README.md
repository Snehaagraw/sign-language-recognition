# 🧠 Sign Language Recognition using CNN, Mediapipe & Tkinter ✋📷

A real-time sign language recognition system that uses a webcam to recognize hand gestures representing alphabets (A–Z), built using:
- **Mediapipe** for hand landmark detection
- **TensorFlow/Keras** for gesture classification
- **Tkinter GUI** for a simple live interface

## 📸 Demo

![demo](assets/demo.gif) <!-- Add a demo GIF or image here if available -->

## 📁 Project Structure

sign-language-recognition/ ├── gui.py # GUI application for real-time predictions ├── train.py # Training script for model ├── models/ │ └── sign_model.keras # Trained model saved in .keras format ├── datasets/ # Folder to store gesture data (optional to upload) ├── requirements.txt # List of all required Python packages ├── README.md # Project documentation └── .gitignore


## 🚀 Features

✅ Real-time gesture detection via webcam  
✅ Predicts alphabets A to Z  
✅ Simple GUI interface using Tkinter  
✅ Easily extendable to form words/sentences  
✅ Trained using Mediapipe hand landmarks  

## 🛠️ Installation & Setup

1. **Clone this repository:**
```bash
git clone https://github.com/Snehaagraw/sign-language-recognition.git
cd sign-language-recognition
python -m venv venv
venv\Scripts\activate       # On Windows
pip install -r requirements.txt
python gui.py

✋ Press Q or close the window to exit the GUI.

🏋️‍♀️ To Retrain the Model
python train.py

🧠 Model
-Uses hand landmarks (x, y, z) from Mediapipe.

-Trained using TensorFlow Keras Sequential model.

-Saves model in .keras format for GUI use.

🚀 Future Upgrades
-Word/Sentence construction from alphabet stream

-Word-level gesture classification

-Web app using Streamlit or Flask

-Confidence scoring & error handling

🙋‍♀️ Author
Krishanangi Agrawal