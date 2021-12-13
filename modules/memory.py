import psutil
import json

def get_mem_params():
    result = {}
    result["swap_mem"] = psutil.swap_memory().total
    result["virt_mem"] = psutil.virtual_memory().total
    return result

with open("memory_data.json", 'w') as file:
    file.write(json.dumps(get_mem_params()))