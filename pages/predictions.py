# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import numpy as np
from joblib import load

# Imports from this application
from app import app

#Load pipeline
pipeline = load('./assets/final_pipeline.joblib')


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   #Gender dropdown menu (male, female)
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('Gender'),
        dcc.Dropdown(
            id = 'Sex',
            options = [
                {'label': 'Male', 'value': 'Male'},
                {'label': 'Female', 'value': 'Female'},
            ],
            className = 'mb-5',
            value = 'Male',
            placeholder='Select a gender'
            
    ),
         #Age
        html.Hr(),
        html.Label('How old are you?',style={'display':'inline-block'}),
        dcc.Slider(
            id = 'Age',
            min = 10,
            max = 100,
            step = 1,
            value = 30,
            marks = {'10': '10','25':'25','50': '50', '75': '75','100': '100'}),
         html.Br(),
         html.P('10', id='age-selected-selected'),

         html.Br(),
        
        #Height
        html.Hr(),
        html.Label('How tall are you? (in inches!)',style={'display':'inline-block'}),
        dcc.Slider(
            id = 'Height',
            min = 50,
            max = 90,
            step = 1,
            value = 70,
            marks = {'50': '50','60':'60','70': '70', '80': '80', '90': '90'}),
         html.Br(),
         html.P('120', id='height-selected-selected'),

         html.Br(),
        
        #Weight
          html.Hr(),
        html.Label('How much do you weigh? (in lbs!)',style={'display':'inline-block'}),
        dcc.Slider(
            id = 'Weight',
            min = 55,
            max = 230,
            step = 1,
            value = 130,
            marks = {'55': '55','75':'75','100': '100', '125': '125', '150': '150', '175': '175', '200':'200',
                        '230':'230'}),
         html.Br(),
         html.P('130', id='weight-selected-slider'),

         html.Br(),

        #year
        html.P('Year of Olympics: ',style={'display':'inline-block'}),
        daq.NumericInput(id='Year',
        value = 2000,
        min = 1896,
        max = 2016,
        style={'display':'inline-block'}),
        
        #season
         dcc.Markdown('Season'),
         dcc.Dropdown(
            id = 'Season',
            options = [
                {'label': 'Winter', 'value': 'Winter'},
                {'label': 'Summer', 'value': 'Summer'},
            ],
            className = 'mb-5',
            value = 'Summer',
            placeholder='Select a season'
        

        ),
     
        

    
        

    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Top 5 sports you would most likely medal in!', className='mb-5'), 
        #html.Div(id='prediction-content', className='lead')
        dcc.Graph(id='prediction-content')

    ]
)

layout = dbc.Row([column1, column2])


@app.callback(
    Output(component_id='age-selected-selected', component_property='children'),
    [Input(component_id='Age', component_property='value')]
)
def update_output_div(input_value):
    return 'You are "{}" years old'.format(input_value)

@app.callback(
    Output(component_id='height-selected-selected', component_property='children'),
    [Input(component_id='Height', component_property='value')]
)
def update_output_div(input_value):
    return 'You are "{}" inches tall'.format(input_value)

@app.callback(
    Output(component_id='weight-selected-slider', component_property='children'),
    [Input(component_id='Weight', component_property='value')]
)
def update_output_div(input_value):
    return 'You weigh "{}" pounds'.format(input_value)

@app.callback(
    Output('prediction-content', 'figure'),
    [Input('Sex','value'),
    Input('Age', 'value'),
    Input('Height', 'value'),
    Input('Weight', 'value'),
    Input('Year', 'value'),
    Input('Season','value')],
)
# def predict(gender,age,height,weight,year,season):
#     height_cm = height*2.54
#     weight_kg = weight/2.2
#     df = pd.DataFrame(
#         columns=['Sex', 'Age', 'Height', 'Weight','Year','Season'], 
#         data=[[gender,age,height_cm,weight_kg,year,season]]
#     )
#      y_pred = pipeline.predict(df)[0]
#      return y_pred



def predict(gender,age,height,weight,year,season):
    Height_in = height*2.54
    Weight_lb = weight/2.2
    df = pd.DataFrame(
        columns=['Sex', 'Age', 'Height', 'Weight','Year','Season'], 
        data=[[gender,age,Height_in,Weight_lb,year,season]]
    )
    y_pred = pipeline.predict_proba(df)[0]
    sports = pipeline.classes_
    top_5_idx = np.argsort(y_pred)[-5:]
    top_5_probs = [y_pred[i] for i in top_5_idx]
    top_5_sports = [sports[i] for i in top_5_idx]
    top_5_dict = {top_5_sports[i]: top_5_probs[i] for i in range(len(top_5_sports))}
    output_df = pd.DataFrame.from_dict(top_5_dict, orient = 'index').reset_index()
    output_df.columns = ['Sport','Probability']
    sorted_df = output_df.sort_values(by = 'Probability', ascending = False)
    fig = px.bar(sorted_df, x='Sport', y='Probability')
    
    return fig

