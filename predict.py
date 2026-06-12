import pickle

model = pickle.load(
    open("models/crop_model.pkl", "rb")
)

sample = [[90,42,43,20.8,82,6.5,202]]

prediction = model.predict(sample)

print("Recommended Crop:", prediction[0])