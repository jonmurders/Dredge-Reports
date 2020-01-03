import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import pyodbc
from waitress import serve

#clear database
master = pd.DataFrame([])
#SQL Connection
server = 'HMA-S-003'
database = 'DredgeData'
userid = 'redlion'
passwd = 'Weeks123!'
table = 'EWE_300_MAIN'
cnxn_string ='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+userid+';PWD='+passwd+'; Trusted_Connection=yes'
cnxn = pyodbc.connect(cnxn_string)
query = "SELECT * FROM "+table+" ORDER BY DateTime;"
master = pd.read_sql(query, cnxn)

port = 8050
title = 'Office Test'


# master = pd.read_csv('19122600.csv')
#formating data
# master.Time = pd.to_datetime(master.Time, format = '%H:%M:%S').dt.time
# master.Date = pd.to_datetime(master.Date, format = '%Y/%m/%d')
# master.Time = master.apply(lambda master : pd.datetime.combine(master['Date'],master['Time']),1)
# master.sort_values(by='Time')
master.dropna(axis=0)

instantdata = pd.DataFrame(data = master.iloc[-1])
print(instantdata.head(10))
overviewdata = pd.concat([instantdata,instantdata,instantdata,instantdata,instantdata,instantdata,instantdata,], axis=1)



#Dredge Data
dredge_table_data = master[['DateTime','VELOCITY','DENSITY','DISCHPR','SWINGSPD','SWINGRADIUS','CDBW','MDBW','CONFIGURATION',]]
trace_velocity = go.Scatter(x=master['DateTime'], y=master['VELOCITY'],name="Velocity (fps)")
trace_density = go.Scatter(x=master.DateTime, y=master.DENSITY,name='Density (SGU)')
trace_dischpr = go.Scatter(x=master.DateTime, y=master.DISCHPR, name='Discharge Pressure (psig)')
trace_swingspd = go.Scatter(x=master.DateTime, y=master.SWINGSPD, name='Swing Speed (fpm)')
trace_swingradius = go.Scatter(x=master.DateTime, y=master.SWINGRADIUS, name='Swing Radius (ft)')
trace_cdbw = go.Scatter(x=master.DateTime, y=master.CDBW, name='Cutter Depth Below Water (ft)')
trace_mdbw = go.Scatter(x=master.DateTime, y=master.MDBW, name='Max Depth Below Water (ft)')
#trace_configuration = go.Scatter(x=master.DateTime, y=master.CONFIGURATION, name='Configuration')
data = [trace_velocity,trace_density,trace_dischpr,trace_swingspd,trace_swingradius,trace_cdbw,trace_mdbw,]

#Pump 1 Data
pumpone_table_data = master[['DateTime','P1INTAKE','P1DISCH','P1HP','P1HPLIMIT','P1GEAR',]]
trace_p1intake = go.Scatter(x=master['DateTime'], y=master['P1INTAKE'],name="Intake Pressure (psig)")
trace_p1discharge = go.Scatter(x=master['DateTime'], y=master['P1DISCH'],name="Discharge Pressure (psig)")
trace_p1hp = go.Scatter(x=master['DateTime'], y=master['P1HP'],name="Horsepower")
trace_p1hplimit = go.Scatter(x=master['DateTime'], y=master['P1HPLIMIT'],name="Horsepower Limit")
trace_p1gear = go.Scatter(x=master['DateTime'], y=master['P1GEAR'],name="Gear Ratio")
trace_p1engrpm = go.Scatter(x=master['DateTime'], y=master['P1ENGRPM'],name="Engine RPM")
trace_p1rpmsp = go.Scatter(x=master['DateTime'], y=master['P1RPMSP'],name="Engine RPM Set Point")
trace_p1fcsp = go.Scatter(x=master['DateTime'], y=master['P1FCSP'],name="Flow Control Set Point (fpm)")
trace_p1spcsp = go.Scatter(x=master['DateTime'], y=master['P1PCSP'],name="Suction Pressure Control Set Point (psig)")
trace_p1dpcsp = go.Scatter(x=master['DateTime'], y=master['P1DPCSP'],name="Discharge Pressure Control Set Point (psig)")
trace_p1smsp = go.Scatter(x=master['DateTime'], y=master['VELOCITY'],name="Speed Match Control Bias Set Point (RPM)")

