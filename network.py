# %%
from matplotlib import pyplot as plt
import numpy as np

def main():
    arrSize = 10
    neuronOff = np.empty([arrSize, arrSize])
    neuronOff.fill(-1)
    offX = [x for x in range(arrSize) for y in range(arrSize) if neuronOff[x][y] == -1]
    offY = [y for x in range(arrSize) for y in range(arrSize) if neuronOff[x][y] == -1]
    onX = [x for x in range(arrSize) for y in range(arrSize) if neuronOff[x][y] == 0]
    onY = [y for x in range(arrSize) for y in range(arrSize) if neuronOff[x][y] == 0]
    plt.scatter(offX, offY, color='r')
    plt.scatter(onX, onY, color='b')
    plt.title("Completely Off Neuron Grid")
    plt.show()
    """
    l1: list = [i for i in range(10)]
    print(l1)
    l2: list = [i for i in range(10, 20)]
    print(l2)
    for i, (x, y) in enumerate(zip(l1, l2)):
        print(f"At index {i}, L1 is {x} and L2 is {y}")
    """

if __name__ == "__main__":
    main()
# %%
