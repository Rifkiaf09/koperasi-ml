import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load clustered data
data_ml = pd.read_csv("clustered_users.csv")

st.set_page_config(page_title="Dashboard Koperasi", layout="wide")
st.title("📊 Dashboard Segmentasi Pengguna Koperasi")

# Sidebar filter
selected_cluster = st.sidebar.selectbox("Pilih Cluster", sorted(data_ml['cluster'].unique()))
filtered_data = data_ml[data_ml['cluster'] == selected_cluster]

st.markdown(f"### 📌 Statistik Cluster {selected_cluster}")
st.write(filtered_data.describe())

# Visualisasi distribusi pendapatan
st.markdown("### 💰 Distribusi Pendapatan per Cluster")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_data['pendapatan'], kde=True, bins=20, ax=ax1)
st.pyplot(fig1)

# Visualisasi scatter antara pendapatan dan total transaksi
st.markdown("### 🔄 Scatter Plot: Pendapatan vs Total Transaksi")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_data, x='pendapatan', y='total_transaksi', hue='cluster', palette='Set2', ax=ax2)
st.pyplot(fig2)

# Visualisasi rata-rata semua cluster
st.markdown("### 📈 Rata-rata Fitur per Cluster")
cluster_means = data_ml.groupby('cluster')[['pendapatan', 'total_transaksi', 'frekuensi', 'rata_rata_transaksi']].mean()
st.dataframe(cluster_means.style.highlight_max(axis=0))

st.markdown("---")
st.caption("Created with ❤️ by Rifki - Online Cooperative App for SMEs")
