import numpy as np
from traffic import load_data, IMG_WIDTH, IMG_HEIGHT, NUM_CATEGORIES
import tensorflow as tf
from fastai.vision.all import load_learner, PILImage
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ----------------------------
# 1. Load test data
# ----------------------------
test_dir = "gtsrb"  # path to test images folder
images, labels = load_data(test_dir)
labels_cat = tf.keras.utils.to_categorical(labels)  # for TensorFlow models

x_test = np.array(images)
y_true = labels

print(f"Loaded {len(x_test)} test images.")

# ----------------------------
# 2. Load models
# ----------------------------

# TensorFlow models
tf_model1 = tf.keras.models.load_model("traffic_model.h5")
tf_model2 = tf.keras.models.load_model("traffic2_model.h5")

# fastai model
fastai_learner = load_learner("fastai_model.pkl")

# ----------------------------
# 3. Prediction helpers
# ----------------------------

# TensorFlow prediction
def predict_tf(model, x):
    preds = model.predict(x, verbose=0)
    return np.argmax(preds, axis=1)

# fastai prediction
def predict_fastai(learner, images):
    preds = []
    for img_arr in images:
        # convert numpy array back to PILImage
        img = PILImage.create(np.uint8(img_arr))
        pred_class, _, _ = learner.predict(img)
        preds.append(int(pred_class))
    return preds

# ----------------------------
# 4. Run predictions
# ----------------------------

tf1_preds = predict_tf(tf_model1, x_test)
tf2_preds = predict_tf(tf_model2, x_test)
fastai_preds = predict_fastai(fastai_learner, x_test)

# ----------------------------
# 5. Evaluate models
# ----------------------------
def evaluate(name, y_true, y_pred):
    print(f"\n===== {name} =====")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))

evaluate("TensorFlow Model 1", y_true, tf1_preds)
evaluate("TensorFlow Model 2", y_true, tf2_preds)
evaluate("fastai Model", y_true, fastai_preds)
