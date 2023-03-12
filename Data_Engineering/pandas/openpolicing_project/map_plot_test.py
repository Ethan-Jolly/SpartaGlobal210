import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('nashville_data_cleaned.csv')
print(df.head())
df = df[df['lat'].notna()]
df = df[df['lng'].notna()]
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
# df = df.loc['2018-01-01':'2018-12-31']
df = df.loc[:, ['lat', 'lng']].drop_duplicates()

fig = px.scatter_mapbox(df, lat='lat', lon='lng')
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
