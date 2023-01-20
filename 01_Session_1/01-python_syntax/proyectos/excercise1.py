
import numpy_financial as np

# Arguments

proyectos = ["proyecto1.txt","proyecto2.txt","proyecto3.txt","proyecto4.txt","proyecto5.txt"]

# Functions

def tir_calc(flujos):
    
    tir = round(np.irr(flujos), 5)
    
    return tir


lista_resultados = []

# Read all documents and extract data

for proyecto in proyectos:
    
    f = open(proyecto)
    
    cash_flows = f.readlines()
    
    cash_flows = cash_flows[0].split(",")
    
    tir = tir_calc(cash_flows)
    
    dict = {
        "proyecto": proyecto,
        "cash_flows": cash_flows,
        "Tir": tir}
    
    lista_resultados.append(dict)
    

tirs = []

# Read data and extract TIRS

for i in lista_resultados:
    
    tirs.append(i["Tir"])
    
max_tir = max(tirs)

# Create and fill in the report file

g = open("resultado_final.txt","w")

for i in lista_resultados:
    
    g.write(f"El proyecto {i['proyecto']} tiene una TIR: {i['Tir']} \n")

# Print data with maximum TIR

for i in lista_resultados:
    
    if(i["Tir"] == max_tir):
       
        g.write(f"\nEl proyecto {i['proyecto']} es el que tiene una mayor TIR: {i['Tir']}\n")
        g.write(f"Los cash flows del proyecto son: {i['cash_flows']}")

g.close()
    



    
