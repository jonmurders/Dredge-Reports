import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

#Load Data from CSV
master = pd.read_csv('19122000.csv')
master.Time = pd.to_datetime(master.Time, format = '%H:%M:%S')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Dredge Data
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")
trace_density = go.Scatter(x=master.Time, y=master.DENSITY,name='Density')
trace_dischpr = go.Scatter(x=master.Time, y=master.DISCHPR, name='Discharge Pressure')
trace_swingspd = go.Scatter(x=master.Time, y=master.SWINGSPD, name='Swing Speed')
trace_swingradius = go.Scatter(x=master.Time, y=master.SWINGRADIUS, name='Swing Radius')
trace_cdbw = go.Scatter(x=master.Time, y=master.CDBW, name='Cutter Depth Below Water')
trace_mdbw = go.Scatter(x=master.Time, y=master.MDBW, name='Max Depth Below Water')
trace_configuration = go.Scatter(x=master.Time, y=master.CONFIGURATION, name='Configuration')
data = [trace_velocity,trace_density,trace_dischpr,trace_swingspd,trace_swingradius,trace_cdbw,trace_mdbw,trace_configuration]

#Pump 1 Data
trace_p1intake = go.Scatter(x=master['Time'], y=master['P1INTAKE'],name="Intake Pressure")
trace_p1discharge = go.Scatter(x=master['Time'], y=master['P1DISCH'],name="Discharge Pressure")
trace_p1hp = go.Scatter(x=master['Time'], y=master['P1HP'],name="Horsepower")
trace_p1hplimit = go.Scatter(x=master['Time'], y=master['P1HPLIMIT'],name="Horsepower Limit")
trace_p1gear = go.Scatter(x=master['Time'], y=master['P1GEAR'],name="Gear")
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")
trace_velocity = go.Scatter(x=master['Time'], y=master['VELOCITY'],name="Velocity")

pump1data = [trace_p1intake,trace_p1discharge,trace_p1hp,trace_p1hplimit,trace_p1gear]

#Pump 2 data
trace_p2intake = go.Scatter(x=master['Time'], y=master['P2INTAKE'],name="Intake Pressure")
trace_p2discharge = go.Scatter(x=master['Time'], y=master['P2DISCH'],name="Discharge Pressure")
trace_p2hp = go.Scatter(x=master['Time'], y=master['P2HP'],name="Horsepower")
trace_p2hplimit = go.Scatter(x=master['Time'], y=master['P2HPLIMIT'],name="Horsepower Limit")
trace_p2gear = go.Scatter(x=master['Time'], y=master['P2GEAR'],name="Gear")

pump2data = [trace_p2intake,trace_p2discharge,trace_p2hp,trace_p2hplimit,trace_p2gear]



layout = dict(showlegend=True)

dredgegraph = dict(data=data,layout=layout)
pump1graph = dict(data = pump1data, layout=layout)
pump2graph = dict(data = pump2data, layout=layout)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def dredge_stats():
    return html.Div(
        id = 'dredgestats',
        className = 'dredgestats',
        children = [
            html.H3(children = 'Dredge Stats'),
            dcc.Graph(id = 'dredge-graph',figure = dredgegraph),
        ]
    )
def pumpone_stats():
    return html.Div(
        id = 'pump1stats',
        className = 'six columns',
        children = [
            html.H3(children = 'Pump 1 Stats'),
            dcc.Graph(id = 'pump1-graph', figure = pump1graph)
        ],
    )
def pumptwo_stats():
    return html.Div(
        id = 'pump2stats',
        className = 'six columns',
        children = [
            html.H3(children = 'Pump 2 Stats'),
            dcc.Graph(id = 'pump2-graph', figure = pump2graph)
        ],
    )
def build_tabs():
    return html.Div(
        id = 'tabs',
        className = 'tabs',
        children = [
            dcc.Tabs(
                id='app-tabs',
                value = 'tab3',
                className = 'custom-tabs',
                children = [
                    dcc.Tab(
                        id='Overview',
                        label = 'Overview',
                        value = 'tab1',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id='dredgeview',
                        label = 'Dredge',
                        value = 'tab2',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id='pumpview',
                        label = 'Pumps',
                        value = 'tab3',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                ],
            )
        ],
    )
def build_overview_tab():
    return html.Div(
        id = 'Overview-Container',
        className = 'twelve columns',
        children = [
            dredge_stats(),
            html.Div(
                id ='Pumps',
                className = 'row',
                children = [
                    pumpone_stats(),
                    pumptwo_stats()

                    ],
                ),
            ]

    )

app.layout = html.Div(
    id='Main Container',
    children = [

        html.H1(children = 'Dredge Dashboard'),
        build_tabs(),
        build_overview_tab(),
        # dredge_stats(),
        # html.Div(
        #     id ='Pumps',
        #     className = 'row',
        #     children = [
        #         pumpone_stats(),
        #         pumptwo_stats(),
        #     ],
        # )





        ])
if __name__ == '__main__':
    app.run_server(debug=True)
