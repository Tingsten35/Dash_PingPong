#tensor([[0.9940, 0.0018, 0.0042]])
import numpy as np

import dash
import dash_daq as daq
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif
from datetime import date, timedelta
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
import os
print(os. getcwd())
diagram01 = np.load("C:/Users/rmercier/OneDrive - AllianTech/Desktop/Thomas git/USB DISK/Matrice1100mediumblanc4.npy")
#diagram02 = np.load("/home/txa/Documents/data/ball-classifier-frontend/result.txt")

diagram02_string = open('C:/Users/rmercier/OneDrive - AllianTech/Desktop/Thomas git/USB DISK/result.txt', 'r').read()
data = diagram02_string.split('\n')
colour_output = data[0].split(';')[:-1]
tensor_data = data[1].split(';')[:-1]
tensor1 = tensor_data[0:3]
tensor3 = tensor_data[3:]
svm_data = data[2].split(';')[:-1]
svm_range = list(range(len(svm_data)))
svm_pred = data[3].split(';')[:-1]



svm_data = list(map(float, svm_data))
svm_pred = list(map(float, svm_pred))


# for each in data:
#     print("NEXT\n", each)
print(colour_output)
print(tensor1)
print(100-int(min(tensor1)))
print(tensor3)
print(svm_data)
print(svm_range)
print(svm_pred)

print(diagram01.shape)
x_current = list(range(600))
print(x_current)
vibration01_graph = go.Figure()

# for each in diagram01:
vibration01_graph.add_trace(go.Scatter(x=x_current, y=diagram01[10],
                            mode='lines',
                            name='THROW: VIBRATION'))

svm_graph = go.Figure()

# for each in diagram01:
svm_graph.add_trace(go.Scatter(x=svm_range, y=svm_data,
                            mode='markers',
                            name='THROW: SVM'))
svm_graph.add_trace(go.Scatter(x=[svm_pred[0]], y=[svm_pred[1]],
                            mode='markers',
                            name='svm_pred'))
# list(svm_pred[0])
app.layout = html.Div([

                dcc.Store(id='current_tensor', data = [0,0]), #ensures rangeslider consistent 
                dcc.Interval(
                        id='interval-component',
                        interval=1*1000, # in milliseconds
                        n_intervals=0
                ),
                # html.Div(id='dark-theme-components', children=[
                #         daq.DarkThemeProvider(theme=theme)
                #     ], style={
                #         'border': 'solid 1px #A2B1C6',
                #         'border-radius': '5px',
                #         'padding': '50px',
                #         'margin-top': '20px'
                #     }),

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H6(children='DTW', id='title_graph01', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                            html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                                                    html.Div([daq.Indicator(
                                                                id='colour_algo01',
                                                                value=True,
                                                                color="#fcfd85",
                                                                size=300),  
                                                        ], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 
                                                    #html.Div([html.Div("☑️ ", id="open01")], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}),  

                                                ]),
                            dcc.RangeSlider(
                                id='algo01-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000]),

                            # daq.Indicator(
                            # id='my-daq-indicator',
                            # value=True,
                            # color="#00cc96"
                            # ),  

                            html.Div(dcc.Graph(
                                id='algo01',
                                figure=vibration01_graph
                            )),


                    ], className= 'four columns'),

                    ]),

                    html.Div([
                        html.Div([
                            html.H6(children='SVM', id='title_graph02', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                            html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                                                    #html.Div([html.Div("☑️ ", id="open02")], style = {'width': '40%', 'display': 'inline-flex', 'align-items': 'right', 'justify-content': 'right'}),  
                                                    html.Div([daq.Indicator(
                                                                id='colour_algo02',
                                                                value=True,
                                                                color="#ff7400",
                                                                size = 300,
                                                                # label = dict(
                                                                #     label= "ORANGE",
                                                                # ),
                                                                #labelPosition = 'bottom',
                                                                ),  
                                                        ], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 

                                                ]),
                            dcc.RangeSlider(
                                id='algo02-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000]),

                            html.Div(dcc.Graph(
                                id='algo02',
                                figure=svm_graph
                            )),


                    ], className= 'four columns'),

                    ]),


                    html.Div([
                        html.Div([
                            html.H6(children='CNN', id='title_graph03', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                            html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                                                    #html.Div([html.Div("☑️ ", id="open03")], style = {'width': '40%', 'display': 'inline-flex', 'align-items': 'right', 'justify-content': 'right'}),  
                                                    html.Div([daq.Indicator(
                                                                id='colour_algo03',
                                                                value=True,
                                                                color="#d9dadc",
                                                                size = 300),  
                                                        ], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 

                                                ]),
                            dcc.RangeSlider(
                                id='algo03-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000]),

                            html.Div(dcc.Graph(
                                id='algo03',
                                figure=vibration01_graph
                            )),


                    ], className= 'four columns'),

                    ])

                ])

            ])

