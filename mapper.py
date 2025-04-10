import json
import sys

for line in sys.stdin:
    l = line.rstrip()
    try:
        data = json.loads(l.rstrip(","))
    except:
        continue
    else:
        net_profit = 0 #for each store keep net profit as zero initially
        sales_data_available = False
        for goods in data["categories"]: #for the top goods of each store
            if goods in data["sales_data"]: #if sales data is present
                try:
                    net_profit = net_profit + data["sales_data"][goods]["revenue"] - data["sales_data"][goods]["cogs"]
                    sales_data_available = True
                except:
                    continue
            else:
                continue
        if sales_data_available: #cases where sales data not available for any of the popular products ignored
            print(data["city"], net_profit)
