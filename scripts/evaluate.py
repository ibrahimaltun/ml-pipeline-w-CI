import pandas as pd
import joblib
import os


def main():
    df = pd.read_csv("data.csv")
    X = df[["x"]]
    y = df["y"]

    model = joblib.load("model.pkl")
    score = model.score(X, y)

    os.makedirs("results", exist_ok=True)

    with open("results/score.txt", "a") as f:
        f.write(f"Model R^2 skoru: {score}\n")

    print(f"Model başarı skoru: {score}")


if __name__ == "__main__":
    main()
