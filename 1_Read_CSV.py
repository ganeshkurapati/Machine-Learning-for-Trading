import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    print(df.head())
    print(df.tail())
    print df[10:21]


if __name__ == "__main__":
    test_run()

