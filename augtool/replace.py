import pandas as pd
import numpy as np


def word_replace(w: str, s: str, t: str):

    if s not in w:
        return w

    if (s in w) and (t not in s):
        w = w.replace(s, t)

    elif (s in w) and (t in s):
        w = w.replace(t, "[MASK]")
        w = w.replace(s, t)
        w = w.replace("[MASK]", t)

    return w
