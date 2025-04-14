# 🧠 Sign Language Recognition using CNN, Mediapipe & Tkinter ✋📷

A real-time sign language recognition system that uses a webcam to recognize hand gestures representing alphabets (A–Z), built using:
- **Mediapipe** for hand landmark detection
- **TensorFlow/Keras** for gesture classification
- **Tkinter GUI** for a simple live interface


## 🚀 Features

✅ Real-time gesture detection via webcam  
✅ Predicts alphabets A to Z  
✅ Simple GUI interface using Tkinter  
✅ Easily extendable to form words/sentences  
✅ Trained using Mediapipe hand landmarks  

##🧠 Model
-Uses hand landmarks (x, y, z) from Mediapipe.

-Trained using TensorFlow Keras Sequential model.

-Saves model in .keras format for GUI use.

##🚀 Future Upgrades
-Word/Sentence construction from alphabet stream

-Word-level gesture classification

-Web app using Streamlit or Flask

-Confidence scoring & error handling

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
