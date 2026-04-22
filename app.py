from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    user_text = ""

    if request.method == 'POST':
        user_text = request.form['text']
        if user_text.strip():
            blob = TextBlob(user_text)
            polarity = blob.sentiment.polarity   # -1 (negative) to +1 (positive)
            subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
            if polarity > 0:
                sentiment = "Positive 😊"
            elif polarity < 0:
                sentiment = "Negative 😞"
            else:
                sentiment = "Neutral 😐"

    return render_template('index.html',
                           user_text=user_text,
                           sentiment=sentiment,
                           polarity=polarity,
                           subjectivity=subjectivity)

if __name__ == '__main__':
    app.run(debug=True)