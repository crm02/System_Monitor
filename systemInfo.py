import psutil

def get_cpu_per():
        cpu_perc = psutil.cpu_percent(interval =0.1) # since this isn't repeating bc its a func call, does inter
        # val matter here? The interval here affects our x axis! very cool
        return cpu_perc # returns cpu

def get_ram():
        ram = psutil.virtual_memory()
        return ram[2] # returns ram usage