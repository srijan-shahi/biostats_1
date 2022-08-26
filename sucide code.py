import matplotlib as mat
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px
df = pd.read_csv('countries.csv')
fig = px.line(df,x='Year',y='Deaths(x1000)',title='Suicide in India')
fig.show()
