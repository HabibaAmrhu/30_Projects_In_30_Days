import streamlit as st
import numpy as np
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

st.title("MNIST Image Classifier")

@st.cache_resource
def load_and_train_model():
    (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
    train_images, test_images = train_images / 255.0, test_images / 255.0
    train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
    test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))
    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)

    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=2, batch_size=128, verbose=0)
    return model, test_images, test_labels

model, test_images, test_labels = load_and_train_model()

idx = st.slider("Select a test image index", 0, len(test_images)-1, 0)
image = test_images[idx].reshape(28, 28)
st.image(image, caption="Test Image", width=150)

if st.button("Predict"):
    pred = model.predict(test_images[idx].reshape(1,28,28,1))
    st.write(f"Predicted Label: {np.argmax(pred)}")
    st.write(f"True Label: {np.argmax(test_labels[idx])}")