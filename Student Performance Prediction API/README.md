# Student Performance Prediction API

## 📌 Project Overview

This project is a Machine Learning REST API built using Flask. It predicts whether a student is likely to **Pass** or **Fail** based on various academic and personal factors.

The model was trained using a Random Forest Classifier on the Student Performance Factors dataset.

---

## 🚀 Features

* Predicts student performance
* REST API using Flask
* Machine Learning model using Scikit-learn
* Model serialization using Joblib
* Docker support
* Sample JSON request included

---

## 🛠 Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Docker

---

## 📁 Project Structure

```
student-performance-api/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── sample_request.json
├── StudentPerformanceFactors.csv
├── student_performance_model.ipynb
├── README.md
├── .gitignore
│
└── model/
    ├── student_model.pkl
    └── encoders.pkl
```

---

## ▶️ Run the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

## 🔗 API Endpoint

### POST /predict

Send a JSON request containing student information.

Example response:

```json
{
  "prediction": "Pass"
}
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t student-performance-api .
```

Run the container:

```bash
docker run -p 5000:5000 student-performance-api
```

---

## 👨‍💻 Author

**P. Shazin Faisal**
