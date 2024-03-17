# Portfolio

## Introduction

Hello! I'm Szymon Pająk, a 3rd year student of Automatics and Robotics with a passion for programming. Main fields of my interests are Data Science and Machine Learning (what you can see looking through this portfolio).

This portfolio showcases a selection of projects that I've worked on. Each project summary provides insights into the objectives, methodologies, and outcomes, giving you a glimpse of my capabilities.

Feel free to explore and dive into the details of each project to get a better understanding of my skills and contributions.

## Table of Contents
1. [Premier League Stats](#premier-league-stats)
2. [OR Final Project App](#or-final-project-app)
3. [Classification Mini Project](#classification-mini-project)
4. [Predict Bulldozer Price](#predict-bulldozer-price)
5. [Heart Disease Project](#heart-disease-project) 

## Premier League Stats

This project aims to scrape Premier League statistics from the **fbref.com** website and store them in a **MySQL database**. It also provides interactive plots using the **Plotly** library.

#### Project Overview

- **Objective**: Gather and analyze Premier League team and player stats.
- **Data Source**: Scraped from **fbref.com**.
- **Components**:
  - **main.ipynb**: Scrapes and processes data, then creates the MySQL database.
  - **visualization.ipynb**: Generates interactive plots using Plotly.
  
**NOTE**: Plots made with `plotly` aren't displayed due to a Github error.

#### Features

1. **Data Scraping**:
   - Uses web scraping techniques to extract Premier League stats.
   - Gathers both team and player data.

2. **MySQL Database**:
   - Constructs a structured database for storing scraped data.
   - Includes tables for teams, players, matches, and other pertinent information.

3. **Interactive Plots**:
   - Utilizes Plotly for creating dynamic visualizations.
   - Permits users to explore trends, compare teams, and analyze player performance.

## OR Final Project App

This repository contains the code and files for optimizing the schedule of the Premier League using Operations Research techniques. It was created as a final project for an Operations Research subject, developed in collaboration by Szymon Pająk and Klaudiusz Grobelski.

The example screenshot of the app:
![App]("[portfolio/OR Final Project App/report files/Grafiki/app_start_screen.png](https://github.com/szpajak/portfolio/blob/main/OR%20Final%20Project%20App/report%20files/Grafiki/app_start_screen.png?raw=true)")

## Classification Mini Project

This repository showcases the implementation of a neural network for multiclass classification using TensorFlow. The project leverages TensorFlow's Fashion MNIST dataset, which contains 28x28 grayscale images of fashion items categorized into 10 classes:

1. T-shirt/top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle boot

The goal is to train a neural network model that accurately classifies these clothing items into their respective categories. The model architecture includes input, hidden, and output layers, designed to handle the complexity of the Fashion MNIST dataset and make precise predictions for multiclass classification tasks.

## Predict Bulldozer Price

The goal of this project is to predict the future sale prices of bulldozers based on their characteristics and historical data. The dataset is sourced from the Kaggle Bluebook for Bulldozers competition, which includes training, validation, and test sets.

The model's performance is evaluated using the RMSLE (Root Mean Squared Log Error) metric, quantifying the accuracy of predicting bulldozer sale prices over time.

## Heart Disease Project

This project aims to build a machine learning model using Python libraries to predict whether an individual has heart disease based on their medical attributes.

The dataset used for this project is sourced from the UCI Machine Learning Repository and Kaggle. It includes features such as age, gender, chest pain type, blood pressure, cholesterol level, and more.

The model's performance will be evaluated based on its accuracy in predicting the presence or absence of heart disease using these medical features.
