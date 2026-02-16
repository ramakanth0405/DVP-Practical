import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__)
# Sample Data
df = pd.DataFrame({'Product':['Laptop', 'Mac', 'Printer','Mac', 'Printer'],
                   'Region':['North', 'South', 'East', 'West', 'North'],
                   'Sales':[300, 400, 500, 600, 700]})

app.layout = html.Div([
    html.H1('Interactive Sales Dashboard'),
    html.Label('Select Product: '),
    dcc.Dropdown(
        id = 'Product Dropdown',
        options = [
            {'Label': 'Product A', 'Value': 'A'},
            {'Label': 'Product B', 'Value':'B'}
        ],
        value = 'A'
        
    ),
    dcc.Graph(id = 'Sales_Chart')
])

# Call Back
@app.callback(
    Output('Sales_Chart', 'Figure'),
    Input('Product_Dropdown', 'Value')
)
def update_chart(selected_product):
    filtered_df = df[df['Product']==selected_product]
    fig = px.bar(filtered_df, x= 'Region', y = 'Sales',
                 title = f'Sales by Region for Product {selected_product}')
    return fig
if __name__ == '__main__':
    app.run(debug = True)