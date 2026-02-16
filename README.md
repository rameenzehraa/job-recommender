# 🎯 Job Recommendation System

An ML-powered application that recommends relevant job roles based on user skills and interests using Natural Language Processing.

**Built by:** Rameen Zehra

---

## 📋 Overview

This system uses **TF-IDF vectorization** and **cosine similarity** to match user input with job descriptions from a curated dataset of 50+ tech roles. Users enter their skills (e.g., "python machine learning") and receive the top 3 most relevant job recommendations.

---

## 🛠 Tech Stack

- **Python** - Core programming language
- **pandas** - Data manipulation and CSV handling
- **scikit-learn** - TF-IDF vectorization and cosine similarity
- **Streamlit** - Interactive web interface

---

## 🧠 How It Works

1. **Data Loading:** Reads job titles and descriptions from CSV
2. **Text Preprocessing:** Combines job title + description into unified text
3. **Vectorization:** Converts text to numerical vectors using TF-IDF
4. **Similarity Matching:** Compares user input with all jobs using cosine similarity
5. **Ranking:** Returns top 3 jobs with highest similarity scores

**ML Pipeline:**
```
User Input → TF-IDF Transform → Cosine Similarity → Top 3 Recommendations
```

---

## 📦 Installation & Setup

**Prerequisites:** Python 3.8+

**Steps:**

1. Clone the repository
```bash
git clone <your-repo-url>
cd job-recommender
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💡 Usage

1. Enter your skills or interests in the text box (e.g., "python data analysis", "react frontend", "machine learning")
2. Click "Recommend Jobs"
3. View your top 3 job matches ranked by relevance

---

## 📁 Project Structure
```
job-recommender/
├── data.csv              # Dataset of 50 job roles
├── recommender.py        # ML recommendation engine
├── app.py               # Streamlit UI
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

---

## 📊 Dataset

Custom-curated dataset of 50 technology job roles spanning:
- Data Science & Analytics
- Software Engineering
- Machine Learning & AI
- DevOps & Cloud
- Design & Product
- Cybersecurity

---

## 📄 License

This project is open source and available for educational purposes.

---

**Live Demo:** [View App](https://job-rs.streamlit.app/)

---