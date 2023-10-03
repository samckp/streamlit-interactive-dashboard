import pandas as pd
import numpy as np
import panel as pn
pn.extension('tabulator')

import hvplot.pandas

# cache data to improve dashboard performance
if 'data' not in pn.state.cache.keys():

    df = pd.read_csv('TeamsHalf.csv')

    pn.state.cache['data'] = df.copy()

else: 

    df = pn.state.cache['data']

df

