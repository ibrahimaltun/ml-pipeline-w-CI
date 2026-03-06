import pandas as pd
import joblib

def main():
    df = pd.read_csv("data.csv")
    X = df[["x"]]
    y = df["y"]

    model = joblib.load("model.pkl")
    score = model.score(X, y)

    with open("results/score.txt", "w") as f:
        f.write(f"Model R^2 skoru: {score}\n")

    print(f"Model başarı skoru: {score}")

if __name__ == "__main__":
    main()
