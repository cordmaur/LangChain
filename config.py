import os
import pandas as pd
df = pd.read_feather('config.bin')
os.environ.update({df.loc[0].value: df.loc[1].value})