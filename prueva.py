from turtle import pd


Día = int(input("Ingrese el día de su nacimiento [1-31]: )"))
Mes = int(input("Ingrese el mes de su nacimiento [1-12]: )"))
Año = int(input("Ingrese el año de su nacimiento [1-31]: )"))

import numpy as np
import pandas as pd
pd.__version__
Fechas = 'Paso.csv'
df = pd.read_csv(Fechas)
df

if __name__ == '__main__':
    from pycallgraph import PyCallGraph 
    from pycallgraph.output import GraphvizOutput
    with PyCallGraph(output = GraphvizOutput()):
        main()