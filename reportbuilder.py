import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import pyodbc


#SQL Connection
server = 'HMA-S-003'
database = 'DredgeData'
userid = 'redlion'
passwd = 'Weeks123!'
table = 'test'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+userid+';PWD='+passwd+'; Trusted_Connection=yes')
query = "SELECT * FROM "+table+";"
master = pd.read_sql(query, cnxn)
master.to_csv()

port = 8050
title = 'Office Test'

#Load Data from CSV
#master = pd.read_csv('19122000.csv')

#formating data
master.Time = pd.to_datetime(master.Time, format = '%H:%M:%S').dt.time
master.Date = pd.to_datetime(master.Date, format = '%Y/%m/%d')
master.Time = master.apply(lambda master : pd.datetime.combine(master['Date'],master['Time']),1)
dredgemaster = master[['Time','VELOCITY','DENSITY','DISCHPR','SWINGSPD','SWINGRADIUS','CDBW','MDBW','CONFIGURATION',]]



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

trace_cuttertorque = go.Scatter(x=master['Time'], y=master['CUTTERT'],name="Cutter Torque (ft/lbs)")
trace_cuttertorquelimit = go.Scatter(x=master['Time'], y=master['CUTTERTLIM'],name="Cutter Torque Limit (%)")
trace_cutterrpm = go.Scatter(x=master['Time'], y=master['CUTTERRPM'],name="Cutter RPM")
trace_cutterrpmsp = go.Scatter(x=master['Time'], y=master['CUTTERRPMSP'],name="Cutter RPM Set Point")

cutterdata = [trace_cuttertorque,trace_cuttertorquelimit,trace_cutterrpm,trace_cutterrpmsp]

comparisondata = [trace_velocity,trace_density,trace_dischpr,trace_swingspd,trace_swingradius,trace_cdbw,trace_mdbw,trace_configuration,
                    trace_p1intake,trace_p1discharge,trace_p1hp,trace_p1hplimit,trace_p1gear,
                    trace_p2intake,trace_p2discharge,trace_p2hp,trace_p2hplimit,trace_p2gear,
                    trace_cuttertorque,trace_cuttertorquelimit,trace_cutterrpm,trace_cutterrpmsp,
    ]

layout = dict(showlegend=True)

dredgegraph = dict(data=data,layout=layout)
pump1graph = dict(data = pump1data, layout=layout)
pump2graph = dict(data = pump2data, layout=layout)
cuttergraph = dict(data = cutterdata, layout = layout,)
comparisongraph = dict(data = comparisondata, layout = layout)
#Loading Style Sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

def dredge_stats():
    return html.Div(
        id = 'dredgestats',
        className = 'dredgestats',
        children = [
            html.H3(children = 'Dredge Stats'),
            dcc.Graph(id = 'dredge-graph',figure = dredgegraph),
        ]
    )
def dredge_table():
    return dash_table.DataTable(
        id = 'dredgetable',
        columns=[{"name": i, "id": i} for i in dredgemaster.columns],
        data = dredgemaster.to_dict('records'),
        sort_action = 'custom',
        sort_mode = 'multi',
        sort_by=[]
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
def cutter_stats(width):
    return html.Div(
        id = 'cutterstats',
        className = width,
        children = [
            html.H3(children = 'Cutter Stats'),
            dcc.Graph(id = 'cutter-graph', figure = cuttergraph)
            ],
    )
def comparison_stats():
    return html.Div(
    id = 'comparisonstats',
    #classname = 'twelve columns',
    children = [
        html.H3(children = 'Comparison'),
        dcc.Graph(id = 'comparison-graph', figure = comparisongraph)
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
                    dcc.Tab(
                        id = 'comparison',
                        label = 'Comparison',
                        value = 'comparison',
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
            # dash_table.DataTable(
            #     id = 'dredgetable',
            #     columns=[{"name": i, "id": i} for i in dredgemaster.columns],
            #     data = dredgemaster.to_dict('records'),
            #     sort_action = 'custom',
            #     sort_mode = 'multi',
            #     sort_by=[],
            # )
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
            cutter_stats('twelve columns')
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
def build_comparison_tab():
    return html.Div(
        id = 'Comparison-Container',
        className = 'twelve columns',
        children = [
            comparison_stats()
        ],
    )
app.layout = html.Div(
    id='Main Container',
    children = [

        html.H1(children = title+'Dredge Dashboard'),
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
    elif tab == 'comparison':
        return build_comparison_tab()
# @app.callback(
#     Output('dredgetable','data'),
#     [Input('dredgetable','page_current'),
#     Input('dredgetable', 'sort_by')]
# )
#
# def update_dredgetable():
#     print(sort_by)
#     if len(sort_by):
#         dff = dredgemaster.sort_values(
#             [col['column_id'] for col in sort_by],
#             ascending=[
#                 col['direction'] == 'asc'
#                 for col in sort_by
#             ],
#             inplace=False
#         )
#     else:
#         # No sort is applied
#         dff = dredgemaster

if __name__ == '__main__':

    #HMA Server IP: 10.0.0.11
    app.run_server(debug=False, host = '10.0.0.11', port=port)