pump1data = [trace_p1intake,trace_p1discharge,trace_p1hp,trace_p1hplimit,trace_p1gear,trace_p1engrpm,trace_p1rpmsp,trace_p1fcsp,trace_p1dpcsp,trace_p1smsp]

#Pump 2 Data
pumpone_table_data = master[['DateTime','P2INTAKE','P2DISCH','P2HP','P2HPLIMIT','P2GEAR',]]
trace_p2intake = go.Scatter(x=master['DateTime'], y=master['P2INTAKE'],name="Intake Pressure (psig)")
trace_p2discharge = go.Scatter(x=master['DateTime'], y=master['P2DISCH'],name="Discharge Pressure (psig)")
trace_p2hp = go.Scatter(x=master['DateTime'], y=master['P2HP'],name="Horsepower")
trace_p2hplimit = go.Scatter(x=master['DateTime'], y=master['P2HPLIMIT'],name="Horsepower Limit")
trace_p2gear = go.Scatter(x=master['DateTime'], y=master['P2GEAR'],name="Gear Ratio")
trace_p2engrpm = go.Scatter(x=master['DateTime'], y=master['P2ENGRPM'],name="Engine RPM")
trace_p2rpmsp = go.Scatter(x=master['DateTime'], y=master['P2RPMSP'],name="Engine RPM Set Point")
trace_p2fcsp = go.Scatter(x=master['DateTime'], y=master['P2FCSP'],name="Flow Control Set Point (fpm)")
# trace_p2spcsp = go.Scatter(x=master['DateTime'], y=master['P2SPCSP'],name="Suction Pressure Control Set Point (psig)")
trace_p2dpcsp = go.Scatter(x=master['DateTime'], y=master['P2DPCSP'],name="Discharge Pressure Control Set Point (psig)")
trace_p2smsp = go.Scatter(x=master['DateTime'], y=master['VELOCITY'],name="Speed Match Control Bias Set Point (RPM)")

pump2data = [trace_p2intake,trace_p2discharge,trace_p2hp,trace_p2hplimit,trace_p2gear,trace_p2engrpm,trace_p2rpmsp,trace_p2fcsp,trace_p2dpcsp,trace_p2smsp]

#Cutter Data

trace_cuttertorque = go.Scatter(x=master['DateTime'], y=master['CUTTERT'],name="Cutter Torque (k-ft/lbs)")
trace_cuttertorquelimit = go.Scatter(x=master['DateTime'], y=master['CUTTERTLIM'],name="Cutter Torque Limit (%)")
trace_cutterrpm = go.Scatter(x=master['DateTime'], y=master['CUTTERRPM'],name="Cutter RPM")
trace_cutterrpmsp = go.Scatter(x=master['DateTime'], y=master['CUTTERRPMSP'],name="Cutter RPM Set Point")

cutterdata = [trace_cuttertorque,trace_cuttertorquelimit,trace_cutterrpm,trace_cutterrpmsp]

#Port Swing Hoist Data
trace_pswinglp = go.Scatter(x=master['DateTime'], y=master['PSWINGLP'],name="Line Pull (k-ft/lbs)")
trace_pswinglplim = go.Scatter(x=master['DateTime'], y=master['PSWINGLPLIM'],name="Line Pull Limit (ft/lbs)")
trace_pswingdrumdia = go.Scatter(x=master['DateTime'], y=master['PSWINGDRUMDIA'],name="Drum Diameter Factor)")
trace_pswingls = go.Scatter(x=master['DateTime'], y=master['PSWINGLS'],name="Hoist Line Speed (fpm)")
trace_pswinglssp = go.Scatter(x=master['DateTime'], y=master['PSWINGLSSP'],name="Hoist Line Speed Set Point (fpm)")

portswingdata = [trace_pswinglp,trace_pswinglplim,trace_pswingdrumdia,trace_pswingls,trace_pswinglssp,]

