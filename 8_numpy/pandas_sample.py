import numpy as np
import pandas as pd

data = { 
    "names" : ["Anup","Aman","Vinay","Rohan",], 
    "marks" : [80,67,89,90],
    "native": ["Hebri","Mandarthi","Kundapura","Mangalore"]

}

df = pd.DataFrame(data)

print(df,"\n\n")
print(df.describe())