import pandas as pd
from datetime import datetime, date
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import pyodbc
from waitress import serve

#clear database
master = pd.DataFrame([])
#SQL Connection
server = 'HMA-S-003'
database = 'DredgeSQL'
userid = 'redlion'
passwd = 'Weeks123!'
table = '[jschatry].[JSC_325_MAIN]'
cnxn_string ='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+userid+';PWD='+passwd+'; Trusted_Connection=yes'
cnxn = pyodbc.connect(cnxn_string)
query = "SELECT * FROM "+table+" ORDER BY DateTime;"
master = pd.read_sql(query, cnxn)
# oneday = all.loc[all.DateTime > all.DateTime.shift()-pd.Timedelta(hours = 24)]
port = 8050
title = 'Office Test'
datetime_now = datetime.now()
dtwt = date.today()
date = datetime.combine(dtwt, datetime.min.time())
time = datetime.time(datetime_now)


master.index = master.DateTime
#master = pd.read_csv('20010400.csv')
#formating data
master['Date'] = pd.to_datetime(master.DateTime, format = '%Y/%m/%d')
# master.Time = pd.to_datetime(master.Time, format = '%H:%M:%S').dt.time
# master.Date = pd.to_datetime(master.Date, format = '%Y/%m/%d')
# master.loc[:,'DateTime'] = master.apply(lambda master : pd.datetime.combine(master['Date'],master['Time']),1)
# master.sort_values(by='DateTime')
# master.dropna(axis=0)

#Setting Configuration
master.loc[master['CONFIGURATION'] == 0, 'config'] = 'Dredge Spuds'
master.loc[master['CONFIGURATION'] == 1, 'config'] = 'Christmas Tree'
master.loc[master['CONFIGURATION'] == 2, 'config'] = 'Carriage Barge'

#Elapsed Down Time

master['ElapsedTimeDown'] = (master['DateTime'] - master['DateTime'].groupby(master.RUNNING.eq('ON').cumsum()).transform('first'))



#Overview Table Key
key = ['Velocity (fps)', 'Density (SGU)', 'Discharge Pressure (psig)', 'Cutter Depth (ft.)', 'Pump One Horsepower', 'Pump Two Horsepower']


#instant data column of overview table
instantdata = pd.DataFrame(data = master.iloc[-1])
dredge_status = instantdata.loc['RUNNING'].values.item()
instant_velocity = instantdata.loc['VELOCITY'].values.item()
instant_density = instantdata.loc['DENSITY'].values.item()
instant_dischpr = instantdata.loc['DISCHPR'].values.item()
instant_cdbw = instantdata.loc['CDBW'].values.item()
instant_p1hp = instantdata.loc['P1HP'].values.item()
instant_p2hp = instantdata.loc['P2HP'].values.item()
instant_datalist = [instant_velocity,instant_density,instant_dischpr,instant_cdbw,instant_p1hp,instant_p2hp]
instant_config = instantdata.loc['config'].values.item()
downtime = instantdata.loc['ElapsedTimeDown'].values.item()
downtime_str = str(downtime)
downtime_disp = downtime_str[7:]
srv_status = instantdata.loc['SRVSTATUS'].values.item()
srv_uwp_in_opnsp = instantdata.loc['SRVUWPINOPNSP'].values.item()
srv_uwp_in_clssp = instantdata.loc['SRVUWPINCLSSP'].values.item()
srv_uwp_out_opnsp = instantdata.loc['SRVUWPPOUTOPNSP'].values.item()
srv_uwp_out_clssp = instantdata.loc['SRVUWPPOUTCLSSP'].values.item()
srv_p1_out_opnsp = instantdata.loc['SRVP1OUTOPNSP'].values.item()
srv_p1_out_clssp = instantdata.loc['SRVP1OUTCLSSP'].values.item()
srv_p2_out_opnsp = instantdata.loc['SRVP2OUTOPNSP'].values.item()
srv_p2_out_clssp = instantdata.loc['SRVP2OUTCLSSP'].values.item()
uwp_intake = instantdata.loc['UWPINTAKE'].values.item()
uwp_output = instantdata.loc['UWPDISCH'].values.item()
p1_output = instantdata.loc['P1DISCH'].values.item()
p2_output = instantdata.loc['P2DISCH'].values.item()
gen1load = instantdata.loc['GEN1LOADPC'].values.item()
gen2load = instantdata.loc['GEN2LOADPC'].values.item()
gen3load = instantdata.loc['GEN3LOADPC'].values.item()

