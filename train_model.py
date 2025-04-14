import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
import os

# Load data
data = pd.read_csv('asl_data.csv')  # make sure this file has 'label' and features

# Features and labels
X = data.drop('label', axis=1).values
y = pd.get_dummies(data['label']).values  # one-hot encoding

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Save best model
os.makedirs("models", exist_ok=True)
checkpoint = ModelCheckpoint('models/sign_model.keras', monitor='val_accuracy', save_best_only=True)

# Train
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=25, callbacks=[checkpoint])

print("✅ Model trained and saved as models/sign_model.keras")
