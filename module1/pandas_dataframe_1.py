import pandas as pd
import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
# style.use('fivethirtyeight')

start = datetime.datetime(2018,1,1)
end = datetime.date.today()

baba = pdr.get_data_yahoo('BABA', start, end)

print(baba.head())

baba['High'].plot()
plt.legend()
plt.show()