#finding data for Today
today = pd.DataFrame(data = master.loc[master.DateTime > date])
today_running = today.loc[today['RUNNING']=='ON']
today_avgdata = today.mean(axis = 0)
today_velocity = today_avgdata.loc['VELOCITY']
today_density = today_avgdata.loc['DENSITY']
today_dischpr = today_avgdata.loc['DISCHPR']
today_cdbw = today_avgdata.loc['CDBW']
today_p1hp = today_avgdata.loc['P1HP']
today_p2hp = today_avgdata.loc['P2HP']
today_datalist = [today_velocity,today_density,today_dischpr,today_cdbw,today_p1hp,today_p2hp]

#First Block Averages
firstblock = today_running.between_time('00:00:00','6:00:00')
firstblock_avgdata = firstblock.mean(axis = 0)
firstblock_velocity = firstblock_avgdata.loc['VELOCITY']
firstblock_density = firstblock_avgdata.loc['DENSITY']
firstblock_dischpr = firstblock_avgdata.loc['DISCHPR']
firstblock_cdbw = firstblock_avgdata.loc['CDBW']
firstblock_p1hp = firstblock_avgdata.loc['P1HP']
firstblock_p2hp = firstblock_avgdata.loc['P2HP']
firstblock_datalist = [firstblock_velocity,firstblock_density,firstblock_dischpr,firstblock_cdbw,firstblock_p1hp,firstblock_p2hp]

#Second Block Averages
secondblock = today_running.between_time('06:00:01','12:00:00')
secondblock_avgdata = secondblock.mean(axis = 0)
secondblock_velocity = secondblock_avgdata.loc['VELOCITY']
secondblock_density = secondblock_avgdata.loc['DENSITY']
secondblock_dischpr = secondblock_avgdata.loc['DISCHPR']
secondblock_cdbw = secondblock_avgdata.loc['CDBW']
secondblock_p1hp = secondblock_avgdata.loc['P1HP']
secondblock_p2hp = secondblock_avgdata.loc['P2HP']
secondblock_datalist = [secondblock_velocity,secondblock_density,secondblock_dischpr,secondblock_cdbw,secondblock_p1hp,secondblock_p2hp]

#Third Block Averages
thirdblock = today_running.between_time('12:00:01','18:00:00')
thirdblock_avgdata = thirdblock.mean(axis = 0)
thirdblock_velocity = thirdblock_avgdata.loc['VELOCITY']
thirdblock_density = thirdblock_avgdata.loc['DENSITY']
thirdblock_dischpr = thirdblock_avgdata.loc['DISCHPR']
thirdblock_cdbw = thirdblock_avgdata.loc['CDBW']
thirdblock_p1hp = thirdblock_avgdata.loc['P1HP']
thirdblock_p2hp = thirdblock_avgdata.loc['P2HP']
thirdblock_datalist = [thirdblock_velocity,thirdblock_density,thirdblock_dischpr,thirdblock_cdbw,thirdblock_p1hp,thirdblock_p2hp]


#Fourth Block Averages
fourthblock = today_running.between_time('18:00:01','23:59:59')
fourthblock_avgdata = fourthblock.mean(axis = 0)
fourthblock_velocity = fourthblock_avgdata.loc['VELOCITY']
fourthblock_density = fourthblock_avgdata.loc['DENSITY']
fourthblock_dischpr = fourthblock_avgdata.loc['DISCHPR']
fourthblock_cdbw = fourthblock_avgdata.loc['CDBW']
fourthblock_p1hp = fourthblock_avgdata.loc['P1HP']
fourthblock_p2hp = fourthblock_avgdata.loc['P2HP']
fourthblock_datalist = [fourthblock_velocity,fourthblock_density,fourthblock_dischpr,fourthblock_cdbw,fourthblock_p1hp,fourthblock_p2hp]


