# %%
from matplotlib import pyplot as plt
import numpy as np
from itertools import product

ARR_SIZE = 10

def emptyNeuron() -> any:
    neuronOff = np.ones([ARR_SIZE, ARR_SIZE]) * -1
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
    jInteractXX = np.ones([ARR_SIZE, ARR_SIZE, ARR_SIZE, ARR_SIZE]) * -1
    for i, j, k, l in product(range(ARR_SIZE), repeat=4):
        jInteractXX[i][j][k][l] = neuron[i][j] * neuron[k][l]
    return jInteractXX

def makeJXY(neuron1, neuron2) -> any:
    jInteract11 = makeJXX(neuron1)
    jInteract22 = makeJXX(neuron2)
    jInteractXY = np.ones([ARR_SIZE, ARR_SIZE, ARR_SIZE, ARR_SIZE]) * -1
    for i, j, k, l in product(range(ARR_SIZE), repeat=4):
        jInteractXY[i][j][k][l] = (jInteract11[i][j][k][l] + jInteract22[i][j][k][l]) / 2
    return jInteractXY

def calculateEnergy(jInteract, neuron) -> float:
    energy: float = 0
    for i, j, k, l in product(range(ARR_SIZE), repeat=4):
        energy -= (jInteract[i][j][k][l]*neuron[i][j]*neuron[k][l])
    return energy

def makeRandLetter(neuron) -> any:
    randNeuron = neuron
    numIterations = 50
    for i in range(numIterations):
        randSwitch = np.random.randint(0, 10, [1, 2])
        randNeuron[randSwitch[0][0]][randSwitch[0][1]] *= -1
    return randNeuron

def monteCarlo(neuron, jInteract) -> any:
    newA = neuron
    monteSteps = 1
    eMonte = 0
    for n in range(monteSteps):
        for k, l in product(range(ARR_SIZE), repeat=2):
            for i, j in product(range(ARR_SIZE), repeat=2):
                eMonte -= (jInteract[i][j][k][l]*newA[i][j]*newA[k][l])
            if eMonte > 0: #Monte Carlo flip method: T = 0, flip
                newA[k][l] = -1 * newA[k][l]
            eMonte = 0
    return newA

def basicInteractionMatrixStuff() -> None:
    neuronOff = emptyNeuron()
    plotNeuron(neuronOff, "Completely Off Neuron Grid")
    neuronA = makeLetterA()
    plotNeuron(neuronA, "Letter A Grid")
    neuronB = makeLetterB()
    plotNeuron(neuronB, "Letter B Grid")
    neuronC = makeLetterC()
    plotNeuron(neuronC, "Letter C Grid")
    jInteractAA = makeJXX(neuronA)
    jInteractAB = makeJXY(neuronA, neuronB)
    print(f"Energy of A Neuron with AA Interaction Matrix: {calculateEnergy(jInteractAA, neuronA)}")
    randNeuron = makeRandLetter(neuronA)
    plotNeuron(randNeuron, "Randomly Generated Neuron")
    randNeuron = monteCarlo(randNeuron, jInteractAA)
    plotNeuron(randNeuron, "Once-Random Neuron Now Converted Into An A")
    randNeuron = makeRandLetter(neuronA)
    plotNeuron(randNeuron, "Randomly Generated Neuron")
    randNeuron = monteCarlo(randNeuron, jInteractAB)
    plotNeuron(randNeuron, "Once-Random Neuron Now Converted Into \"A\" With AB Interaction Matrix")    
    randNeuron = makeRandLetter(neuronB)
    plotNeuron(randNeuron, "Randomly Generated Neuron")
    randNeuron = monteCarlo(randNeuron, jInteractAB)
    plotNeuron(randNeuron, "Once-Random Neuron Now Converted Into \"B\" With AB Interaction Matrix")         

def abcInteractionMatrix() -> None:
    alpha: float = 0.67
    beta: float = 1 - alpha
    jAB = makeJXY(makeLetterA(), makeLetterB())
    jCC = makeJXX(makeLetterC())
    jABC = jAB * alpha + jCC * beta
    monteA = monteCarlo(makeRandLetter(emptyNeuron()), jABC)
    monteB = monteCarlo(makeRandLetter(emptyNeuron()), jABC)
    monteC = monteCarlo(makeRandLetter(emptyNeuron()), jABC)
    plotNeuron(monteA, "Letter A")
    plotNeuron(monteB, "Letter B")
    plotNeuron(monteC, "Letter C")

def main():
    basicInteractionMatrixStuff()
    #abcInteractionMatrix()
    return

if __name__ == "__main__":
    main()
# %%
