

import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="Skewness & Kurtosis",
    page_icon="📊",
    layout="wide"
)


st.title('Normal Dağılım Görselleştirme')

col1, col2 = st.columns([1, 1])

with col1:
    # Slider ile kullanıcıdan veri girişi alalım
    mean = st.slider('Ortalama (Mean):', 0.0, 1000.0, 0.0)
    std_dev = st.slider('Standart Sapma (Standard Deviation):', 0.1, 1000.0, 1.0)
    sample_size = st.slider('Örnek Boyutu (Sample Size):', 10, 10000, 100)

    # Normal dağılımı oluşturalım
    normal_ondalik_dizi = np.random.normal(mean, std_dev, sample_size)
    normal_tamsayi_dizi = np.round(normal_ondalik_dizi).astype(int)
    median = np.median(normal_ondalik_dizi)


    fig, ax = plt.subplots()
    plt.title("Normal Dağılım Grafiği")  # Başlık ekle
    plt.xlabel("Değer")  # X ekseni etiketi ekle
    plt.ylabel("Frekans")  # Y ekseni etiketi ekle
    # Eksen aralıklarını belirle
    plt.xlim(-3000, 3000)  # X ekseni aralığı
    plt.ylim(0, 600)  # Y ekseni aralığı
    sns.set(style="whitegrid")  # Stil ayarla
    sns.histplot(normal_tamsayi_dizi, kde=True)  # Histogram ve KDE çiz
    for i in range(-3, 4):
        plt.axvline(x=mean + i * std_dev, color='r', linestyle='--')  # Standart sapma çizgilerini çiz
    st.pyplot(fig)


with col2:
    st.header("Skewness and Kurtosis")
    st.subheader("Skewness")
    skewness = (3 * (mean - median)) / std_dev
    st.subheader(skewness)
    st.divider()
    st.subheader('Kurtosis')
    kurtosis = (1 / sample_size) * sum(((normal_tamsayi_dizi - mean) / std_dev) ** 4) - 3
    st.subheader(kurtosis)
    st.divider()
    st.image("/skewness_vis.png")
