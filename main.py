import matplotlib.pyplot as plt
import math

N = 5000

def sieve():
    global N
    prime = [True] * N
    for i in range(2, N):
        if (prime[i]):
            for x in range(i+i, N, i):
                prime[x] = False
    return prime

def main():

    global N
    
    x_values = []
    y_values = []
    prime = sieve()
    for i in range(1, N):
        x_values.append(i * math.cos(i))
        y_values.append(i * math.sin(i))
        # x_values.append(i * math.cos(i))
        # y_values.append(i * mathcode.sin(i))

    plt.figure(1)
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis line
    plt.scatter(x_values, y_values, color='red', marker='.', label='Dots')
    
    x_primes = []
    y_primes = []
    prime = sieve()
    for i in range(1, N):
        if (prime[i]):
            y_primes.append(i * math.cos(i))
            x_primes.append(i * math.sin(i))
        # x_values.append(i * math.cos(i))
        # y_values.append(i * math.sin(i))

    plt.figure(2)
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis line
    plt.scatter(x_primes, y_primes, color='blue', marker='.', label='Dots')




    plt.show()

main()