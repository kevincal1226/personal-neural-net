# %%
from matplotlib import pyplot as plt
import numpy as np

def makeLetterA(neuron) -> any:
    return neuron

def makeJXX(neuron) -> any:
    return neuron

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
    neuronA = makeLetterA(neuronOff)


if __name__ == "__main__":
    main()
# %%
