import pandas as pd
import numpy as np
import math
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt 

#load the data
df = web.DataReader('FBGRX', data_source='yahoo', start='2016-01-01', end='2020-07-01')# how to import a file

# show part of the data as a graph
# plt.figure(figsize=(16,8))
# plt.title('Closing Price')
# plt.plot(df['Close'])
# plt.xlabel('Date',fontsize=18)
# plt.ylabel('Close Price USD($)', fontsize=18)
# plt.show()

data = df.filter(['Close'])
dataset = data.values

training_data_amt = math.ceil(len(dataset)* .8)

#scale the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

#create the training dataset
train_data = scaled_data[0:training_data_amt, :]

#Split the data into x_train and y_train
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])

#convert the x_train and y_train 
x_train, y_train = np.array(x_train), np.array(y_train)

#reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# #build the LSTM model
model = Sequential()
model.add(LSTM(50,return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50,return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

#Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

#Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

#create the testing data set
test_data = scaled_data[training_data_amt - 60:, :]
x_test = []
y_test = dataset[training_data_amt:,:]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i,0])

#convert data into a numpy array
x_test = np.array(x_test)
# #reshape the data
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#Get the model's predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

#get the root mean squared error (RMSE)
rmse  = np.sqrt( np.mean(predictions - y_test)**2)

#plot the data 
train = data[:training_data_amt]
valid = data[training_data_amt:]
valid['Predictions'] = predictions
#Visualize the data
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date',fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val','Predict'], loc='lower right')
plt.show()

