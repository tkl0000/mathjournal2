import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

N = 10000

def sieve():
    global N
    prime = [True] * N
    for i in range(2, N):
        if (prime[i]):
            for x in range(i+i, N, i):
                prime[x] = False
    return prime

def static():
    global N
    
    x_values = [i * math.cos(i) for i in range(1, N)]
    y_values = [i * math.sin(i) for i in range(1, N)]

    plt.figure(1)
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis line
    plt.scatter(x_values, y_values, color='red', marker='.', label='Dots')
    
    prime = sieve()
    x_primes = [i * math.cos(i) for i in range(1, N) if prime[i]]
    y_primes = [i * math.sin(i) for i in range(1, N) if prime[i]]

    fig = plt.subplots()
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis line
    plt.scatter(x_primes, y_primes, color='blue', marker='.', label='Dots')
    plt.show()

def animate():
    global N
    
    prime = [True] * N
            
    i_to_plot = [i for i in range(1, N)]

    fig, ax = plt.subplots()
    scat = ax.scatter(0, 0, color='blue', marker='.', label='Dots')
    plt.xlim(-N, N)
    plt.ylim(-N, N)
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis line
    

    def update(frame, i_to_plot):
        if (frame == 1): 
            i_to_plot = [i for i in range(1, N)]
            for i in range(1, N):
                prime[i] = True
        if (frame > 1 and prime[frame]):
            for i in range(frame + frame, N, frame):
                if (i in i_to_plot):
                    i_to_plot.remove(i)
                prime[i] = False
        x_plot = [i * math.cos(i) for i in i_to_plot]
        y_plot = [i * math.sin(i) for i in i_to_plot]
        scat.set_offsets(np.c_[x_plot, y_plot])
        plt.title(f'p: {frame}')
        print(frame)

    ani = animation.FuncAnimation(fig, update, frames=N, fargs=[i_to_plot], interval=500, repeat=True)
    plt.show()

def main():
    static()
    animate()
    # ex()

main()