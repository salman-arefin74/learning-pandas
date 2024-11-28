import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.query('weight > 100').sort_values(['weight'], ascending=False).drop(['species', 'age', 'weight'], axis=1)

    # Alternative Solution:
    # return animals[animals['weight'] > 100].sort_values(['weight'],ascending=False)[['name']]
