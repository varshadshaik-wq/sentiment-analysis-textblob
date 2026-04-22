# 😊 Sentiment Analysis Web App (Flask)

A simple **Flask-based web application** that analyzes user input text and predicts whether the sentiment is **Positive, Negative, or Neutral** using **TextBlob (NLP)**.

---

## 🚀 Features

* 🧠 Sentiment analysis using Natural Language Processing
* 😊 Detects Positive, Negative, and Neutral sentiments
* 📊 Displays polarity and subjectivity scores
* 🌐 Interactive web interface using Flask
* ⚡ Real-time text analysis

---

## 🛠️ Technologies Used

* Python
* Flask
* TextBlob
* HTML (for frontend templates)

---

## 📂 Project Structure

```id="pl4h9f"
sentiment-analysis-flask-app/
│── app.py
│── templates/
│     └── index.html
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```id="7c9kq1"
git clone https://github.com/your-username/sentiment-analysis-flask-app.git
```

### 2. Navigate to Project Folder

```id="w2a9bz"
cd sentiment-analysis-flask-app
```

### 3. Install Dependencies

```id="s98b1v"
pip install flask textblob
```

### 4. Download TextBlob Corpora

```id="2vcllb"
python -m textblob.download_corpora
```

---

## ▶️ How to Run

```id="9v5k2g"
python app.py
```

Open your browser and go to:

```id="gklx1o"
http://127.0.0.1:5000/
```

---

## 💻 How It Works

* User enters text in the web form
* Text is processed using **TextBlob**
* The model calculates:

  * **Polarity** → (-1 to +1)
  * **Subjectivity** → (0 to 1)
* Sentiment is classified as:

  * Positive 😊
  * Negative 😞
  * Neutral 😐

---

## 📊 Example

```id="cwx3l7"
Input: "I love this product!"
Output: Positive 😊
Polarity: 0.5
Subjectivity: 0.6
```

---

## 📈 Future Improvements

* Add advanced NLP models (like BERT)
* Improve UI with CSS/Bootstrap
* Deploy on cloud (Render/Heroku)
* Add support for multiple languages

---


