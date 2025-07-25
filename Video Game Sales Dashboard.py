# Video Game Sales Analysis Dashboard

# app.py
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# Config
st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")
sns.set(style="whitegrid")

# Load dataset
file_path = "datasets/games.csv"
if not os.path.exists(file_path):
    st.error(f"File not found: {file_path}")
    st.stop()

df = pd.read_csv('datasets/games.csv')
df.columns = df.columns.str.lower()
df = df.dropna(subset=['year_of_release', 'name', 'genre'])
df['year_of_release'] = df['year_of_release'].astype(int)
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df['rating'].fillna('Unknown', inplace=True)
df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filters")
selected_years = st.sidebar.multiselect(
    "Select Year(s):",
    options=sorted(df['year_of_release'].unique()),
    default=[2014, 2015, 2016]
)

selected_platforms = st.sidebar.multiselect(
    "Select Platform(s):",
    options=sorted(df['platform'].unique()),
    default=['PS4', 'XOne']
)

selected_genres = st.sidebar.multiselect(
    "Select Genre(s):",
    options=sorted(df['genre'].unique()),
    default=['Action', 'Shooter']
)

# Apply filters
filtered_df = df[
    (df['year_of_release'].isin(selected_years)) &
    (df['platform'].isin(selected_platforms)) &
    (df['genre'].isin(selected_genres))
]

# Tabs for navigation
tab1, tab2 = st.tabs(["Dashboard", "Hypothesis Testing"])

# ---------------- TAB 1: Dashboard ----------------
with tab1:
    st.title("Video Game Sales Dashboard (Interactive)")

    # KPIs
    col1, col2, col3 = st.columns(3)
    if not filtered_df.empty:
        top_platform = filtered_df.groupby('platform')['total_sales'].mean().idxmax()
        top_genre = filtered_df.groupby('genre')['total_sales'].median().idxmax()
        total_sales = filtered_df['total_sales'].sum()
    else:
        top_platform = "N/A"
        top_genre = "N/A"
        total_sales = 0

    col1.metric("Top Platform (avg sales)", top_platform)
    col2.metric("Top Genre (median sales)", top_genre)
    col3.metric("Total Global Sales (M)", f"{total_sales:.2f}")

    # Games Released Per Year
    st.subheader("Games Released Per Year")
    games_per_year = filtered_df.groupby('year_of_release')['name'].count()
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    games_per_year.plot(kind='bar', ax=ax1, color='skyblue')
    st.pyplot(fig1)

    # Regional Sales Pie
    st.subheader("Regional Sales Distribution")
    region_sales = filtered_df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum()
    fig2, ax2 = plt.subplots(figsize=(5, 5))
    region_sales.plot(kind='pie', autopct='%1.1f%%', ax=ax2, startangle=90)
    ax2.set_ylabel('')
    st.pyplot(fig2)

    # Top Platforms
    st.subheader("Top Platforms by Average Sales")
    top_platforms = filtered_df.groupby('platform')['total_sales'].mean().nlargest(5)
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=top_platforms.values, y=top_platforms.index, ax=ax3)
    st.pyplot(fig3)

with tab1:
    st.title("Video Game Sales Dashboard (Interactive)")

    if not filtered_df.empty:
        # Calculate KPIs
        num_games = filtered_df['name'].nunique()
        avg_user_score = filtered_df['user_score'].mean()
        avg_critic_score = filtered_df['critic_score'].mean()
        top_game = filtered_df.loc[filtered_df['total_sales'].idxmax(), 'name']
        top_game_sales = filtered_df['total_sales'].max()

        # Display KPI cards
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Games Released", num_games)
        kpi2.metric("Avg User Score", f"{avg_user_score:.2f}" if not np.isnan(avg_user_score) else "N/A")
        kpi3.metric("Avg Critic Score", f"{avg_critic_score:.2f}" if not np.isnan(avg_critic_score) else "N/A")
        kpi4.metric("Top Game", f"{top_game} ({top_game_sales:.2f}M)")

    else:
        st.warning("No data available for the selected filters.")


# ---------------- TAB 2: Hypothesis Testing ----------------
with tab2:
    st.title("Hypothesis Testing (Dynamic)")
    ALPHA = 0.05

    def run_ttest(sample1, sample2):
        t_stat, p_val = stats.ttest_ind(sample1.dropna(), sample2.dropna())
        return p_val

    if not filtered_df.empty:
        # Hypothesis 1: Xbox One vs PC
        st.subheader("Hypothesis 1: Xbox One vs PC Ratings")
        xbox_ratings = filtered_df[filtered_df['platform'] == 'XOne']['user_score']
        pc_ratings = filtered_df[filtered_df['platform'] == 'PC']['user_score']
        if len(xbox_ratings) > 1 and len(pc_ratings) > 1:
            p_val1 = run_ttest(xbox_ratings, pc_ratings)
            st.write(f"P-value: **{p_val1:.4f}**")
            st.write("**Conclusion:**", "Reject H0" if p_val1 < ALPHA else "Fail to reject H0")
        else:
            st.write("Not enough data for Xbox One vs PC comparison.")

        # Hypothesis 2: Action vs Sports
        st.subheader("Hypothesis 2: Action vs Sports Ratings")
        action_ratings = filtered_df[filtered_df['genre'] == 'Action']['user_score']
        sports_ratings = filtered_df[filtered_df['genre'] == 'Sports']['user_score']
        if len(action_ratings) > 1 and len(sports_ratings) > 1:
            p_val2 = run_ttest(action_ratings, sports_ratings)
            st.write(f"P-value: **{p_val2:.4f}**")
            st.write("**Conclusion:**", "Reject H0" if p_val2 < ALPHA else "Fail to reject H0")
        else:
            st.write("Not enough data for Action vs Sports comparison.")
    else:
        st.warning("Filtered dataset is empty. Adjust filters.")

