import psutil
import json

def get_disks():
    result = {}
    result["usage_perc"] = psutil.disk_usage('/').percent
    return result

with open("disks_data.json", 'w') as file:
    file.write(json.dumps(get_disks()))