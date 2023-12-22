import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

N = 5000

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
    
    x_primes = []
    y_primes = []
    prime = sieve()
    for i in range(1, N):
        if (prime[i]):
            y_primes.append(i * math.cos(i))
            x_primes.append(i * math.sin(i))
        # x_values.append(i * math.cos(i))
        # y_values.append(i * math.sin(i))
            
    i_to_plot = [i for i in range(1, N)]

    fig, ax = plt.subplots()
    scat = ax.scatter(0, 0, color='blue', marker='.', label='Dots')
    plt.xlim(-5000, 5000)
    plt.ylim(-5000, 5000)
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis line
    

    def update(frame, i_to_plot):
        if (frame == 0): i_to_plot = [i for i in range(1, N)]
        if (not prime[frame] and frame in i_to_plot):
            i_to_plot.remove(frame)
        x_plot = [i * math.cos(i) for i in i_to_plot]
        y_plot = [i * math.sin(i) for i in i_to_plot]
        scat.set_offsets(np.c_[x_plot, y_plot])
        print(frame)

    ani = animation.FuncAnimation(fig, update, frames=N, fargs=[i_to_plot], interval=0, repeat=True)
    plt.show()

def ex():
    np.random.seed(0)
    x_data = np.random.rand(100)
    y_data = np.random.rand(100)

    fig, ax = plt.subplots()
    scat = ax.scatter(x_data, y_data)

    def update(frame):
        # Updating the data for the scatter plot
        scat.set_offsets(np.c_[np.random.rand(100), np.random.rand(100)])
        return scat,

    # Creating an animation
    ani = animation.FuncAnimation(fig, update, frames=10, interval=200, blit=True)
    plt.show()

def main():
    static()
    animate()
    # ex()

main()