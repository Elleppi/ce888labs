# Lab8

## Results
---
1. `run python imdb.py and note somewhere the test accuracy score.'

    Test score: 	0.687792005032
    
    Test accuracy: 	0.83652


2. `Modify the code to add one more layer of 64 relu units after the embedding layer record the score (i.e. add a dense followed by an "activation" layer)'.

    Test score: 	1.11285641961

    Test accuracy: 	0.82096


3. `Modify the code and add a dropout layer after the relu layer'.


    Test score: 1.19840768408

    Test accuracy: 0.81168


4. `Remove the layers you have added previously and add a Convolution layer followed by a relu non-linearity and global max pooling (see lecture notes)'.

    Test score: 0.92753789885

    Test accuracy: 0.83084

5. `Modify the code and add an LSTM layer in place of the convolution layer'.

    Test score: 1.56047097652

    Test accuracy: 0.79808

