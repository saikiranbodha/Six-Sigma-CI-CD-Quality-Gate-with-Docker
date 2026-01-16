import pandas as pd

def check_data_quality(file_path: str):
    df = pd.read_csv(file_path)

    defects = 0

    # Rule 1: Missing values
    defects += df.isnull().sum().sum()

    # Rule 2: Invalid salary
    defects += (df["salary"] < 0).sum()

    # Rule 3: Invalid age range
    defects += ((df["age"] < 18) | (df["age"] > 60)).sum()

    # Rule 4: Invalid experience
    defects += (df["experience"] < 0).sum()

    total_opportunities = df.shape[0] * df.shape[1]

    return defects, total_opportunities
