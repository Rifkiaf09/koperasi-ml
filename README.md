# Online Cooperative App for SMEs – Machine Learning Segmentation

A data-driven app that helps cooperatives segment users based on transaction behavior using K-Means clustering. Built using Python, SQLite, and Streamlit.

## 📦 Features
- Simulated cooperative user and transaction data
- K-Means clustering for user segmentation
- Interactive Streamlit dashboard
- Clean ERD and real database implementation

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

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run dashboard/streamlit_app.py
