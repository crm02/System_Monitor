import matplotlib.pyplot as plt
from systemInfo import get_cpu_per, get_ram
from matplotlib.animation import FuncAnimation


def update(frame):
    
    new_cpu =get_cpu_per() 
    cpu.append(new_cpu)
    line.set_data(range(len(cpu)),cpu)

    new_ram = get_ram()
    ram.append(new_ram)
    line2.set_data(range(len(ram)),ram)

    ax.relim()
    ax.autoscale_view()
    plt.annotate(f'{get_ram()}',xy=(get_ram(),get_ram()))

    
if __name__ == "__main__":
    cpu = []
    ram = []

    fig, ax = plt.subplots()
    line, = ax.plot([],[], label='CPU')
    line2, = ax.plot([],[],  label = 'RAM')
    ax.legend()
    ax.set_ylim(0,100)
    ax.set_yticks(range(0,101,5))
    ax.set_title('CPU and RAM Percentages')
    ax.set_xlabel('Time')
    ax.set_ylabel('%')


    animation = FuncAnimation(fig, update, frames=None, interval= 100, repeat =True)
    # Decrease interval for faster updates
    plt.show()