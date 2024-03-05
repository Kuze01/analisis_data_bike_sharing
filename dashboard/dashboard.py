import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

url = "https://raw.githubusercontent.com/Kuze01/analisis_data_bike_sharing/main/dashboard/main_data.csv"
bike_share = pd.read_csv(url)

# Filter data untuk 4 musim
seasonal_data = bike_share.groupby('season_x')['cnt_x'].mean().loc[[1, 2, 3, 4]]
season_names = ['Spring', 'Summer', 'Fall', 'Winter']

st.header('Bike Sharing Data Visualization :bike:')

# Membuat bar chart
st.subheader("Seasonal Data Visualization")
fig_seasonal = plt.figure()
plt.bar(season_names, seasonal_data)
plt.xlabel('Season')
plt.ylabel('Daily Bike Rentals')
st.pyplot(fig_seasonal)

# Membuat line chart
st.subheader("Monthly Data Visualization")
sns.set_style("whitegrid")
fig_monthly = plt.figure(figsize=(10, 6))
sns.lineplot(x="mnth_x", y="cnt_x", data=bike_share, ci=None)
plt.xlabel("Month")
plt.ylabel("Daily Bike Rentals")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
st.pyplot(fig_monthly)