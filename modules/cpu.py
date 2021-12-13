import psutil
import json

def get_cpu_params():
    result = {}
    result["cur_freq"] = psutil.cpu_freq(False).current
    result["count"] = psutil.cpu_count(True)
    return result

with open("cpu_data.json", 'w') as file:
    file.write(json.dumps(get_cpu_params()))