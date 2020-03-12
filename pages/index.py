# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What sport would you medal in the Olympics?

            What if you wanted to compete in the olympics?

            You can use this app and enter your gender, age, weight, height, year of olypmics and season to see 
            what sport you would do best in, compared to real olympians stats. 

            This app was soley made for educational purposes, as most do not train day in and day out,
            but fun to see!!
           
           
            """
        ),
        dcc.Link(dbc.Button('Predict Your Sport!', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col([html.Img(src = 'assets/olympic_rings.jpg', className = 'Olympic Rings')
],
align = 'center'
)

layout = dbc.Row([column1, column2])