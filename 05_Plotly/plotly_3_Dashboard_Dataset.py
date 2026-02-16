import pandas as pd
from dash import Dash, html, dcc, 
import plotly.express as px
# dcc : dash core components

app = Dash(__name__) # Use __name__ with two underscores
app.layout = html.Div([
    html.H1('My first Dashboard'),
    html.P('This is my Dashboard')
])
# Sample Data
data = {'Region':['North', 'South', 'East','West'],
        'Sales': [50000, 40000, 30000, 45000]}
df = pd.DataFrame(data)
fig = px.bar(df, x='Region', y='Sales', title = 'Sales by Region')
app.layout = html.Div([html.H1('Sales Dashboard'),
                       html.H3('Total Sales'),
                       html.H2(f'{df['Sales'].sum()}'),
                       dcc.Graph(figure = fig)
                       ])

if __name__ == '__main__':
    app.run(debug = True)