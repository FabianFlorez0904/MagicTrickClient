class cartaClass():

    def __init__(self, nombre, numCarta, cartas):
        self.nombre = nombre
        self.cartas = cartas
        self.numCarta = numCarta

    def imprimirCarta(self):
        print(
            "-------------------------------------------------\n",
            "{: ^50}\n".format(self.nombre),
            "-------------------------------------------------",sep=''
        )
        while True:
            j = 0
            for i in range(len(self.cartas)):
                if j == 8:#round(len(self.cartas)/6):
                    print()
                    j = 0     
                print("| {: >3} ".format(self.cartas[i]), end='')
                j += 1
            print("\n-------------------------------------------------\n")
            break
    def getNumCarta(self):
        return self.numCarta
    
    def getCartas(self):
        return self.cartas

    def encontrarCarta(self,numeroDeCarta):
        if numeroDeCarta in self.cartas:
            return True
        else:
            return False
        
cartaUno = cartaClass(
    "Carta 1",
    1,
    [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99]
)
cartaDos = cartaClass(
    'Carta 2',
    2,
    [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62,63,66,67,70,71,74,75,78,79,82,83,86,87,90,91,94,95,98,99]
)
cartaTres = cartaClass(
    'Carta 3',
    3,
    [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31,36,37,38,39,44,45,46,47,52,53,54,55,60,61,62,63,68,69,70,71,74,75,78,79,84,85,86,87,92,93,94,95,100]
)
cartaCuatro = cartaClass(
    'Carta 4',
    4,
    [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,63,72,73,74,75,76,77,78,79,88,89,90,91,92,93,94,95]
)
cartaCinco = cartaClass(
    'Carta 5',
    5,
    [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,80,81,82,83,84,85,86,87,88,89,90,9,92,93,94,95]
)
cartaSeis = cartaClass(
    'Carta 6',
    6,
    [32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,96,97,98,99,100]
)
cartaSiete = cartaClass(
    'Carta 7',
    7,
    [64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
)