firstblocktableframe = pd.DataFrame(list(zip(key,instant_datalist,firstblock_datalist,secondblock_datalist,thirdblock_datalist,fourthblock_datalist,today_datalist,)), columns = ['Data','Instant','0:00-6:00','6:00-12:00','12:00-18:00','18:00-24:00','Today'])
secondblocktableframe = pd.DataFrame(list(zip(key,instant_datalist,secondblock_datalist,firstblock_datalist,thirdblock_datalist,fourthblock_datalist,today_datalist,)), columns = ['Data','Instant','6:00-12:00','0:00-6:00','12:00-18:00','18:00-24:00','Today'])
thirdblocktableframe = pd.DataFrame(list(zip(key,instant_datalist,thirdblock_datalist,firstblock_datalist,secondblock_datalist,fourthblock_datalist,today_datalist,)), columns = ['Data','Instant','12:00-18:00','0:00-6:00','6:00-12:00','18:00-24:00','Today'])
fourthblocktableframe = pd.DataFrame(list(zip(key,instant_datalist,fourthblock_datalist,firstblock_datalist,secondblock_datalist,thirdblock_datalist,today_datalist,)), columns = ['Data','Instant','18:00-24:00','0:00-6:00','6:00-12:00','12:00-18:00','Today'])



#Dredge Data
dredge_table_data = master[['DateTime','VELOCITY','DENSITY','DISCHPR','SWINGSPD','SWINGRADIUS','CDBW','MDBW','CONFIGURATION',]]
trace_velocity = go.Scatter(x=master['DateTime'], y=master['VELOCITY'],name="Velocity (fps)")
trace_density = go.Scatter(x=master.DateTime, y=master.DENSITY,name='Density (SGU)',yaxis = y2)
trace_dischpr = go.Scatter(x=master.DateTime, y=master.DISCHPR, name='Discharge Pressure (psig)',yaxis = y2)
trace_swingspd = go.Scatter(x=master.DateTime, y=master.SWINGSPD, name='Swing Speed (fpm)',yaxis = y2)
trace_swingradius = go.Scatter(x=master.DateTime, y=master.SWINGRADIUS, name='Swing Radius (ft)',yaxis = y2)
trace_cdbw = go.Scatter(x=master.DateTime, y=master.CDBW, name='Cutter Depth Below Water (ft)',yaxis = y2)
trace_mdbw = go.Scatter(x=master.DateTime, y=master.MDBW, name='Max Depth Below Water (ft)',yaxis = y2)
#trace_configuration = go.Scatter(x=master.DateTime, y=master.CONFIGURATION, name='Configuration')
data = [trace_velocity,trace_density,trace_dischpr,trace_swingspd,trace_swingradius,trace_cdbw,trace_mdbw,]

# UWP Data
trace_uwpintake = go.Scatter(x=master['DateTime'], y=master['UWPINTAKE'],name = "Suction Pressure(psig)")
trace_uwpdisch = go.Scatter(x=master['DateTime'], y=master['UWPDISCH'],name = "Discharge Pressure(psig)")
trace_uwphp = go.Scatter(x=master['DateTime'], y=master['UWPHP'],name = "Horsepower")
trace_uwphplimit = go.Scatter(x=master['DateTime'], y=master['UWPHPLIMIT'],name = "Horsepower Limit")
trace_uwpgear = go.Scatter(x=master['DateTime'], y=master['UWPINTAKE'],name = "Gear Ratio")
trace_rpm = go.Scatter(x=master['DateTime'], y=master['UWPINTAKE'],name = "RPM")
trace_rpmsp = go.Scatter(x=master['DateTime'], y=master['UWPINTAKE'],name = "RPM Set Point")

