import streamlit as st
import pandas as pd
import datetime
#from vega_lite.vega.v4.api import DateTimeUnit
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import date
from datetime import datetime, timedelta
#from vega_lite.altair import Chart

# Image URL
icon_url = "https://upload.wikimedia.org/wikipedia/commons/1/12/Logo_BMKG_%282010%29.png"
st.set_page_config(page_title="Pasut Briefing Maritim", page_icon=icon_url, layout="wide")

#st.set_page_config(layout="wide")

margins_css = """
<style>
  .appview-container .main .block-container {
    padding-top: 1rem;
  }
</style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

# Set the image as the header with a caption and custom width
#st.image(icon_url, width=150)
# Streamlit title and subtitle
#st.title('Tabel dan Grafik Pasang Surut')
#st.write("Briefing Pusat Meteorologi Maritim")

# Display the image and title
col1, col2 = st.columns([1, 12])
with col1:
    #st.image(icon_url , width=80)
    st.image(icon _url, width=80, style={"margin-top": "20px"})
with col2:
    st.title("Tabel dan Grafik Pasang Surut")
    st.write("Briefing Pusat Meteorologi Maritim")

col1, col2 = st.columns([1, 5])

# Load the csv of tide data
#main_table = pd.read_csv('/home/adit/#time_series/pasut_hidrosal/tabel_pasut_hidros_briefing.csv')
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
    #st.subheader("Content for Column 1")
    #st.write("This text appears in the first column.")
    # Choosing the start and end time interface
    locations = ['Jakarta', 'Semarang', 'Cilacap', 'Surabaya']
    selected_location = st.selectbox('Pilih lokasi:', locations)
    #start_date = st.date_input('Pilih tanggal awal', datetime.date(year=2024, month=6, day=14))  # Set default date (optional)
    today = date.today()  # Get today's date
    start_date = st.date_input('Pilih tanggal awal', today - timedelta(days=3))  # Set default date to today
    end_date = st.date_input('Pilih tanggal akhir', today + timedelta(days=3))  # Set default date (optional)
    # Display or use the selected date
    st.write("Lokasi:", selected_location)
    st.write("Tanggal awal:", start_date)
    st.write("Tanggal akhir:", end_date)

#start_datetime = pd.to_datetime('2024-06-11')
#end_datetime = pd.to_datetime('2024-06-14')

# Select the specified date and location
filtered_df = main_table.loc[start_date:end_date]
series_to_plot = filtered_df[selected_location]

# Convert index to 24-hour format (adjust format string if needed)
#series_to_plot.index = series_to_plot.index.strftime('%Y-%m-%d %H:%M:%S')

# Plot the dataframe with the modified index
#st.line_chart(df)


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
#name_mapping = {0: '00:00', 1: '01:00', 2: '02:00', 3: '03:00', 4: '04:00', 5: '05:00', 6: '06:00', 
#                7: '07:00', 8: '08:00', 9: '09:00', 10: '10:00', 11: '10:00', 12: '10:00',
#                13: '13:00', 14: '14:00', 15: '15:00', 16: '16:00', 17: '17:00', 18: '18:00',
#                19: '19:00', 20: '20:00', 21: '21:00', 22: '22:00', 23: '23:00' }

#df_tabel = df_tabel.rename(columns=name_mapping)
#df_tabel    
    




#series_to_plot.plot
#series_to_plot.plot(kind='line', style='o-')  # Adjust kind and style as needed
#series_to_plot.plot(kind='line')  # Adjust kind and style as needed
# App section title

#st.line_chart(series_to_plot, use_container_width=True, marker='circle')

#st.dataframe(series_to_plot)    
with col2:
    st.subheader('Pasang Surut '+selected_location)
    #st.write("This text appears in the second column.")
    #st.title('Pasang Surut '+selected_location)
    fig = st.line_chart(series_to_plot)

    st.dataframe(df_tabel)
    #st.dataframe(series_to_plot)
    
    # Chart title and configuration
    #title = 'Sample Interactive Line Chart'
    #fig = go.Figure(go.Scatter(x=series_to_plot['time'], y=series_to_plot['Jakarta']))
    #fig = go.Figure(go.Scatter(x=series_to_plot['waktu'], y=series_to_plot['Jakarta']))
    
    #fig.update_layout(title_text=title)

    # Display the chart with Streamlit
    #st.plotly_chart(fig)

    
    #fig, ax = plt.subplots()  # Create Matplotlib figure and axis

    #ax.plot(series_to_plot)  # Plot the line

    # Add horizontal grid lines (adjust y-axis limits as needed)
    #ax.grid(True, linestyle='--', linewidth=0.5, color='gray', which='both', axis='y')

    # Display the chart using st.pyplot
    #st.pyplot(fig)

    #st.line_chart(data, x="hour", y="value")
    #fig = st.line_chart(data, x="hour", y="value")

    # Access x-axis labels using fig.get_xticks()
    #xticks_list = fig.get_xticks().tolist()

    # Format labels as strings with leading zeros (00.00 - 23.00)
    #formatted_labels = [f"{int(label):02d}.00" for label in xticks_list]

    # Set the formatted labels back to the x-axis
    #fig.set_xticklabels(formatted_labels)

    # Access underlying chart elements
    #fig = st._current_widget.interactive_figure

    # Customize x-axis tick labels (assuming Matplotlib is used for plotting)
    #fig.get_axes()[0].set_xticks(range(24))  # Set tick positions for each hour
    #fig.get_axes()[0].set_xticklabels([f"{hour:02d}.00" for hour in range(24)])  # Format labels

    #chart = alt.Chart(series_to_plot).mark_line().encode(x=alt.X("date:T", title="Time", axis=alt.Axis(format=TimeUnitFormat.HOURS24))).properties(width=800, height=400)
    #st.altair_chart(chart)
    #fig = go.Figure()
    #fig.add_trace(go.Scatter(x=data["date"], y=data["value"], mode='lines+markers'))  # Line with markers
    #fig.add_trace(go.Scatter(series_to_plot, mode='lines+markers'))  # Line with markers
    
    #st.plotly_chart(fig)








