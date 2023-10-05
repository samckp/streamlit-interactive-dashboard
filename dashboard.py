import pandas as pd
import numpy as np
import panel as pn

import hvplot.pandas


pn.extension('tabulator')


# cache data to improve dashboard performance
if 'data' not in pn.state.cache.keys():

    df = pd.read_csv('TeamsHalf.csv')

    pn.state.cache['data'] = df.copy()

else: 

    df = pn.state.cache['data']

df


pn.extension()

df.interactive(width=600).head(n=pn.widgets.IntSlider(start=1, end=5, value=3))

hvplot.help(kind='scatter')



