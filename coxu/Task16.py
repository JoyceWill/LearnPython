import csv

writter = csv.writer(open('stocks.csv', 'wb', buffering = 0))
writter.writerows(
    [
        ('GOOG', 'Google Inc', 505.24, 0.47, 0.09),
        ('YHOO', 'Yahoo!', 27.38, 0.33,1.22)
    ]
)

#read stock data, print status messages
stocks = csv.reader(open('stocks.csv','rb'))
status_labels = {-1: 'down', 0 : 'unchaged', 1 : 'up'}
for ticker , name, price, change, pct in stocks:
    status = status_labels[cmp(float(change), 0.0)]
    print '%s is %s (%s%%)' %(name, status, pct )