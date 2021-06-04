from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd


#basic data
df = pd.read_csv("C:\\Users\\ssubh\\Downloads\\bokeh.csv",parse_dates=["Date"])

p=figure(width=500,height=250,x_axis_type="datetime")
p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)
p.circle(df["Date"],df["Close"],color="Orange",alpha=0.5)

output_file("timeseries.html")


show(p)