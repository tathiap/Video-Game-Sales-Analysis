# Identifying Success Patterns in Video Game Sales for Advertising Campaign Planning

## Overall Project Overview: Analyzing Success Drivers in the Video Game Industry: 
These two projects collectively explore the key factors influencing the commercial performance of video games across platforms, genres, regions, and time periods. Using historical data, statistical testing, and KPI-driven dashboards, the goal was to uncover actionable insights that can inform product development, marketing strategies, and market expansion for a fictional video game retailer.

In this project, the goal is to analyze data from the online store Ice, which sells video games globally. The dataset includes information on user and expert reviews, genres, platforms (e.g., Xbox or PlayStation), historical data on game sales, and the Entertainment Software Rating Board (ESRB) ratings. The task is to uncover patterns that can help determine the success of video games, aiding in the identification of potential blockbuster titles and the planning of effective advertising campaigns.

The analysis covers data from 2016, with the scenario set in December 2016 as the team plans a campaign for 2017. The specific focus is on gaining valuable experience in working with data, and the time frame for forecasting sales is not strictly constrained to the year under consideration.

## Project 1: Strategic Insights for Gaming Success
Period Analyzed: 2016–2017
Filename Suggestion: video_game_sales_analysis_2016_2017.ipynb

### Overview
This project analyzes global video game sales and market trends for the years 2016 and 2017. The goal was to uncover the factors contributing to a game's commercial success using historical sales data, user and critic reviews, platform performance, and genre trends. The analysis was conducted for the fictional online retailer "Ice", which seeks to optimize its inventory and marketing strategies based on consumer behavior.
 
### Key Objectives
* Clean and prepare raw game sales data for analysis
* Examine trends across platforms, genres, and regions
* Investigate correlations between review scores and sales
* Perform hypothesis testing on platform and genre ratings
* Create user profiles by region and identify top-performing genres and ESRB ratings

### Tools & Libraries
* pandas, numpy for data manipulation
* matplotlib, seaborn for visualization
* scipy.stats for hypothesis testing

### Hypotheses Tested
* Are average user ratings significantly different between Xbox One and PC?
* Do Action and Sports games receive similar user ratings?
* Have user ratings changed before and after 2010?

### Findings Summary
* PS4 and Xbox One were the most profitable platforms
* Action games were most common, but Shooter and Platform genres had higher median sales
* North America led in total game sales
* Critic scores showed a moderate correlation with sales (0.41), user scores did not
* Wii Sports was the highest-selling game
* Hypothesis testing revealed a significant difference in genre ratings and release-era ratings

## Project 2: Video Game KPI Dashboard & Ratings Analysis
Filename Suggestion: video_game_kpi_dashboard.py

### Overview
This project builds a strategic KPI dashboard and rating analysis pipeline for global video game data. The goal was to quantify platform and genre performance, assess regional market shares, and explore the influence of user and critic reviews on game sales. Visualizations are used to support storytelling and help stakeholders make informed marketing decisions.

### KPI Highlights
* Top platform by average sales: Game Boy
* Top genre by median sales: Platform
* Region with highest sales: North America
* Critic score correlation with sales: 0.25
* Percentage of games rated 8+ by users: 15.47%
* Top-selling game: Wii Sports (82.54 million units)

### Dashboard Visualizations
* Bar charts of top platforms and genres
* Pie chart of regional sales distribution
* Critic review impact + user score badge
* Line plots and box plots for exploratory insights

### Hypotheses Tested
* No significant difference in ratings between Xbox One and PC
* Action and Sports genres differ significantly in user ratings
* User ratings shifted significantly after 2010

### Tools Used
* pandas, numpy, scipy for data analysis
* seaborn, matplotlib for KPI dashboard
* os, warnings for environment control

