from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

import schedule_data as bball_data

# splitting data into feature and target with one-hot encoding
def preprocess_data(df_data):
    # columns to one-hot encode
    to_one_hot_encode = ['Away', 'Home', 'Arena', 'Start (ET)']

    # get input features and target data
    X_completed = df_data[to_one_hot_encode]
    y_completed = df_data['HomeWin']

    # use ColumnTransformer with OneHotEncoder
    column_transformer = ColumnTransformer(
        transformers=[
            ('onehot', OneHotEncoder(drop='first'), to_one_hot_encode)],
        remainder='passthrough')

    # fit the transformer on the training data
    X_completed_encoded = column_transformer.fit_transform(X_completed)

    return X_completed_encoded, y_completed, column_transformer


# using Logistic Regression Model to predict outcome
def predict_with_model(df_upcoming_game, X_completed_encoded, y_completed, column_transformer):
    # splitting data into training and testing data sets
    X_train, _, y_train, _ = train_test_split(X_completed_encoded, y_completed, test_size=0.2, random_state=42)

    # train the logistic regression model
    model_completed = LogisticRegression()

    # fit trained data onto the model
    model_completed.fit(X_train, y_train)

    # transform the new data using the fitted transformer
    df_upcoming_game_encoded = column_transformer.transform(df_upcoming_game)

    # get probabilities using the trained model
    predicted_probabilities = model_completed.predict_proba(df_upcoming_game_encoded)
    return predicted_probabilities


def get_probs(date, nba=True):
    df_predict_game, df_total_data = bball_data.get_data(date, nba)

    # preprocess data
    X_completed_encoded, y_completed, column_transformer = preprocess_data(df_total_data)

    # get predictions as probabilities
    probabilities = predict_with_model(df_predict_game, X_completed_encoded, y_completed, column_transformer)
    return probabilities, df_predict_game
