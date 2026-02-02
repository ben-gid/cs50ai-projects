import tensorflow as tf
from fastai.vision.all import *
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from pathlib import Path
import numpy as np

from traffic2 import load_data


import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# ----------------------------
# 1. Load Your Models
# ----------------------------

# TensorFlow / Keras models
tf_model1 = tf.keras.models.load_model("traffic_model.h5")
tf_model2 = tf.keras.models.load_model("traffic2_model.h5")

# fastai model (exports as a .pkl)
fastai_learner = load_learner("traffic3_model.pkl")


# ----------------------------
# 2. Load Test Images + Labels
# ----------------------------

test_path = Path("gtsrb")
classes = sorted([d.name for d in test_path.iterdir() if d.is_dir()])

image_files = get_image_files(test_path)

def preprocess_tf(img_path, img_size):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=img_size)
    arr = tf.keras.preprocessing.image.img_to_array(img)
    arr = arr / 255.0
    return np.expand_dims(arr, axis=0)

# fastai handles preprocessing internally via learner.dls
def preprocess_fastai(img_path):
    return PILImage.create(img_path)

y_true = [f.parent.name for f in image_files]


# ----------------------------
# 3. Run Predictions
# ----------------------------

def predict_tf(model, img_path):
    img = preprocess_tf(img_path, (224, 224))
    preds = model.predict(img)[0]
    return classes[np.argmax(preds)]

def predict_fastai(learner, img_path):
    pred_class, pred_idx, _ = learner.predict(preprocess_fastai(img_path))
    return str(pred_class)

tf1_preds = [predict_tf(tf_model1, f) for f in image_files]
tf2_preds = [predict_tf(tf_model2, f) for f in image_files]
fastai_preds = [predict_fastai(fastai_learner, f) for f in image_files]


# ----------------------------
# 4. Compute Metrics
# ----------------------------

def evaluate(name, preds):
    print(f"\n===== {name} =====")
    print("Accuracy:", accuracy_score(y_true, preds))
    print("Classification Report:\n", classification_report(y_true, preds))
    print("Confusion Matrix:\n", confusion_matrix(y_true, preds))

evaluate("TensorFlow Model 1", tf1_preds)
evaluate("TensorFlow Model 2", tf2_preds)
evaluate("fastai Model", fastai_preds)
