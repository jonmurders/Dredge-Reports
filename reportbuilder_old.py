import jinja2
import os
import pandas as pd
from bokeh.layouts import column
from bokeh.models import Button, CustomJS, ColumnDataSource
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from bokeh.io import output_file, show
from bokeh.models.widgets import MultiSelect


templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "name.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(name='Jon')

master = pd.read_csv('19122000.csv')
master.Time = pd.to_datetime(master.Time, format = '%H:%M:%S')
mastersource = ColumnDataSource(master)
multiselect = MultiSelect(title = 'Tags', value = ['VELOCITY'],options = [('VELOCITY','Velocity'),['DENSITY','Density']] )

callback = CustomJS(args=dict(source = mastersource), code = '''

    var data = mastersource.data


''')

#Velocity plot
vp = figure(y_range=(0, 1),x_axis_type = 'datetime')
vp.line(master.Time,master.VELOCITY)

curdoc().add_root(column(vp,multiselect))
os.system('bokeh serve --show reportbuilder.py')
