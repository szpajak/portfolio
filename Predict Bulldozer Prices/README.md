# Predicting the Sale Price of Bulldozers using Machine Learning

## 1. Problem Definition
The main goal of this project is to predict the future sale prices of bulldozers based on their characteristics and historical data of similar bulldozers' sale prices. This task falls under the domain of time series forecasting, where we aim to utilize Machine Learning techniques to make accurate predictions.

## 2. Data
The dataset used in this project is sourced from the Kaggle Bluebook for Bulldozers competition, which can be accessed through the following link: [Kaggle Bluebook for Bulldozers](https://www.kaggle.com/c/bluebook-for-bulldozers/data).

There are three primary datasets included:

- **Train.csv**: This dataset serves as the training set and encompasses data up to the end of 2011.
- **Valid.csv**: The validation set contains data ranging from January 1, 2012, to April 30, 2012. Participants use this set to make predictions during most of the competition, and their performance on this set contributes to the public leaderboard.
- **Test.csv**: This test set will only be released in the last week of the competition and comprises data from May 1, 2012, to November 2012. Participants' scores on this set determine their final ranking in the competition.

## 3. Evaluation
The evaluation metric for assessing the performance of our predictive model in this competition is the RMSLE (Root Mean Squared Log Error). This metric quantifies the difference between the actual and predicted auction prices, providing a comprehensive measure of the model's accuracy in predicting bulldozer sale prices over time.