#Stbd Swing Hoist Data
trace_sswinglp = go.Scatter(x=master['DateTime'], y=master['SSWINGLP'],name="Line Pull (k-ft/lbs)")
trace_sswinglplim = go.Scatter(x=master['DateTime'], y=master['SSWINGLPLIM'],name="Line Pull Limit (ft/lbs)")
trace_sswingdrumdia = go.Scatter(x=master['DateTime'], y=master['SSWINGDRUMDIA'],name="Drum Diameter Factor)")
trace_sswingls = go.Scatter(x=master['DateTime'], y=master['SSWINGLS'],name="Hoist Line Speed (fpm)")
trace_sswinglssp = go.Scatter(x=master['DateTime'], y=master['SSWINGLSSP'],name="Hoist Line Speed Set Point (fpm)")

stbdswingdata = [trace_sswinglp,trace_sswinglplim,trace_sswingdrumdia,trace_sswingls,trace_sswinglssp,]

#Port Ladder Hoist Data
trace_pladderlp = go.Scatter(x=master['DateTime'], y=master['PLADDERLP'],name="Line Pull (k-ft/lbs)")
trace_pladderlplim = go.Scatter(x=master['DateTime'], y=master['PLADDERLPLIM'],name="Line Pull Limit (ft/lbs)")
trace_pladderls = go.Scatter(x=master['DateTime'], y=master['PLADDERLS'],name="Hoist Line Speed (fpm)")
trace_pladderlssp = go.Scatter(x=master['DateTime'], y=master['PLADDERLSSP'],name="Hoist Line Speed Set Point (fpm)")

portladderdata = [trace_pladderlp,trace_pladderlplim,trace_pladderls,trace_pladderlssp,]

#Stbd Ladder Hoist Data
trace_sladderlp = go.Scatter(x=master['DateTime'], y=master['SLADDERLP'],name="Line Pull (k-ft/lbs)")
trace_sladderlplim = go.Scatter(x=master['DateTime'], y=master['SLADDERLPLIM'],name="Line Pull Limit (ft/lbs)")
trace_sladderls = go.Scatter(x=master['DateTime'], y=master['SLADDERLS'],name="Hoist Line Speed (fpm)")
trace_sladderlssp = go.Scatter(x=master['DateTime'], y=master['SLADDERLSSP'],name="Hoist Line Speed Set Point (fpm)")

stbdladderdata = [trace_sladderlp,trace_sladderlplim,trace_sladderls,trace_sladderlssp,]

#Main Spud Data
trace_spmain_xs_lp = go.Scatter(x=master['DateTime'], y=master['SPUDMAINXS_LP'],name="Main Spud or Stern Christmas Tree Winch Line Pull (k-ft/lbs)")
trace_spudmainlplim = go.Scatter(x=master['DateTime'], y=master['SPMAINLPLIM'],name="Main Spud or Stern Christmas Tree Winch Line Pull Limit (ft/lbs)")
trace_spudmainls = go.Scatter(x=master['DateTime'], y=master['SPMAINLS'],name="Main Spud or Stern Christmas Tree Winch Line Speed (fpm)")
trace_spudmainlssp = go.Scatter(x=master['DateTime'], y=master['SPMAINLSSP'],name="Main Spud or Stern Christmas Tree Winch Line Speed Set Point (fpm)")
trace_spudmainpos = go.Scatter(x=master['DateTime'], y=master['SPMAINPOS'],name="Main Spud Position or Stern Christmas Tree Line Length (ft)")

spudmaindata = [trace_spmain_xs_lp,trace_spudmainlplim,trace_spudmainls,trace_spudmainlssp,trace_spudmainpos]

