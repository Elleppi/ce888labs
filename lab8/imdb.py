
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Activation, Embedding, Flatten, Input, Dropout, Conv1D, Conv2D, MaxPooling2D, GlobalMaxPooling1D, GlobalMaxPooling2D, LSTM
from keras.datasets import imdb

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

print (X_train[0])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')


inputs = Input(shape=(maxlen,))
x = inputs
x = Embedding(max_features, 128, dropout=0.2)(x)

# 1. `Modify the code to add one more layer of 64 relu units after the embedding layer record the score (i.e. add a dense followed by an "activation" layer)'.
# x = Dense(64, activation='relu')(x)

# 2. `Modify the code and add a dropout layer after the relu layer'.
# x = Dropout(0.5)(x)

# 3. `Remove the layers you have added previously and add a Convolution layer followed by a relu non-linearity and global max pooling (see lecture notes)'.
# x = Conv1D(64, kernel_size=(3), strides=(1), activation='relu')(x)

# 4. `Modify the code and add an LSTM layer in place of the convolution layer'.
x = LSTM(64, activation='relu')(x)

# x = GlobalMaxPooling1D()(x)

# x = Flatten()(x)
x = Dense(1)(x)
predictions = Activation("sigmoid")(x)


model = Model(input=inputs, output=predictions)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
