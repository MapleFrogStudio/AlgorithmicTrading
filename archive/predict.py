import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

import stocks

def load_prices(ticker):
    start = "2013-01-01"
    end = "2021-03-01"
    # ticker = "FB"
    df = stocks.GrabPrices(ticker, start, end)
    return df

def add_test_data_to_prices(df):
    # Ads indicators to dataframe
    df['HL_pct'] = (df['High'] - df['Low']) / df['Low'] * 100

    # Add a new column with the 3 day prediction based on the price for the days before
    predict_col = 'Adj Close'
    df.fillna(0, inplace=True)
    df['future3days'] = df[predict_col].shift(-3)
    df.dropna(inplace=True)

    return df

def prepare_training_data(df):
    # Let's use the SciKit Learn package
    # Using data split for testing and linear regression to train the model
    #
    X = np.array(df.drop(['future3days'], 1))
    X = preprocessing.scale(X)
    y = np.array(df['future3days'])
    # Split our historic data into 30% test data and 70% train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3)
    return X_train, X_test, y_train, y_test

def save_our_classifier(X_train, X_test, y_train, y_test, ticker):
    #Multiple Linear Regression model using a clf (Classifier)
    clf = LinearRegression()
    clf.fit(X_train, y_train)

    #Save out classifier model
    with open(f"{ticker}_predictionmodel.pickle", "wb") as f:
        pickle.dump(clf, f)

    confidence = clf.score(X_train, y_train)
    print(f"Accuracy : {confidence}")

def use_our_classifier():
    with open(f"{ticker}_predictionmodel.pickle", "rb") as f:
        clf = pickle.load(f)


# Load our prices and add prediction for training (price 3 days before)
ticker = 'FB'
df = load_prices('FB')
print(f"Raw data from web:\n{df.tail(10)}")
df = add_test_data_to_prices(df)
print(f"\nPrices with new columns for prediction (last 3 days removed because NaN values):\n {df.tail(10)}")

# Train our classifier and save it as a pickle binary file
X_train, X_test, y_train, y_test = prepare_training_data(df)
save_our_classifier(X_train, X_test, y_train, y_test, ticker)

# Load our classifer and do some predictions