#Aux Spud Data
trace_spaux_xs_lp = go.Scatter(x=master['DateTime'], y=master['SPUDAUXLP'],name="Aux Spud or Port Christmas Tree Winch Line Pull (k-ft/lbs)")
trace_spudauxlplim = go.Scatter(x=master['DateTime'], y=master['SPUDAUXLPLIM'],name="Aux Spud or Port Christmas Tree Winch Line Pull Limit (ft/lbs)")
trace_spudauxls = go.Scatter(x=master['DateTime'], y=master['SPUDAUXLS'],name="Aux Spud or Port Christmas Tree Winch Line Speed (fpm)")
trace_spudauxlssp = go.Scatter(x=master['DateTime'], y=master['SPUDAUXLSSP'],name="Aux Spud or Port Christmas Tree Winch Line Speed Set Point (fpm)")
trace_spudauxpos = go.Scatter(x=master['DateTime'], y=master['SPUDAUXPOS'],name="Aux Spud Position or Port Christmas Tree Line Length (ft)")

spudauxdata = [trace_spaux_xs_lp,trace_spudauxlplim,trace_spudauxls,trace_spudauxlssp,trace_spudauxpos]

#Spud Carriage Data
trace_spcar_xs_lp = go.Scatter(x=master['DateTime'], y=master['SPUDCARLP'],name="Spud Carriage or Stbd Christmas Tree Winch Line Pull (k-ft/lbs)")
trace_spudcarlplim = go.Scatter(x=master['DateTime'], y=master['SPUDCARLPLIM'],name="Spud Carriage or Stbd Christmas Tree Winch Line Pull Limit (ft/lbs)")
trace_spudcarls = go.Scatter(x=master['DateTime'], y=master['SPUDCARLS'],name="Spud Carriage or Stbd Christmas Tree Winch Line Speed (fpm)")
trace_spudcarlssp = go.Scatter(x=master['DateTime'], y=master['SPUDCARLSSP'],name="Spud Carriage or Stbd Christmas Tree Winch Line Speed Set Point (fpm)")
trace_spudcarpos = go.Scatter(x=master['DateTime'], y=master['SPUDCARPOS'],name="Spud Carriage Position or Stbd Christmas Tree Line Length (ft)")

spudcardata = [trace_spcar_xs_lp,trace_spudcarlplim,trace_spudcarls,trace_spudcarlssp,trace_spudcarpos]



comparisondata = [trace_velocity,trace_density,trace_dischpr,trace_swingspd,trace_swingradius,trace_cdbw,trace_mdbw,
                    trace_p1intake,trace_p1discharge,trace_p1hp,trace_p1hplimit,trace_p1gear,
                    trace_p2intake,trace_p2discharge,trace_p2hp,trace_p2hplimit,trace_p2gear,
                    trace_cuttertorque,trace_cuttertorquelimit,trace_cutterrpm,trace_cutterrpmsp,
                    trace_pswinglp,trace_pswinglplim,trace_pswingdrumdia,trace_pswingls,trace_pswinglssp,
                    trace_sswinglp,trace_sswinglplim,trace_sswingdrumdia,trace_sswingls,trace_sswinglssp,
    ]

layout = dict(showlegend=True)

dredgegraph = dict(data=data,layout=layout)
pump1graph = dict(data = pump1data, layout=layout)
pump2graph = dict(data = pump2data, layout=layout)
cuttergraph = dict(data = cutterdata, layout = layout,)
portswinggraph = dict(data = portswingdata, layout = layout,)
stbdswinggraph = dict(data = stbdswingdata, layout = layout,)
portladdergraph = dict(data = portladderdata, layout = layout,)
stbdladdergraph = dict(data = stbdladderdata, layout = layout,)
spudmaingraph = dict(data = spudmaindata, layout = layout,)
spudauxgraph = dict(data = spudauxdata, layout = layout,)
spudcargraph = dict(data = spudcardata, layout = layout,)
comparisongraph = dict(data = comparisondata, layout = layout)
#Loading Style Sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets,)

server = app.server

def overview_table_block1():
    return dash_table.DataTable(
        id = 'overview-table',
        columns = ['Instant','0:00-6:00','6:00-12:00','12:00-18:00','18:00-24:00','Today','Yearly'],
        data = overviewdata.to_dict('records'),

    )


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

