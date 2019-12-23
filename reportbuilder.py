import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
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
def pumpone_stats(width):
    return html.Div(
        id = 'pump1stats',
        className = width,
        children = [
            html.H3(children = 'Pump 1 Stats'),
            dcc.Graph(id = 'pump1-graph', figure = pump1graph)
        ],
    )
def pumptwo_stats(width):
    return html.Div(
        id = 'pump2stats',
        className = width,
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
                value = 'overview',
                className = 'custom-tabs',
                children = [
                    dcc.Tab(
                        id='Overview',
                        label = 'Overview',
                        value = 'overview',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id='dredgeview',
                        label = 'Dredge',
                        value = 'dredge',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id='pumpview',
                        label = 'Pumps',
                        value = 'pumps',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'cutterview',
                        label = 'Cutter',
                        value = 'cutter',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'swingview',
                        label = 'Swing Hoist',
                        value = 'swing',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'ladderview',
                        label = 'Ladder Hoist',
                        value = 'ladder',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'spudview',
                        label = 'Spuds',
                        value = 'spuds',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'positionview',
                        label = 'Positions and Angles',
                        value = 'positions',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'srvview',
                        label = 'SRV',
                        value = 'srv',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'genview',
                        label = 'Generators',
                        value = 'gens',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected',
                    ),
                    dcc.Tab(
                        id = 'boosters',
                        label = 'Boosters',
                        value = 'boosters',
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
                    pumpone_stats('six columns'),
                    pumptwo_stats('six columns'),

                    ],
                ),
            ]

    )

def build_dredge_tab():
    return html.Div(
        id = 'Dredge-Container',
        className = 'twelve columns',
        children = [
            dredge_stats(),
        ]
    )

def build_pumps_tab():
    return html.Div(
        id ='Pumps-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_cutter_tab():
    return html.Div(
        id ='Cutter-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_swing_tab():
    return html.Div(
        id ='Swing-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_ladder_tab():
    return html.Div(
        id ='Ladder-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_spuds_tab():
    return html.Div(
        id ='Spuds-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_positions_tab():
    return html.Div(
        id ='Positions-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_srv_tab():
    return html.Div(
        id ='SRV-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_generators_tab():
    return html.Div(
        id ='Generators-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

def build_boosters_tab():
    return html.Div(
        id ='Boosters-Container',
        className = 'twelve columns',
        children = [
            pumpone_stats('twelve columns'),
            pumptwo_stats('twelve columns'),
        ]
    )

app.layout = html.Div(
    id='Main Container',
    children = [

        html.H1(children = 'Dredge Dashboard'),
        build_tabs(),
        html.Div(id='app-content'),
        ]
)
@app.callback(
    Output('app-content','children'),
    [Input('app-tabs','value')])

def render_tabs(tab):
    if tab == 'overview':
        return build_overview_tab()
    elif tab == 'dredge':
        return build_dredge_tab()
    elif tab == 'pumps':
        return build_pumps_tab()
    elif tab == 'cutter':
        return build_cutter_tab()
    elif tab == 'swing':
        return build_swing_tab()
    elif tab == 'ladder':
        return build_ladder_tab()
    elif tab == 'spuds':
        return build_spuds_tab()
    elif tab == 'positions':
        return build_positions_tab()
    elif tab == 'srv':
        return build_srv_tab()
    elif tab == 'gens':
        return build_generators_tab()
    elif tab == 'boosters':
        return build_boosters_tab()



if __name__ == '__main__':
    app.run_server(debug=True)
