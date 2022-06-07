# %% codecell
import numpy as np
import pandas as pd
from datetime import datetime
import re

# %% codecell

connected = []
disconnected = []

szukane = r'(?:\d{1,3}\.)+(?:\d{1,3})'


with open("tarpit.log", "r") as f:
    for i in range(50):
        line = f.readline()
        dt = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if 'TarpitServer: Client' in line:
            print(dt, re.search(szukane, line))

# %%
