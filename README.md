# Online Cooperative App for SMEs – Machine Learning Segmentation

A data-driven app that helps cooperatives segment users based on transaction behavior using K-Means clustering. Built using Python, SQLite, and Streamlit.

## 📦 Features
- Simulated cooperative user and transaction data
- K-Means clustering for user segmentation
- Interactive Streamlit dashboard
- Clean ERD and real database implementation

  <img width="1366" height="2693" alt="screencapture-koperasi-ml-jh5b4pfhzudcjsrbxkrb7p-streamlit-app-2025-08-15-11_22_28" src="https://github.com/user-attachments/assets/b5fa8027-7a0b-4a82-bce4-3e5f4927fcfd" />


## 📁 Structure
- `generate_data.py`: Create and populate SQLite database with fake data
- `clustered_users.csv`: Output with cluster labels
- `streamlit_app.py`: Streamlit dashboard
- `schema.sql`: Database schema
- `elbow_plot.png`: Plot used to determine optimal number of clusters

## 🛠 Tech Stack
- Python, Pandas, Scikit-learn, Faker
- SQLite
- Streamlit
https://koperasi-ml-jh5b4pfhzudcjsrbxkrb7p.streamlit.app/

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run dashboard/streamlit_app.py

