import pandas as pd

# My solution:
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    cols = len(players.columns)
    rows = len(players.index)
    return [rows, cols]

# Better solution:
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    [rows, cols] = players.shape
    return [rows, cols]
