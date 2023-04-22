import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Load the energy consumption data into a pandas DataFrame
data = pd.read_csv('energy_consumption.csv', index_col='Date', parse_dates=True)

# Visualize the energy consumption data
plt.plot(data)
plt.xlabel('Date')
plt.ylabel('Energy Consumption')
plt.title('Energy Consumption Time Series')
plt.show()

# Split the data into training and testing sets
train_data = data[:'2019-12-31']
test_data = data['2020-01-01':]

# Scale the data using MinMaxScaler
scaler = MinMaxScaler()
train_data_scaled = scaler.fit_transform(train_data)
test_data_scaled = scaler.transform(test_data)

# Define the input and output data for the model
def create_dataset(dataset, time_steps=1):
    X, y = [], []
    for i in range(len(dataset)-time_steps):
        X.append(dataset[i:i+time_steps, :])
        y.append(dataset[i+time_steps, 0])
    return np.array(X), np.array(y)

time_steps = 30 # Number of time steps to look back
X_train, y_train = create_dataset(train_data_scaled, time_steps)
X_test, y_test = create_dataset(test_data_scaled, time_steps)

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_steps, 1)))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32)

# Generate predictions for the test data
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

# Plot the actual and predicted values for the test data
plt.plot(test_data.index, test_data, label='Actual')
plt.plot(test_data.index, predictions, label='Predicted')
plt.xlabel('Date')
plt.ylabel('Energy Consumption')
plt.title('LSTM Model Predictions')
plt.legend()
plt.show()