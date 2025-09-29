# Example: how to load a saved model (placeholder)
# For ARIMA/Prophet you may use pickle. For LSTM use keras.models.load_model.
try:
    import pickle
    with open("models/arima_model.pkl","rb") as f:
        arima = pickle.load(f)
except Exception as e:
    print("No ARIMA model found yet. Train and save models into the /models directory.")