def pumpone_table():
    return dash_table.DataTable(
        id= 'pumpone-tab-table',
        className = 'six columns',
        columns = [{"name": i, "id": i} for i in pumpone_table_data.columns],
        data = pumpone_table_data.to_dict("rows"),
        sort_action = 'native',
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

def portswing_stats(width):
    return html.Div(
        id = 'pswingstats',
        className = width,
        children = [
            html.H3(children = 'Port Swing Hoist Stats'),
            dcc.Graph(id = 'pswing-graph', figure = portswinggraph)
            ],
    )

def stbdswing_stats(width):
    return html.Div(
        id = 'sswingstats',
        className = width,
        children = [
            html.H3(children = 'Stbd. Swing Hoist Stats'),
            dcc.Graph(id = 'sswing-graph', figure = stbdswinggraph)
            ],
    )

def portladder_stats(width):
    return html.Div(
        id = 'pladderstats',
        className = width,
        children = [
            html.H3(children = 'Port Ladder Hoist Stats'),
            dcc.Graph(id = 'pladder-graph', figure = portladdergraph)
            ],
    )

def stbdladder_stats(width):
    return html.Div(
        id = 'sladderstats',
        className = width,
        children = [
            html.H3(children = 'Stbd. Ladder Hoist Stats'),
            dcc.Graph(id = 'sladder-graph', figure = stbdladdergraph)
            ],
    )

def spudaux_stats(width):
    return html.Div(
        id = 'spudauxstats',
        className = width,
        children = [
            html.H3(children = 'Auxillary Spud and Port Christmas Tree Winch Stats'),
            dcc.Graph(id = 'pladder-graph', figure = spudauxgraph)
            ],
    )

def spudmain_stats(width):
    return html.Div(
        id = 'spudmainstats',
        className = width,
        children = [
            html.H3(children = 'Main Spud and Stern Christmas Tree Winch Stats'),
            dcc.Graph(id = 'spudmain-graph', figure = spudmaingraph)
            ],
    )

def spudcar_stats(width):
    return html.Div(
        id = 'spudcarstats',
        className = width,
        children = [
            html.H3(children = 'Spud Carriage and Stbd. Christmas Tree Winch Stats'),
            dcc.Graph(id = 'spudcar-graph', figure = spudcargraph)
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
            #overview_table_block1(),
            html.H1("Table Goes Here")
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
            # html.Div(
            # id = 'pumpone-stats-containers',
            # className = 'row',
            # children = [
            #         pumpone_stats('six columns'),
            #         html.Div(
            #             id = 'pumpone-table-container',
            #             className = 'sixcolumns',
            #             children = pumpone_table(),
            #         ),
            #
            # ],
            # ),
            pumpone_stats('six columns'),
            pumptwo_stats('six columns'),
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
            portswing_stats('twelve columns'),
            stbdswing_stats('twelve columns'),
        ]
    )

def build_ladder_tab():
    return html.Div(
        id ='Ladder-Container',
        className = 'twelve columns',
        children = [
            portladder_stats('twelve columns'),
            stbdladder_stats('twelve columns'),
        ]
    )

def build_spuds_tab():
    return html.Div(
        id ='Spuds-Container',
        className = 'twelve columns',
        children = [
            spudmain_stats('twelve columns'),
            spudauxgraph_stats('twelve columns'),
            spudcargraph_stats('twelve columns'),
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
        html.Div(
            id = 'toolbar',
            className = 'row',
            children = [
                html.H1(children = title+' Dredge Dashboard',className = 'six columns'),
                html.H1(className = 'five columns'),
            ],
        ),
        build_tabs(),
        html.Div(id='app-content'),
        dcc.Interval(
            id='interval-component',
            interval = 5 #milliseconds
        ),

        ]
)
@app.callback(
    Output('app-content','children'),
    [Input('app-tabs','value')])

def render_tabs(tab):
    global master
    cnxn = pyodbc.connect(cnxn_string)
    query = "SELECT * FROM "+table+" ORDER BY DateTime;"
    master = pd.read_sql(query, cnxn)
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



if __name__ == '__main__':

    #HMA Server IP: 10.0.0.11
    serve(app, host='10.0.0.11', port=8051)
    #Testing
    #app.run_server(debug=True, host = '10.0.0.153', port=port)
