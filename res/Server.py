from flask import Flask, request, jsonify
import pandas as pd
from joblib import load
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model
model = load('model.jb')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    year = data.get('year')
    actor1 = data.get('actor1')
    actor2 = data.get('actor2')
    duration = data.get('duration')
    genre = data.get('genre')
    votes = data.get('votes')
    director = data.get('director')

    # Create DataFrame for the input
    new_movie = pd.DataFrame({
        'Year': [year],
        'Actor 1': [actor1],
        'Actor 2': [actor2],
        'Duration': [duration],
        'Genre': [genre],
        'Votes': [votes],
        'Director': [director]
    })

    # Predict rating
    predicted_rating = model.predict(new_movie)
    return jsonify({'predicted_rating': round(predicted_rating[0], 2)})

if __name__ == '__main__':
    app.run(debug=True)
