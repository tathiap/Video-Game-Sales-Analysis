
# video_game_analysis.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings
import os

# Config
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")
ALPHA = 0.05

# Load Dataset
file_path = 'datasets/games.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")
df = pd.read_csv(file_path)

# Data Preparation
df.columns = df.columns.str.lower()
df = df.dropna(subset=['year_of_release', 'name', 'genre'])
df['year_of_release'] = df['year_of_release'].astype(int)
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df['rating'].fillna('Unknown', inplace=True)
df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Utility Functions
def plot_bar(series, title, xlabel, ylabel):
    series.plot(kind='bar', figsize=(12, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def plot_box(data, x, y, title):
    plt.figure(figsize=(16, 8))
    sns.boxplot(x=x, y=y, data=data)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def run_ttest(sample1, sample2, alpha=ALPHA):
    t_stat, p_val = stats.ttest_ind(sample1.dropna(), sample2.dropna())
    print(f"P-value: {p_val:.4f}")
    if p_val < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")

# EDA
# Games Released Per Year
games_per_year = df.groupby('year_of_release')['name'].count()
plot_bar(games_per_year, 'Games Released Per Year', 'Year', 'Number of Games')

# Sales Variation Across Top Platforms
top_platforms = df.groupby('platform')['total_sales'].sum().nlargest(5).index
platform_sales = df[df['platform'].isin(top_platforms)]
plot_box(platform_sales, 'platform', 'total_sales', 'Sales Variation Across Top Platforms')

# Total Sales by Platform (2014-2016)
filtered_df = df[df['year_of_release'].between(2014, 2016)]
sales_by_platform = filtered_df.pivot_table(index='year_of_release', columns='platform', values='total_sales')
sales_by_platform.plot(marker='o', figsize=(12, 6), title='Sales by Platform (2014-2016)')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Average Sales by Platform
avg_sales = filtered_df.groupby('platform')['total_sales'].mean().sort_values(ascending=False)
print("Average Sales by Platform:\n", avg_sales)

# Reviews vs. Sales (PS4)
ps4_data = filtered_df[filtered_df['platform'] == 'PS4']
plt.figure(figsize=(12, 6))
sns.scatterplot(x='user_score', y='total_sales', data=ps4_data, label='User Score')
sns.scatterplot(x='critic_score', y='total_sales', data=ps4_data, label='Critic Score')
plt.title('PS4: Review Scores vs. Sales')
plt.legend()
plt.tight_layout()
plt.show()

print("Correlation (User Score vs Sales):", ps4_data['user_score'].corr(ps4_data['total_sales']))
print("Correlation (Critic Score vs Sales):", ps4_data['critic_score'].corr(ps4_data['total_sales']))

# Genre Distribution
plt.figure(figsize=(18, 10))
plt.subplot(2, 1, 1)
sns.countplot(x='genre', data=filtered_df, order=filtered_df['genre'].value_counts().index)
plt.title('Game Count by Genre')
plt.xticks(rotation=45, ha='right')
plt.subplot(2, 1, 2)
sns.boxplot(x='genre', y='total_sales', data=filtered_df, order=filtered_df['genre'].value_counts().index)
plt.title('Sales Distribution by Genre')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Hypothesis Testing
print("\nHypothesis 1: Xbox One vs PC Ratings")
xbox_ratings = filtered_df[filtered_df['platform'] == 'XOne']['user_score']
pc_ratings = filtered_df[filtered_df['platform'] == 'PC']['user_score']
run_ttest(xbox_ratings, pc_ratings)

print("\nHypothesis 2: Action vs Sports Ratings")
action_ratings = filtered_df[filtered_df['genre'] == 'Action']['user_score']
sports_ratings = filtered_df[filtered_df['genre'] == 'Sports']['user_score']
run_ttest(action_ratings, sports_ratings)

print("\nAdditional Test: Pre vs Post 2010 Ratings")
before_2010 = df[df['year_of_release'] < 2010]['user_score']
after_2010 = df[df['year_of_release'] >= 2010]['user_score']
run_ttest(before_2010, after_2010)

# KPI Summary
top_platform_avg_sales = df.groupby('platform')['total_sales'].mean().sort_values(ascending=False)
top_genre_median_sales = df.groupby('genre')['total_sales'].median().sort_values(ascending=False)
region_sales_series = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum()
critic_corr = ps4_data['critic_score'].corr(ps4_data['total_sales'])
percent_highly_rated = (df[df['user_score'] >= 8].shape[0] / df.shape[0]) * 100
best_selling_game = df.loc[df['total_sales'].idxmax(), ['name', 'total_sales']]

# KPI Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Top Platforms by Avg Sales
sns.barplot(x=top_platform_avg_sales.head(5).values, y=top_platform_avg_sales.head(5).index, ax=axes[0, 0])
axes[0, 0].set_title('Top 5 Platforms by Avg Sales')
axes[0, 0].set_xlabel('Average Sales (millions)')

# Top Genres by Median Sales
sns.barplot(x=top_genre_median_sales.head(5).values, y=top_genre_median_sales.head(5).index, ax=axes[0, 1])
axes[0, 1].set_title('Top 5 Genres by Median Sales')
axes[0, 1].set_xlabel('Median Sales (millions)')

# Region Sales Distribution
region_sales_series.plot(kind='pie', autopct='%1.1f%%', ax=axes[1, 0], startangle=90)
axes[1, 0].set_ylabel('')
axes[1, 0].set_title('Regional Sales Distribution')

# Correlation Summary and Top Game
axes[1, 1].text(0.5, 0.6, f'Critic Score Correlation:\n{critic_corr:.2f}',
                ha='center', fontsize=14)
axes[1, 1].text(0.5, 0.4, f'Games Rated 8+:\n{percent_highly_rated:.2f}%',
                ha='center', fontsize=14)
axes[1, 1].text(0.5, 0.2, f'Top Game:\n{best_selling_game["name"]}\n{best_selling_game["total_sales"]:.2f}M',
                ha='center', fontsize=14)
axes[1, 1].set_axis_off()

plt.suptitle('KPI Visualization Dashboard', fontsize=18, y=1.02)
plt.tight_layout()
plt.show()

