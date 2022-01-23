# https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo

# https://plotly.com/python/scatter-plots-on-maps/

# https://www.kaggle.com/subinium/road-to-viz-expert-3-geo-with-plotly-express

# https://www.kaggle.com/paultimothymooney/latitude-and-longitude-for-every-country-and-state?select=world_country_and_usa_states_latitude_and_longitude_values.csv

#longitude / latitude.
import pandas as pd
import numpy as np 
import plotly.express as px

data =  np.array([["arg", (-51.92528, -14.235004)], ["bra",  (-63.616672, -38.416097)]])

df =  pd.DataFrame(data, columns= ['nome' , 'iso_alpha'])

print(df)


df = px.data.gapminder().query("year == 2007")
fig = px.scatter_geo(df, locations="iso_alpha",
                     color="continent", # which column to use to set the color of markers
                     projection="natural earth")
fig.show()
