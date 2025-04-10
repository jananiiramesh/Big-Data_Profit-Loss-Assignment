import json
import sys

prev_city = None

for line in sys.stdin:
    current_city, profit_loss = line.split()
    profit_loss = int(profit_loss)
    if(current_city == prev_city):
        if profit_loss>0:
            dict_for_city["profit_stores"] += 1
        elif profit_loss <= 0:
            dict_for_city["loss_stores"] += 1
    else:
        if prev_city:
            print(json.dumps(dict_for_city))
        prev_city = current_city
        dict_for_city = {}
        dict_for_city["city"] = current_city
        dict_for_city["profit_stores"] = 0
        dict_for_city["loss_stores"] = 0
        if profit_loss>0:
            dict_for_city["profit_stores"] += 1
        else:
            dict_for_city["loss_stores"] += 1

print(json.dumps(dict_for_city))

