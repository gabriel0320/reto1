import pandas as pd

# Download latest version
path = "Energia_en_ZNI.csv"

reatail_data = pd.read_csv(path, encoding= 'latin1')

print(type(reatail_data))

print(reatail_data)