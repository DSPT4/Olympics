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
            Colorado Springs is not only my home but also home to the Olympic and Paralympic Committee Headquarters. In the latest build week in my Data Science program, 
            I chose to work with Olympic data for our machine learning project. As a professional athlete myself, Colorado Springs is perfect for training. I also have a 
            personal passion for hearing the background of athletes' lives and love watching the games themselves.
            
            ## Process

            My data exploration was fairly straight forward.  As it was fairly clean.  I decided to drop all athletes that didn't medal in the Olympics. I was orginally 
            going to try and predict which counties would have the most medals in 2020, but with where I am in my ability and talking to experts, this would have been
            fairly difficult.  Therefore, I decided to predict which sport one would most likely medal in based on their own stats.  

            I went down a few rabbit holes with some feature engineering, that in the end I ended up not even using.  After cleaning up the data, mainly reducing my Sport 
            features cardinality (cardinality refers to the uniqueness of data values contained in a column) to 40 from 65 and getting the columns I needed, I 
            was ready to split my data. I used a 3 way split - train, val and test.  Here is an example of my target 'Sport' based on one feature 'Age'. 

            """
            ),
             html.Img(src='assets/sports_based_on_age.png', 
                 className='sport_age', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
            
            ), 
            
        dcc.Markdown(
            """
            ## Machine Learning

            I did a logistic model as my majority base classifier since this is a multi-classification problem. My training accuracy was only 17%.  This means that 
            without doing any machine learning on my model, it would only guess correctly 17% of the time.  For my machine learning models, I tried both Random Forest Classifer
            and an XGboost model.  I ended up using the Random Forest for my final pipeline as it produced slightly better results.  
            ```
            {
                final_pipeline = make_pipeline(
                    ce.OrdinalEncoder(), 
                    RandomForestClassifier(n_estimators=100, 
                                           max_features='auto', random_state=42, 
                                           n_jobs=-1)
                )
                # Fit on train, score on val
                final_pipeline.fit(X_train, y_train)
                print('Validation Accuracy', final_pipeline.score(X_val, y_val))
            }
            ```
            """
            ),
            
        dcc.Markdown(
            """
            Below are the permutation importance of the features. Or bagging, which is used for Random Forests.  The most important feature in my model was weight.  This makes sense
            because a weightlifter, for example, will be way heavier than an athlete such as cycling who will be leaner. It's interesting that sex is the least
            important feature.   

            """

            ),
             html.Img(src='assets/permutaion_importance.png', 
                 className='permutaion_importance', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '40%'}

             ),
        dcc.Markdown(
            """
            Gradient Boosting, which is used for xgboost.  Below is the graph, though it is slightly less interruptible than the 
            bagging of random forest above.



            """
        ),   

          html.Img(src='assets/xgboost.png', 
                 className='xgboost', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '40%'}
          ),
    dcc.Markdown(
            """        
            ## Results

            For the Random Forest Classifier, my accuracy ending up being 42%! Still not the best score, but it did increase from my base by 25%. 
            So what this means, is my final model can now correctly identify which sport you would most likely medal in 42% of the time. With 40 sports, 
            or classes to choose from, I'd say this is pretty darn good. 

            Xgboost my model only had a 36% accuracy. 

            To gain further insights into how the different features impacted my predictions, I created
            Shapley values on two examples:
            * A Cyclist - 
            """
            ),
            html.Img(src='assets/shap_cyclist.png', 
                 className='cyclist', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'} 
            ),
    dcc.Markdown(
            """
            * An Ice Hockey Player -
            
            """
    
            ),
            html.Img(src='assets/shap_IceHockey.png', 
                 className='IceHockey', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
            ), 
    dcc.Markdown(
            """
            Each example interacts differently. For the first example: season, year and weight helped the probability for the cyclist.
            But for the Ice Hockey player, only height helped. And the season, year, age and weight lowered it. 
            """    
    ),
     dcc.Markdown(
            """
            Here is my full [Github notebook](https://github.com/AmyBeisel/Olympics-Data/blob/master/notebooks/LS_DS_231_assignment_AMY_BEISEL.ipynb), 
            if you want to dig deeper. Thank you! 
            """

     ),    
    ],
)

layout = dbc.Row([column1])