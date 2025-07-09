# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("Used_Bikes.csv")

# Manual brand encoding (must match Flask app)
brand_map = {
    'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3, 'Honda': 4,
    'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8, 'KTM': 9,
    'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12, 'Hyosung': 13, 'Harley-Davidson': 14,
    'Jawa': 15, 'BMW': 16, 'Indian': 17, 'Rajdoot': 18, 'LML': 19,
    'Yezdi': 20, 'MV': 21, 'Ideal': 22
}

df["brand_encoded"] = df["brand"].map(brand_map)

# Drop missing values in relevant columns
df.dropna(subset=["owner", "brand_encoded", "kms_driven", "age", "power", "price"], inplace=True)

# Define X and y
X = df[["owner", "brand_encoded", "kms_driven", "age", "power"]]
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained with 5 features and saved as model.pkl")