uwpdata = [trace_uwpintake,trace_uwpdisch,trace_uwphp,trace_uwphplimit,trace_uwpgear,trace_rpm,trace_rpmsp,]

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
trace_p1spcsp = go.Scatter(x=master['DateTime'], y=master['P1SPCSP'],name="Suction Pressure Control Set Point (psig)")
trace_p1dpcsp = go.Scatter(x=master['DateTime'], y=master['P1DPCSP'],name="Discharge Pressure Control Set Point (psig)")
trace_p1smsp = go.Scatter(x=master['DateTime'], y=master['P1SMCSP'],name="Speed Match Control Bias Set Point (RPM)")

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
trace_p2spcsp = go.Scatter(x=master['DateTime'], y=master['P2SPCSP'],name="Suction Pressure Control Set Point (psig)")
trace_p2dpcsp = go.Scatter(x=master['DateTime'], y=master['P2DPCSP'],name="Discharge Pressure Control Set Point (psig)")
trace_p2smsp = go.Scatter(x=master['DateTime'], y=master['P2SMCSP'],name="Speed Match Control Bias Set Point (RPM)")

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
trace_spmain_xs_lp = go.Scatter(x=master['DateTime'], y=master['SPUDMAINXSLP'],name="Main Spud or Stern Christmas Tree Winch Line Pull (k-ft/lbs)")
trace_spudmainlplim = go.Scatter(x=master['DateTime'], y=master['SPUDMAINLPLIM'],name="Main Spud or Stern Christmas Tree Winch Line Pull Limit (ft/lbs)")
trace_spudmainls = go.Scatter(x=master['DateTime'], y=master['SPUDMAINLS'],name="Main Spud or Stern Christmas Tree Winch Line Speed (fpm)")
trace_spudmainlssp = go.Scatter(x=master['DateTime'], y=master['SPUDMAINLSSP'],name="Main Spud or Stern Christmas Tree Winch Line Speed Set Point (fpm)")
trace_spudmainpos = go.Scatter(x=master['DateTime'], y=master['SPUDMAINPOS'],name="Main Spud Position or Stern Christmas Tree Line Length (ft)")
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

#Generator Load Charts
trace_gen1load = go.Scatter(x=master['DateTime'], y=master['GEN1LOADPC'],name="Gen 1")
trace_gen2load = go.Scatter(x=master['DateTime'], y=master['GEN2LOADPC'],name="Gen 2")
trace_gen3load = go.Scatter(x=master['DateTime'], y=master['GEN3LOADPC'],name="Gen 3")

genloaddata = [trace_gen1load,trace_gen2load,trace_gen3load]

comparisondata = [trace_velocity,trace_density,trace_dischpr,trace_swingspd,trace_swingradius,trace_cdbw,trace_mdbw,
                    trace_uwpintake,trace_uwpdisch,trace_uwphp,trace_uwphplimit,trace_uwpgear,trace_rpm,trace_rpmsp,
                    trace_p1intake,trace_p1discharge,trace_p1hp,trace_p1hplimit,trace_p1gear,
                    trace_p2intake,trace_p2discharge,trace_p2hp,trace_p2hplimit,trace_p2gear,
                    trace_cuttertorque,trace_cuttertorquelimit,trace_cutterrpm,trace_cutterrpmsp,
                    trace_pswinglp,trace_pswinglplim,trace_pswingdrumdia,trace_pswingls,trace_pswinglssp,
                    trace_sswinglp,trace_sswinglplim,trace_sswingdrumdia,trace_sswingls,trace_sswinglssp,
    ]

layout = dict(showlegend=True)
dredgelayout = go.Layout(yaxis = dict(range = [master.VELOCITY.min(),master.VELOCITY.max()]),
                            yaxis2 = dict(range = [master.SWINGRADIUS.min(),master.SWINGRADIUS.max()]))

