from ctypes import resize
import psutil

def get_cpu_params():
    result = {}
    result["cur_freq"] = psutil.cpu_freq(False).current
    result["count"] = psutil.cpu_count(True)
    return result


def get_mem_params():
    result = {}
    result["swap_mem"] = psutil.swap_memory().total
    result["virt_mem"] = psutil.virtual_memory().total
    return result


def get_disks():
    result = {}
    result["usage_perc"] = psutil.disk_usage('/').percent
    return result


def get_connetcion_status():
    result ={}
    result["net_connection"] = psutil.net_if_stats()['enp0s3'].isup
    result["cur_net_speed"] = psutil.net_if_stats()['enp0s3'].speed
    return result

def display_params(**kwargs):
    cpu_str_template = "Current CPU frequency: {} | CPU count: {}"
    disk_str_template = "Disc memory usage percent: {}%"
    mem_str_template = "Swap memory: {}  |  Virtual memoru: {}"
    net_str_template = "Is network connection active: {}  |  Current network speed: {}"
    print("******MACHINE PARAMETERS******")
    print(cpu_str_template.format(kwargs['cpu']['cur_freq'], kwargs['cpu']['count']))
    print(disk_str_template.format(kwargs['disk']['usage_perc']))
    print(mem_str_template.format(kwargs['mem']['swap_mem'], kwargs['mem']['virt_mem']))
    print(net_str_template.format(kwargs['net']['net_connection'], kwargs['net']['cur_net_speed']))
    print('***************************')
    

def start():
    cpu_data = get_cpu_params()
    diskpart_data = get_disks()
    memory_data = get_mem_params()
    network_data = get_connetcion_status()

    display_params(cpu=cpu_data, disk=diskpart_data, mem=memory_data, net=network_data)

if __name__ == "__main__":
    start()

    