# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Olympics Data

            I've always enjoyed watching the olympics.  As an athlete myself, I tried going in 2016 for the mountain biking event.  Chasing UCI 
            points like my life depended on it.  I fell short and was not put on the long list. Out of the 8 that were allowed, according to 
            my coach at the time, said I was 9th.  Out of that 8, 2 were then picked to go.  It is all very political.  I did my best and although
            wasn't even allowed to go, I absolutly loved the process.

            The data set I used is from kaggle.com and was 120 years of Olympic History: athletes and results. Here are the first five rows and the shape
            of the data frame. 
            
            """
        ),
        html.Img(src='assets/head_and_shape.png', 
                 className='head_and_shape', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
                 
        ),
        dcc.Markdown(
            """
            # Some fun facts
            As I was doing some data exploration, here are some facts I learned.

            1.  Summer 1896 was the first-ever Olympics.  Although the ancient Games were staged in Olympia, Greece, 
                from 776 BC through 393 AD, it took 1503 years for the Olympics to return.  
            2.  Winter Olympics didn't come about until 1928, 32 years later. 
            3.  Both Summer and Winter were held in the same year until 1992.
            4.  1916, 1940 and 1944 were canceled.  After doing some research it was during wars. WWI and WWII.
            
            """ 
        ),
        html.Img(src='assets/Games(sort_values_and_unique).png', 
                 className='Games', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}

        ),
        dcc.Markdown(
            """
            5. . Art competitions used to be part of the Olympics? That is crazy. This is cool to know. I actually ended up dropping this 'Sport', 
            as most didn't have much information
            6. Over the 120 years, only 35 of those were Olympic years. 
            7. Although the Olympics have been around for 120 years, because they only happen every 2-4 years, there has only been 51 games total.
             
            """
        ),
        html.Img(src='assets/Art_Comp.png', 
                 className='Art Competition', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
        ),
        html.Img(src='assets/Year_and_games.png', 
                 className='year and games', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
                
        ),
    



    ],
)

layout = dbc.Row([column1])