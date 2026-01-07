# 🌸 Dockerized Iris Flower Classification

A beginner-friendly machine learning project that demonstrates **classification using the Iris dataset** and **deployment of an ML model using Docker and Flask**.
The application provides a simple **web interface** where users can input flower measurements and get real-time predictions.

---

## 🚀 Project Overview

This project focuses on the **end-to-end ML workflow**:

* Training a supervised classification model
* Saving the trained model
* Serving predictions through a Flask web app
* Containerizing the entire application using Docker

The goal is to showcase **basic ML + Docker deployment skills** in a practical and easy-to-understand way.

---

## 🧠 Machine Learning Details

* **Dataset**: Iris Flower Dataset
* **Problem Type**: Multiclass Classification
* **Classes**:

  * Setosa
  * Versicolor
  * Virginica
* **Algorithm Used**: Random Forest Classifier
* **Features**:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* Flask
* NumPy
* Docker

---

## 📂 Project Structure

```
docker-iris-classifier/
│
├── app.py              # Flask application with prediction routes
├── train_model.py      # Script to train and save ML model
├── model.pkl           # Trained ML model
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
└── README.md           # Project documentation
```

---

## ⚙️ How It Works

1. The ML model is trained using the Iris dataset.
2. The trained model is saved as a `.pkl` file.
3. Flask loads the model and exposes a web interface.
4. Users enter flower measurements in the browser.
5. The model predicts the Iris species in real time.
6. Docker packages the entire application into a container.

---

## 🐳 Run the Project Using Docker

### 1️⃣ Build Docker Image

```bash
docker build -t docker-iris-classifier .
```

### 2️⃣ Run Docker Container

```bash
docker run -p 5000:5000 docker-iris-classifier
```

### 3️⃣ Open in Browser

```
http://localhost:5000
```

---

## 🖥️ Web Interface

* Enter flower measurements
* Click **Predict**
* Instantly see the predicted Iris species

No Postman or API tools required.

---

## 📌 Example Input

| Feature      | Value |
| ------------ | ----- |
| Sepal Length | 5.1   |
| Sepal Width  | 3.5   |
| Petal Length | 1.4   |
| Petal Width  | 0.2   |

**Prediction Output**: `Setosa`

---

## 🎯 What This Project Demonstrates

* Understanding of supervised ML classification
* Model training and serialization
* Flask backend development
* Docker containerization
* Deployment-ready ML application
* Beginner-level MLOps concepts

---

## 📝 Resume Description

> Built a supervised machine learning model using the Iris dataset and deployed it as a Dockerized Flask web application with a user-friendly prediction interface.

---

## 📈 Future Enhancements

* Add model accuracy and evaluation metrics
* Show prediction probabilities
* Improve UI using Bootstrap
* Deploy on AWS EC2
* Add Docker Compose

---

## 🤝 Acknowledgements

* Iris Dataset from scikit-learn
* Flask & Docker open-source communities

---

## 📬 Author

**Deep Shrivastav**
M.Sc. Data Science & AI
Beginner-friendly ML & Docker project for learning and demonstration


