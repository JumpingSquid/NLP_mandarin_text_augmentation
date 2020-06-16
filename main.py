import pandas as pd
import numpy as np

from augtool import replace

syno_df = pd.read_csv("data/syno/word_replace_t.csv")
syno_map = {}
for i, r in syno_df.iterrows():
    if r["source"] not in syno_map:
        syno_map[r["source"]] = [r["target"]]
    else:
        syno_map[r["source"]].append(r["target"])

