# Premier League Stats Scraper and MySQL Database

This project is designed to scrape Premier League statistics from the **fbref.com** website and create a **MySQL database** to store this data. Additionally, it generates interactive plots using the **Plotly** library.

## Project Overview
- **Objective**: Collect and analyze Premier League team and player stats.
- **Data Source**: Scrapes data from **fbref.com**.
- **Components**:
    - **main.ipynb**: Scrapes and processes the data, then creates the MySQL database.
    - **visualization.ipynb**: Generates interactive plots using Plotly.
  
**NOTE**: Due to the Github error, plots created with `plotly` library aren't displayed. 

## Features
1. **Data Scraping**:
    - Utilizes web scraping techniques to extract Premier League stats.
    - Collects both team and player data.
2. **MySQL Database**:
    - Creates a structured database to store the scraped data.
    - Includes tables for teams, players, match and other relevant information.
3. **Interactive Plots**:
    - Uses Plotly to create dynamic visualizations.
    - Allows users to explore trends, compare teams, and analyze player performance.

## Future Enhancements
- Include additional leagues or competitions.
- Improve data cleaning and preprocessing.
- Add more advanced visualizations and insights.
