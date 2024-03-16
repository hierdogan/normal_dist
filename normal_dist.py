import streamlit as st
import numpy as np
import plotly.figure_factory as ff

st.title('Normal Dağılım Görselleştirme')

# Slider ile kullanıcıdan veri girişi alalım
mean = st.slider('Ortalama (Mean):', -10.0, 10.0, 0.0)
std_dev = st.slider('Standart Sapma (Standard Deviation):', 0.1, 10.0, 1.0)
sample_size = st.slider('Örnek Boyutu (Sample Size):', 10, 1000, 100)

# Normal dağılımı oluşturalım
data = np.random.normal(loc=mean, scale=std_dev, size=sample_size)

# Plotly ile histogram oluşturalım
fig = ff.create_distplot([data], ['Normal Dağılım'], show_hist=False)
fig.update_layout(title='Normal Dağılım', xaxis_title='Değer', yaxis_title='Yoğunluk')

# Streamlit ile grafiği gösterelim
st.plotly_chart(fig)
