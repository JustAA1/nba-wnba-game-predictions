# HoopFuture

## Overview

HoopFuture predicts NBA/WNBA game winners for a chosen day. It was built mainly to practice an end-to-end ML pipeline (live schedule data, a simple classifier, console output), not to maximize accuracy. With only team, arena, and tip-off time as inputs (no form, injuries, or box-score stats), the model mostly picks up coarse home-court/matchup patterns, so predictions stay rough.

## Features

### 1. Model Training

- **Data Splitting:** Split into training and testing sets 
- **One-Hot Encoding:** Non-numeric input data is converting into usable, numeric data for the model
- **Logistic Regression Model:** To get a binary outcome (W or L for the home team)
- **Training on Completed Data:** Trains the model on completed data (games that have already occurred)

### 2. Upcoming Predictions

- **Data Preparation:** Upcoming game data is provided as a dictionary and converted into a Pandas DataFrame
- **One-Hot Encoding:** Non-numeric input data is converting into usable, numeric data for the model
- **Model Predictions:** Using this future game data to predict each outcome with the model

### 3. PrettyTable Output

- **Predictions Display:** Provides simple text-based display predictions for each game on a certain day
- **Additional Information:** Team win-loss records shown for both teams.
- **Console Display:** Prints the final table to the console, showing matchups and predicted winners.

## Prerequisites

Dependencies or prerequisites.

- Python 3.8+ (I used 3.11.5)
- Required Python packages (numpy, pandas, scikit-learn, prettytable, nba_api)

### Data Source

- NBA Game Data sourced from [nba.com](https://www.nba.com/).
- WNBA Game Data sourced from [wnba.com](https://www.wnba.com/).
- NBA/WNBA Standings sourced from [nba_api](https://github.com/swar/nba_api).

