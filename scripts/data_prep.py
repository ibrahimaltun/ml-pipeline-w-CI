import pandas as pd

def main():
    # Basit bir veri seti oluştur
    data = {
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)
    print("Veri hazırlandı ve data.csv dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
