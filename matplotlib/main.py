import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def new_function(): 
    # initializing
    slices = [7,2,2,13]
    activities = ['sleeping','eating','working','playing']
    cols = ['c','m','r','b']

    # pie chart 
    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')

    plt.title('Interesting Graph\nCheck it out')
    plt.show()

    # intializing 
    days = [1,2,3,4,5]

    sleeping = [7,8,6,11,7]
    eating =   [2,3,4,3,2]
    working =  [7,8,7,2,2]
    playing =  [8,5,7,8,13]

    # plot 
    plt.plot([],[],color='m', label='Sleeping', linewidth=5)
    plt.plot([],[],color='c', label='Eating', linewidth=5)
    plt.plot([],[],color='r', label='Working', linewidth=5)
    plt.plot([],[],color='k', label='Playing', linewidth=5)

    plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()
    # initializing 
    x = [1,2,3]
    y = [5,7,4]

    x2 = [1,2,3]
    y2 = [10,14,12]


    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()
    # regular plot
    plt.plot([1,2,3],[5,7,4])
    plt.show()


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True)
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)
    
##    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
##                                                          delimiter=',',
##                                                          unpack=True,
##                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep,'-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)#, color='g', linestyle='-', linewidth=5)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('TSLA')