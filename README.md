# Movie Rating Predictor

A React web application that predicts movie ratings based on various details about the movie using a Python machine learning model. Flask is used for communication between the Python backend and the React app.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Backend Details](#backend-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Movie Rating Predictor is a web application built with React for the frontend and a Python machine learning model for the backend. It predicts the rating of a movie (from 0 to 10) based on details such as duration, actors' names, and director's name.

## Features

- **User-friendly Interface:** Simple interface to input movie details and predict ratings.
- **Real-time Predictions:** Quickly processes input to provide movie rating predictions.
- **Machine Learning:** Utilizes a trained machine learning model for accurate predictions.

## Installation

### Prerequisites

- Node.js
- Python 3.x
- pip (Python package installer)

### Frontend Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/LavKalsi/MovieRatingPredictor.git
    cd MovieRatingPredictor
    ```

2. Navigate to the `frontend` directory and install dependencies:
    ```sh
    cd frontend
    npm install
    ```

3. Start the React application:
    ```sh
    npm start
    ```

### Backend Setup

1. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the required Python packages:
    ```sh
    pip install -r res/requirements.txt
    ```

3. Run the backend server:
    ```sh
    python res/Server.py
    ```

## Usage

1. Ensure both the frontend and backend servers are running.
2. Open your browser and navigate to `http://localhost:3000`.
3. Enter the movie details (such as duration, actors' names, and director's name).
4. Click the "Predict" button to receive the rating prediction.

## How It Works

The Movie Rating Predictor web app allows users to predict the rating of a movie. Here's how you can use it:

1. **Input Details:** Users can input movie details such as duration, actors' names, and director's name into the provided fields on the web app.
2. **Submit for Prediction:** After entering the details, users click the "Predict" button to submit the information for analysis.
3. **Backend Processing:** The frontend sends the movie details to the backend Python server, where the machine learning model processes them.
4. **Receive Results:** The backend returns the prediction result (movie rating from 0 to 10) to the frontend, which is then displayed to the user.

## Backend Details

The backend is a Python Flask application that serves a machine learning model trained to predict movie ratings. The backend files, including the model and Flask app, are located in the `res` folder.

### Files in `res` Folder

- `Server.py`: The Flask application that handles HTTP requests from the frontend.
- `model.pkl`: The trained machine learning model.
- `requirements.txt`: The dependencies required for the Python backend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

LavKalsi - [GitHub](https://github.com/LavKalsi)

Feel free to contact me if you have any questions or suggestions!
