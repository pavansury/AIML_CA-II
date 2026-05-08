# Movie Recommender System

A simple Content-Based Recommender System using Flask and Machine Learning.

**Subject:** Advanced Machine Learning (BTAIC602)

## Features
- ✅ Search movie name
- ✅ Recommend similar movies
- ✅ Content-Based Filtering
- ✅ TF-IDF + Cosine Similarity
- ✅ Simple Web Interface
- ✅ Deployable on Render

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Flask
- HTML/CSS
- Render (Deployment)

## Project Structure
```
movie-recommender-system/
│
├── app.py
├── recommender.py
├── requirements.txt
├── render.yaml
├── README.md
├── .gitignore
│
├── dataset/
│   └── movies.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── model/
    └── similarity.pkl (generated on first run)
```

## Installation & Local Run

### Prerequisites
- Python 3.8+
- pip

### Steps

1. Clone the repository:
```bash
git clone <YOUR_GITHUB_REPO_LINK>
cd movie-recommender-system
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open in your browser:
```
http://127.0.0.1:5000
```

## How It Works

1. **Load Dataset:** Movies are loaded from `dataset/movies.csv` with title and genre information.
2. **TF-IDF Vectorization:** Genre descriptions are converted into numerical vectors using TF-IDF.
3. **Cosine Similarity:** Similarity scores between movies are calculated using cosine similarity.
4. **Recommendations:** When a user searches for a movie, the system returns the top 5 most similar movies.

## Example Usage

1. Enter a movie name (e.g., "Avengers")
2. Click "Recommend"
3. View similar movies based on genre

## Deploy on Render

### Step 1: Create GitHub Repository
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_LINK>
git push -u origin main
```

### Step 2: Connect to Render
1. Go to [Render.com](https://render.com)
2. Sign up/Log in with GitHub
3. New Web Service
4. Connect your GitHub repository
5. Select the repository
6. Deploy settings will auto-detect from `render.yaml`
7. Click "Deploy"

## Future Improvements
- [ ] Add poster images
- [ ] Add user login/authentication
- [ ] Use large movie dataset (TMDB/IMDb)
- [ ] Add collaborative filtering
- [ ] Deploy ML model separately
- [ ] Add Streamlit version
- [ ] Add user ratings and feedback
- [ ] Implement advanced NLP techniques
- [ ] Add movie search API integration

## License
MIT License

## Author
Created for Advanced Machine Learning (BTAIC602) Course