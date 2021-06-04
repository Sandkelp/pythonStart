from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file


start=datetime.datetime(2016,3,1)
end=datetime.datetime(2020,3,10)
df = data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

p = figure(x_axis_type='datetime',width=1000,height=300)
p.title.text = "Candle Stick Chart"
hours_12 = 60*60*12*1000
p.segment(df.index, df.High, df.index, df.Low, color='Black')
p.rect(df.index[df.Close > df.Open], (df.Open+df.Close)/2, hours_12,abs(df.Open - df.Close),fill_color='green',line_color='black')

p.rect(df.index[df.Close < df.Open], (df.Open+df.Close)/2, hours_12,abs(df.Open - df.Close),fill_color='red',line_color='black')
def inc_dec(c,o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "No Change"
    return value
df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]


output_file("CS.html")
show(p)
print(df)