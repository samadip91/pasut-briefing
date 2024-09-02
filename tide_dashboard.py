import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go
from datetime import date
from datetime import datetime, timedelta

# Image URL
icon_url = "https://upload.wikimedia.org/wikipedia/commons/1/12/Logo_BMKG_%282010%29.png"
st.set_page_config(page_title="Pasut Briefing Maritim", page_icon=icon_url, layout="wide")

margins_css = """
<style>
  .appview-container .main .block-container {
    padding-top: 1rem;
  }
</style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

# Display the image and title
col1, col2 = st.columns([1, 12])
with col1:
    st.image(icon_url , width=80)
    #st.image(icon_url, width=80, style={"margin-top": "20px"})
with col2:
    st.title("Tabel dan Grafik Pasang Surut")
    st.write("Briefing Pusat Meteorologi Maritim")

col1, col2 = st.columns([1, 5])

# Load the csv of tide data
main_table = pd.read_csv('./tabel_pasut_hidros_briefing.csv')

# timestamping and indexing
start_time = pd.Timestamp("2024-01-01 01:00:00")  # Example starting datetime with hour
increment = pd.Timedelta(hours=1)  # Increment of 1 hour
end_time = pd.Timestamp("2025-01-01 00:00:00")
timestamps = pd.date_range(start_time, end_time, freq=increment)

main_table['time'] = timestamps
main_table['waktu'] = timestamps
main_table = main_table.set_index('time')

with col1:
    # Choosing the start and end time interface
    locations = ['Jakarta', 'Semarang', 'Cilacap', 'Surabaya']
    selected_location = st.selectbox('Pilih lokasi:', locations)
    today = date.today()  # Get today's date
    start_date = st.date_input('Pilih tanggal awal', today - timedelta(days=3))  # Set default date to today
    end_date = st.date_input('Pilih tanggal akhir', today + timedelta(days=3))  # Set default date (optional)

    # Display or use the selected date
    st.write("Lokasi:", selected_location)
    st.write("Tanggal awal:", start_date)
    st.write("Tanggal akhir:", end_date)

# Select the specified date and location
filtered_df = main_table.loc[start_date:end_date]
series_to_plot = filtered_df[selected_location]

# Assuming your dataframe is called 'df' and the index is datetime

waktu = [ '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',  '21',  '22',  '23', ]
df_tabel = pd.DataFrame()

for jam in waktu:
    jam = jam + ':00:00'
    df_filtered = series_to_plot[series_to_plot.index.strftime('%H:%M:%S') == jam]
    df_filtered = df_filtered.reset_index(drop=True)
    df_tabel = pd.concat([df_tabel, df_filtered], axis=1, ignore_index=True)

#df_tabel
increment = pd.Timedelta(days=1)  # Increment of 1 hour
timestamps = pd.date_range(start_date, end_date, freq='D')
#timestamps = pd.date_range(start_date, end_date, freq='', format='%d-%m-%Y')


df_tabel['tanggal_jam'] = timestamps
df_tabel = df_tabel.set_index('tanggal_jam')
df_tabel = df_tabel.round(1)

with col2:
    st.subheader('Pasang Surut '+selected_location)
    #st.write("This text appears in the second column.")
    #st.title('Pasang Surut '+selected_location)
    fig = st.line_chart(series_to_plot)

    st.dataframe(df_tabel)
