# webcam+hand tracking
import cv2
import mediapipe as mp

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils

hands=mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

cap=cv2.VideoCapture(0) #open webcam

while True:
    success,frame=cap.read() #read frame from webcam
    if not success:
        break

    frame=cv2.flip(frame,1) # Flip the frame for natural movement
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert BGR to RGB for Mediapipe
    results = hands.process(rgb_frame) # Process the frame and detect hands

    # If hands detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the frame
    cv2.imshow("Hand Detection!", frame)

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()