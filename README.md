# 🧠 Sign Language Recognition using CNN, Mediapipe & Tkinter ✋📷

A real-time sign language recognition system that uses your webcam to recognize hand gestures representing alphabets (A–Z), built using:
- **Mediapipe** for hand landmark detection  
- **TensorFlow/Keras** for gesture classification  
- **Tkinter** for a simple live GUI interface

---

## 🚀 Features

✅ Real-time gesture detection via webcam  
✅ Predicts alphabets A to Z  
✅ Simple and clean GUI interface using Tkinter  
✅ Easily extendable to form words or full sentences  
✅ Trained using Mediapipe hand landmark data  

---

## 🧠 Model

- Uses 21 hand landmarks (x, y, z) extracted from Mediapipe.  
- Trained using a **TensorFlow Keras Sequential model**.  
- Final model is saved in `.keras` format and loaded in the GUI for live predictions.

---

## 🔮 Future Upgrades

- 🔤 Construct full words/sentences from continuous letter prediction  
- 🧩 Add word-level gesture classification  
- 🌐 Create a web app using Streamlit or Flask  
- 📊 Integrate confidence scores and improve error handling  

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Snehaagraw/sign-language-recognition.git
cd sign-language-recognition
```
### 2. Create & Activate Virtual Environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
