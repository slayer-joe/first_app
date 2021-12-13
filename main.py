import psutil
from modules import connection
from modules import cpu
from modules import disks
from modules import memory


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
    cpu_data = cpu.get_cpu_params()
    diskpart_data = disks.get_disks()
    memory_data = memory.get_mem_params()
    network_data = connection.get_connetcion_status()

    display_params(cpu=cpu_data, disk=diskpart_data, mem=memory_data, net=network_data)

if __name__ == "__main__":
    start()

    