@app.callback(Output('algo02', 'figure'), 
            Output('algo03', 'figure'), 
            Output('colour_algo01', 'label'),
            Output('colour_algo02', 'label'),
            Output('colour_algo03', 'label'),
            Output('colour_algo01', 'color'),
            Output('colour_algo02', 'color'),
            Output('colour_algo03', 'color'),
            Input('interval-component', 'n_intervals'), )
def clean_data(n):

    diagram02_string = open('C:/Users/rmercier/OneDrive - AllianTech/Desktop/Thomas git/USB DISK/result.txt', 'r').read() 
    data = diagram02_string.split('\n')
    colour_output = data[0].split(';')[:-1]
    tensor_data = data[1].split(';')[:-1]
    tensor1 = tensor_data[0:3]
    remi=100-int(min(tensor1))
    print(remi)
    tensor3 = tensor_data[3:]
    svm_data = data[2].split(';')[:-1]
    svm_range = list(range(len(svm_data)))
    svm_pred = data[3].split(';')[:-1]

    colour_output = list(map(int, colour_output))
    svm_data = list(map(float, svm_data))
    svm_pred = list(map(float, svm_pred))

    svm_layout = go.Layout(
        xaxis=dict(range=[-100,100]),
        yaxis=dict(range=[-100,100]),
    )
    svm_graph = go.Figure(layout = svm_layout)

    svm_graph.add_trace(go.Scatter(x=[svm_pred[0]], y=[svm_pred[1]],
                                marker_symbol='x',
                                marker_color='#FF0000',
                                mode='markers',
                                name='svm_pred'))
    # svm_graph.add_trace(daq.Indicator(
    #                                                             id='colour_algo03',
    #                                                             value=True,
    #                                                             color="#d9dadc",
    #                                                             size = 300),
    # ),

    # svm_graph.add_shape(type="circle",
    #     xref="x", yref="y",
    #     x0=1, y0=1, x1=3, y1=3,
    #     line_color="LightSeaGreen",
    # )

    svm_graph.add_annotation(
            x=svm_pred[0],
            y=svm_pred[1],
            xref="x",
            yref="y",
            text="["+str(svm_pred[0])+","+str(svm_pred[1])+"]",
            #showarrow=True,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
                ),
            align="center",
            #arrowhead=2,
            #arrowsize=1,
            #arrowwidth=2,
            #arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#FF0000",
            borderwidth=2,
            borderpad=4,
            bgcolor="#FF0000",
            opacity=0.8
            )

    cnn_graph = go.Figure()

    cnn_graph.add_trace(go.Scatter(x=svm_range, y=svm_data,
                                mode='lines',
                                name='THROW: SVM'))

    cnn_graph.update_traces(marker=dict(size=3),
                        selector=dict(mode='lines'))
    # cnn_graph.add_annotation(x=2, y=5,
    #             text="Text annotation with arrow",
    #             showarrow=True,
    #             arrowhead=1)
    label01 = 'accuracy: '+str(remi)+'%' 
    label02 = 'point: x:'+str(round(svm_pred[0], 2))+', y:'+str(round(svm_pred[1], 2))
    label03 = 'accuracy: '+str(max(tensor3))+'%'                    
    #array is ordered ['orange', 'white', 'yellow']
    colour_array = ['#ff7400', '#d9dadc', '#fcfd85']
    colour_selected01 = colour_array[colour_output[0]]
    colour_selected02 = colour_array[colour_output[1]]
    colour_selected03 = colour_array[colour_output[2]]

    return svm_graph, cnn_graph, label01, label02, label03, colour_selected01, colour_selected02, colour_selected03

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')


