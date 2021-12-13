import psutil
import json

def get_connetcion_status():
    result ={}
    result["net_connection"] = psutil.net_if_stats()['enp0s3'].isup
    result["cur_net_speed"] = psutil.net_if_stats()['enp0s3'].speed
    return result

with open("connection_data.json", 'w') as file:
    file.write(json.dumps(get_connetcion_status()))