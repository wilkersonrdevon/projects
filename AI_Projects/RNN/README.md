# Recurrent Neural Network Project

## Part 1

This part implements a basic RNN network to solve time series prediction by:

1. Loads the given train and test data: "train.txt" and "test.txt"
2. Generates the TRAIN and TEST labels
3. Normalizes the TRAIN and TEST data with sklearn function "MinMaxScaler"
4. Prints out the TEST data and label
5. Builds an RNN model with 1 RNN layer and 1 Dense layer
6. Compiles the model
7. Trains the model for 1000 epochs with batch_size = 10
8. Does direct prediction on train and test datapoints with the obtained model
9. Scales the prediction results back to original representation with the scaler
10. Calculates root mean squared error (RMSE) and print out the error for both TRAIN and TEST
11. Plots the TEST label and prediction

## Part 2

This part implements an LSTM network to conduct sentiment analysis by:

1. Load the data from IMDB review dataset and print out the lengths of sequences. (3 Points)
2. Preprocess review data to meet the network input requirement by specifying number of words=1000, setting the analysis length of the review = 100, and padding the input sequences. (10 Points)
3. Build the LSTM model with 1 embedding layer, 1 LSTM layer, and 1 Dense layer. Print out model summary. The embedding vector is specified with the dimension of 8. (10 Points)
4. Compile the LSTM model with Adam optimizer, binary_crossentropy loss function, and accuracy metrics. (5 Points)
5. Train the LSTM model with batch_size=64 for 10 epochs and report training and validation accuracies over epochs. (5 Points)
6. Print out best validation accuracy. (5 Points)

## Part 3

This part modifies the vanilla model above in three separate scenarios by hyperparameter tuning:

Scenario 1:
    Adds one additional LSTM layer (total 2 LSTM layers)
    Modifies the embedding dimension to 16
    Modifies the units of LSTM to 16
Scenario 2:
    Adds one additional LSTM layer (total 2 LSTM layers)
    Modifies the embedding dimension to 128
    Modifies the units of LSTM to 128
Scenario 3:
    Adds one additional LSTM layer (total 2 LSTM layers)
    Modifies the embedding dimension to 128
    Modifies the units of LSTM to 128
    Increases analysis length for review data to maxlen = 200
