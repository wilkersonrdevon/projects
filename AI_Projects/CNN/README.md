# Convolutional Neural Network Project

## Part 1

This part does Digital Image Processing using numpy, imageio, and IPython by:

1. Displays the image in the output box before image-array conversion.
2. Prints out the size of the array
3. Prints out the numeric matrix form of image, i.e. the obtained array after image-array conversion
4. Prepare a 3X3 Laplacian kernel (aka Laplacial filter) with array as convolution filter
5. Conducts convolution on image with prepared kernel
6. Prints out convolution result for first ten rows
7. Prints out the shape of the convolution result
8. Displays convolution result as image with matplotlib
9. Modifies the convolution process with stride=2
10. Prints out convolution result for first ten rows
11. Prints out the shape of the convolution result
12. Displays convolution result as image with matplotlib
13. Prepares a 2X2 pooling mask
14. Conducts max pooing on image with prepared mask
15. Prints out convolution result for first ten rows
16. Prints out the shape of the convolution result
17. Displays convolution result as image with matplotlib

## Part 2

This part uses tensorflow to solve a classification problem using the Fashion MNIST dataset by:

1. Downloads Fashion MNIST data and splits it with keras and prepare training/test data sets
2. Preprocesses training/test data with normalization, dimension extension, and zero padding (for LeNet-5 configuration)
3. Preprocesses label data to binary class matrices
4. Prints out first image in training set and its correponding label index
5. Prints out the shape of total training data, the number of training samples, and the number of test samples
6. Builds up LeNet-5 with keras.Sequential
7. Sets the regularizer to l2 and regularizer lambda is 4e-5
8. Prints out the model summary
9. Sets batch size to 64 for training
10. Picks SGD optimizer with learning rate of 0.1, momentum of 0.9, and nesterov=True, for model training
11. Picks cross-entropy loss function for optimization and evaluation metrics is set to accuracy
12. Sets validation_split to 0.1 which means it excludes 1/10 training data for validation process
13. Trains the model with 10 epochs
14. Evaluates model with test data set and prints out : test loss and test accuracy.
15. Tries only modify batch size to 128 and sees if there is a difference
16. Reports final test loss and test accuracy and intermediate training/validation loss plots over epochs
17. Tries only modify optimizer to Adam (optimizer="adam") and sees if there is a difference
18. Reports final test loss and test accuracy and intermediate training/validation loss plots over epochs
19. Tries only change learning rate to 0.05 and sees if there is a difference
20. Reports final test loss and test accuracy and intermediate training/validation loss plots over epochs
