import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


def main():
    df = pd.read_csv("data.csv")
    X = df[["x"]]
    y = df["y"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "model.pkl")
    print("Model eğitildi ve model.pkl dosyasına kaydedildi.")


if __name__ == "__main__":
    main()
