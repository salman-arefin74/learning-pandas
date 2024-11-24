import pandas as pd

# My solution:
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    data = []
    for row in employees.head(3).itertuples(index=False):
        data.append(row)
    
    return pd.DataFrame(data)
    
# Better solution:
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3) #SIGH!
