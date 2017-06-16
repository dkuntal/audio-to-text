import tflearn
import speech_data

learning_rate = 0.0001
training_iters = 30000

batch = word_batch = speech_data.mfcc_batch_generator(64)
X, Y = next(batch)
trainX, trainY = X, Y
testX, testY, x, Y


net = tflearn.input_data([None, 20, 80])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, 10, activitation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')
