# Identifying Success Patterns in Video Game Sales

These projects explore the key factors driving the commercial success of video games across platforms, genres, regions, and time periods. Using historical data, KPI dashboards, and statistical analysis, the objective is to extract actionable insights that can inform product development, marketing strategies, and advertising campaigns for a fictional video game retailer, Ice.

The analysis leverages user and critic reviews, sales trends, platform performance, and ESRB ratings to identify patterns behind blockbuster titles and market behavior. The primary time frame of interest is 2016, with the scenario set in December 2016 as the team plans campaigns for 2017.

## Project 1: Strategic Insights for Gaming Success
- Period Analyzed: 2016–2017
- File: video_game_sales_analysis_2016_2017.ipynb

### Overview
This project investigates global video game sales and trends to uncover the factors that contribute to a game’s success. It focuses on analyzing user and critic reviews, sales by platform and genre, and regional performance to support inventory and marketing decisions.

### Key Objectives
- Clean and preprocess raw game sales data
- Analyze trends by platform, genre, and region
- Explore the relationship between review scores and total sales
- Test hypotheses on platform and genre ratings
- Identify top-performing genres and ESRB rating patterns

### Tools & Libraries
- pandas, numpy – Data manipulation
- matplotlib, seaborn – Visualizations
- scipy.stats – Hypothesis testing

### Hypotheses Tested
- Are user ratings significantly different between Xbox One and PC?
- Do Action and Sports games have similar user ratings?
- Have user ratings changed significantly before and after 2010?

Key Findings
- PS4 and Xbox One were the most profitable platforms.
- Action games were the most common, while Shooter and Platform genres had higher median sales.
- North America led in overall sales.
- Critic scores showed a moderate correlation (0.41) with sales, while user scores had minimal impact.
- Wii Sports was the highest selling game.
- Hypothesis testing revealed significant differences between genres and pre-/post-2010 ratings.

## Project 2: Video Game KPI Dashboard & Ratings Analysis
- File: video_game_kpi_dashboard.py

### Overview
This project builds an interactive KPI dashboard to visualize game sales performance. It evaluates top performing platforms and genres, analyzes regional market share, and studies the impact of user and critic ratings on sales.

### KPI Highlights
- Top platform by average sales: Game Boy
- Top genre by median sales: Platform
- Region with highest total sales: North America
- Critic score correlation with sales: 0.25
- Percentage of games rated 8+ by users: 15.47%
- Top-selling game: Wii Sports (82.54M units)

### Dashboard Visualizations
- Bar charts: Top platforms and genres
- Pie chart: Regional sales distribution
- KPI cards: Critic score impact and highly-rated games
- Line & box plots: Sales trends and variation

### Tools Used
- pandas, numpy, scipy – Data analysis
- seaborn, matplotlib – Dashboard visualizations
- os, warnings – Environment configuration
