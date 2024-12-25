import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "main_data.csv"

try:
    day_df = pd.read_csv(DATA_PATH)

    if {'season_day', 'registered_day', 'casual_day', 'weathersit_day', 'cnt_day'}.issubset(day_df.columns):
        st.title("Analisis Penggunaan Sepeda")

        st.sidebar.subheader("Filter Data")
        season_day_options = day_df['season_day'].dropna().unique()
        selected_season_day = st.sidebar.multiselect(
            "Pilih Musim:",
            options=season_day_options,
            default=season_day_options
        )
        filtered_df = day_df[day_df['season_day'].isin(selected_season_day)]
        st.subheader("Distribusi Musim")
        season_day_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        fig1, ax1 = plt.subplots(1, 2, figsize=(14, 6))

        sns.countplot(
            x='season_day',
            data=filtered_df,
            hue='season_day',
            palette=season_day_colors,
            legend=False,
            ax=ax1[0]
        )
        ax1[0].set_title('Distribusi Musim', fontsize=14, fontweight='bold')
        ax1[0].set_xlabel('Musim', fontsize=12)
        ax1[0].set_ylabel('Jumlah', fontsize=12)

        sns.barplot(
            x='season_day',
            y='registered_day',
            data=filtered_df,
            hue='season_day',
            label='Terdaftar',
            palette=season_day_colors,
            legend=False,
            ax=ax1[1],
            width=0.5,
            errorbar=None
        )
        sns.barplot(
            x='season_day',
            y='casual_day',
            data=filtered_df,
            hue='season_day',
            label='Kasual',
            palette=season_day_colors,
            legend=False,
            hatch='/',
            ax=ax1[1],
            width=0.5,
            errorbar=None
        )
        ax1[1].set_title('Korelasi Pengguna Terdaftar dan Kasual', fontsize=14, fontweight='bold')
        ax1[1].set_xlabel('Musim', fontsize=12)
        ax1[1].set_ylabel('Rata-rata Jumlah Penyewa', fontsize=12)
        ax1[1].legend(['Terdaftar', 'Kasual'], loc='upper left')
        plt.tight_layout()
        st.pyplot(fig1)

        st.subheader("Distribusi Kondisi Cuaca")
        weathersit_day_colors = ['tab:blue', 'tab:orange', 'tab:green']
        fig2, ax2 = plt.subplots(1, 2, figsize=(12, 7))

        sns.countplot(
            x='weathersit_day',
            data=filtered_df,
            hue='weathersit_day',
            ax=ax2[0], 
            palette=weathersit_day_colors,
            width=0.5
        )
        ax2[0].set_title('Distribusi Kondisi Cuaca', fontsize=14, fontweight='bold')
        ax2[0].set_xlabel('Kondisi Cuaca', fontsize=12, fontweight='medium')
        ax2[0].set_ylabel('Jumlah', fontsize=12, fontweight='medium')

        sns.barplot(
            x='weathersit_day',
            y='registered_day',
            data=filtered_df,
            label='Pengguna Terdaftar',
            color='tab:blue',
            ax=ax2[1],
            width=0.5,
            errorbar=None
        )
        sns.barplot(
            x='weathersit_day',
            y='casual_day',
            data=filtered_df,
            label='Pengguna Kasual',
            color='tab:orange',
            ax=ax2[1],
            width=0.5,
            errorbar=None
        )
        ax2[1].set_title('Korelasi Pengguna Terdaftar dan Kasual', fontsize=14, fontweight='bold')
        ax2[1].set_xlabel('Kondisi Cuaca', fontsize=12, fontweight='medium')
        ax2[1].set_ylabel('Rata-rata Jumlah Pengguna', fontsize=12, fontweight='medium')
        ax2[1].legend(title='Tipe Pengguna')
        plt.tight_layout()
        st.pyplot(fig2)

        st.markdown("---")
        st.markdown("<h5 style='text-align: center;'>Dibuat dengan ❤️ oleh Ariana</h5>", unsafe_allow_html=True)
    else:
        st.error("File CSV tidak memiliki kolom yang diperlukan: 'season_day', 'registered_day', 'casual_day', 'weathersit_day', 'cnt_day'.")
except FileNotFoundError:
    st.error(f"File {DATA_PATH} tidak ditemukan. Pastikan file berada di direktori yang benar.")
