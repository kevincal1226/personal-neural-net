# %%
from matplotlib import pyplot as plt
import numpy as np

ARR_SIZE = 10

def emptyNeuron() -> any:
    neuronOff = np.empty([ARR_SIZE, ARR_SIZE])
    neuronOff.fill(-1)    
    return neuronOff


def makeLetterA() -> any:
    neuron = emptyNeuron()
    for i in range(4, 6):
        neuron[i][9] = 1
    for i in range(3, 7):
        neuron[i][8] = 1
    for i in range(2, 8):
        if i != 4 and i != 5:
            neuron[i][7] = 1
    for i in range (1, 3):
        neuron[i][6] = 1
    for i in range(7, 9):
        neuron[i][6] = 1
    for i in range(1, 9):
        neuron[i][5] = 1
    for i in range(0, 10):
        neuron[i][4] = 1
    for i in range(0, 10):
        if i <= 2 or i >= 7:
            neuron[i][3] = 1
    for i in range(0, 10):
        if i <= 1 or i >= 8:
            neuron[i][2] = 1
    for i in range(0, 10):
        for j in range(0, 2):
            if i <= 1 or i >= 8:
                neuron[i][j] = 1
    return neuron

def makeLetterB() -> any:
    neuron = emptyNeuron()   
    for i in range(2, 7):
        neuron[i][9] = 1
        neuron[i][5] = 1
        neuron[i][4] = 1
        neuron[i][0] = 1
    for i in range(2, 4):
        for j in range(1, 4):
            neuron[i][j] = 1
        for j in range(6, 9):
            neuron[i][j] = 1
    for i in range(6, 8):
        for j in range(1, 4):
            neuron[i][j] = 1
        for j in range(6, 9):
            neuron[i][j] = 1
    return neuron

def makeLetterC() -> any:
    neuron = emptyNeuron()    
    for i in range(2, 8):
        neuron[i][9] = 1
        neuron[i][0] = 1
    for i in range(1, 8):
        neuron[i][8] = 1
        neuron[i][1] = 1
    for i in range(1, 4):
        neuron[i][7] = 1
        neuron[i][2] = 1
    for i in range(1, 3):
        for j in range(3, 7):
            neuron[i][j] = 1
    return neuron

def plotNeuron(neuron, title: str = "Neuron Grid") -> None:
    offX = [x for x in range(len(neuron)) for y in range(len(neuron)) if neuron[x][y] == -1]
    offY = [y for x in range(len(neuron)) for y in range(len(neuron)) if neuron[x][y] == -1]
    onX = [x for x in range(len(neuron)) for y in range(len(neuron)) if neuron[x][y] != -1]
    onY = [y for x in range(len(neuron)) for y in range(len(neuron)) if neuron[x][y] != -1]
    plt.figure().set_figwidth(10)
    plt.figure().set_figheight(6)    
    plt.scatter(offX, offY, color='r', linewidths=8)
    plt.scatter(onX, onY, color='b', linewidths=8)
    plt.title(title)
    plt.show()    


def makeJXX(neuron) -> any:
    return neuron

def main():
    neuronOff = emptyNeuron()
    plotNeuron(neuronOff, "Completely Off Neuron Grid")
    neuronA = makeLetterA()
    plotNeuron(neuronA, "Letter A Grid")
    neuronB = makeLetterB()
    plotNeuron(neuronB, "Letter B Grid")
    neuronC = makeLetterC()
    plotNeuron(neuronC, "Letter C Grid")


if __name__ == "__main__":
    main()
# %%