dredgegraph = dict(data=data,layout=dredgelayout)
uwpgraph = dict(data=uwpdata,layout=layout)
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
genloadgraph = dict(data = genloaddata, layout = layout,)
comparisongraph = dict(data = comparisondata, layout = layout)
#Loading Style Sheet
external_stylesheets = ['https://codepen.io/jonmurders/pen/qBEoLeE.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets,)

server = app.server

def overview_table_firstblock():
    return dash_table.DataTable(
        id = 'overview-table',
        #width = '50%',
        columns=[{"name": i, "id": i} for i in firstblocktableframe.columns],
        data=firstblocktableframe.to_dict('records'),

    )
srvframe = pd.DataFrame(list(zip([
                                    'UWP Intake Open Set Point',
                                    'UWP Intake Close Set Point',
                                    'UWP Output Open Set Point',
                                    'UWP Output Close Set Point',
                                    'Pump One Output Open Set Point',
                                    'Pump One Output Close Set Point',
                                    'Pump Two Output Open Set Point',
                                    'Pump Two Output Close Set Point,'],
                                    [
                                    srv_uwp_in_opnsp,
                                    srv_uwp_in_clssp,
                                    srv_uwp_out_opnsp,
                                    srv_uwp_out_clssp,
                                    srv_p1_out_opnsp,
                                    srv_p1_out_clssp,
                                    srv_p2_out_opnsp,
                                    srv_p2_out_clssp,])),columns = ['Data', 'Current Set Points'])
def srv_table():
    return dash_table.DataTable(
    id = 'srv-table',
    columns=[{"name": i, "id": i} for i in srvframe.columns],
    data=srvframe.to_dict('records'),
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


def uwp_stats(width):
    return html.Div(
        id = 'uwpstats',
        className = width,
        children = [
            html.H3(children = 'UWP Stats'),
            dcc.Graph(id = 'uwp-graph', figure = uwpgraph)
        ],
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
            html.Br(),
            html.Div(className = 'three columns', children = [
                html.H4('Dredge Overview'),
                html.Div(id = 'status-container',className = 'row',children = [
                    html.Div(id = 'status-cats', className = 'eight columns', children = [
                        html.H5('Dredge Status:'),
                        html.H6('Elapsed Time:'),
                        html.Br(),
                        html.H5('Configuration'),
                        html.Div(id = 'indicator-container', className = 'row', children = [
                            html.Div(id = 'spud-light-container',className = 'four columns',children = [
                                daq.Indicator(id = 'spud-light', color = "#B7BDC0", value = False,label = 'Spuds'),
                            ],),
                            html.Div(id = 'spud-light-container',className = 'four columns',children = [
                                daq.Indicator(id = 'carriage-light', color = "#B7BDC0", value = False,label = 'Carriage'),
                            ],),
                            html.Div(id = 'spud-light-container',className = 'four columns',children = [
                                daq.Indicator(id = 'christmas-tree-light', color = "#B7BDC0", value = False,label = 'X-Mas'),
                            ],),
                        ],),


                    ]),
                    html.Div(id = 'status-results', className = 'one columns', children = [
                        html.Br(),
                        daq.Indicator(id = 'running-light', color = "red", value = True),
                        html.H6(downtime_disp),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        ]),
                ], ),


            ]),
            html.Div(
                id = 'table-container',
                className = 'six columns',
                children = [overview_table_firstblock(),],
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

            uwp_stats('twelve columns'),
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
            spudaux_stats('twelve columns'),
            spudcar_stats('twelve columns'),
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
            html.Br(),
            html.Div( id = 'srv-tab-container',
            className = 'row',
            children = [
                html.Div(id = 'srv-indicator-container',className = 'two columns',
                    children = [
                        daq.Indicator(id = 'running-light', color = "red", value = True,label = 'Dredge Status'),
                        html.Br(),
                        daq.Indicator(id = 'srv-light', color = "red", value = True,label = 'SRV Status'),
                    ]),
                html.Div( id = 'srv-data-container',
                    className = 'four columns',
                    children = [srv_table()]),
                html.Div(className = 'row', children = [
                    html.Div(id = 'srv-gauges-container-1',
                        className = 'three columns',
                        children = [
                            daq.Gauge(
                                id = 'srv-uwp-in-gauge',
                                label = 'UWP Intake',
                                value = 0,
                                min = 0,
                                max = 100,
                                showCurrentValue = True,
                                units = 'PSIG'
                            ),
                            daq.Gauge(
                                id = 'srv-uwp-out-gauge',
                                label = 'UWP Discharge',
                                value = 0,
                                min = 0,
                                max = 100,
                                showCurrentValue = True,
                                units = 'PSIG'
                            ),
                        ],),
                        html.Div(id = 'srv-gauges-container-2',
                            className = 'three columns',
                            children = [
                            daq.Gauge(
                                id = 'srv-p1-gauge',
                                label = 'P1 Discharge',
                                value = 0,
                                min = 0,
                                max = 400,
                                showCurrentValue = True,
                                units = 'PSIG'
                            ),
                            daq.Gauge(
                                id = 'srv-p2-gauge',
                                label = 'P2 Discharge',
                                value = 0,
                                min = 0,
                                max = 400,
                                showCurrentValue = True,
                                units = 'PSIG'
                            ),

                    ],),
                ],),
            ],),

        ]
    )

def build_generators_tab():
    return html.Div(
        id ='Generators-Container',
        className = 'twelve columns',
        children = [
            html.Br(),
            html.Div( className = ('row'), children = [
                html.Div(className = 'four columns', children = [
                    daq.Gauge(
                        id = 'gen1-load-gauge',
                        label = 'Generator 1 Load',
                        value = 0,
                        min = 0,
                        max = 100,
                        showCurrentValue = True,
                        units = '%'
                    ),
                ],),
                html.Div(className = 'four columns', children = [
                    daq.Gauge(
                        id = 'gen2-load-gauge',
                        label = 'Generator 2 Load',
                        value = 0,
                        min = 0,
                        max = 100,
                        showCurrentValue = True,
                        units = '%'
                    ),
                ],),
                html.Div(className = 'four columns', children = [
                    daq.Gauge(
                        id = 'gen3-load-gauge',
                        label = 'Generator 3 Load',
                        value = 0,
                        min = 0,
                        max = 400,
                        showCurrentValue = True,
                        units = '%'
                    ),
                ],),
            ],),
            html.Div(className = 'twelve columns', children = [
                dcc.Graph(id='genload-graph',figure = genloadgraph)
            ],),
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
app.config.suppress_callback_exceptions = True

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Dredge Dashboard</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>

    </body>
</html>
'''

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
@server.route("/dash")
def Title():
    return app,index()
@app.callback(
    Output('app-content','children'),
    [Input('app-tabs','value'),])

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

@app.callback(Output('running-light','color'),[Input('interval-component','n-intervals')])
def update_dredge_status(clicks):
    if dredge_status == 'On':
        return '#00cc96'
    else:
        return 'red'
@app.callback(Output('spud-light','color'),[Input('interval-component','n-intervals')])
def update_dredge_status(clicks):
    if instant_config == 'Dredge Spuds':
        return '#00cc96'
    else:
        return '#B7BDC0'
@app.callback(Output('carriage-light','color'),[Input('interval-component','n-intervals')])
def update_dredge_status(clicks):
    if instant_config == 'Carriage Barge':
        return '#00cc96'
    else:
        return '#B7BDC0'
@app.callback(Output('christmas-tree-light','color'),[Input('interval-component','n-intervals')])
def update_dredge_status(clicks):
    if instant_config == 'Christmas Tree':
        return '#00cc96'
    else:
        return '#B7BDC0'
@app.callback(Output('srv-light','color'),[Input('interval-component','n-intervals')])
def update_dredge_status(clicks):
    if dredge_status == 'On':
        return '#00cc96'
    else:
        return 'red'

@app.callback(Output('srv-uwp-in-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_in_gauge(clicks):
    return uwp_intake

@app.callback(Output('srv-uwp-out-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_out_gauge(clicks):
    return uwp_output

@app.callback(Output('srv-p1-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_in_gauge(clicks):
    return p1_output

@app.callback(Output('srv-p2-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_in_gauge(clicks):
    return p2_output

@app.callback(Output('gen1-load-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_in_gauge(clicks):
    return gen1load

@app.callback(Output('gen2-load-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_in_gauge(clicks):
    return gen2load

@app.callback(Output('gen3-load-gauge','value'),[Input('interval-component','n-intervals')])
def update_srv_uwp_in_gauge(clicks):
    return gen3load

if __name__ == '__main__':

    #HMA Server IP: 10.0.0.11
    #serve(app.server, host='10.0.0.153', port=8050, url_scheme='https',threads=16)
    #Testing
    app.run_server(debug=True, host = '10.0.0.153', port=port)
