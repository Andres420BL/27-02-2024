import os 
os.system('')
#Elaborar un programa en Python que permita gestionar una competencia de atletismo en la cual se presentan 2 participantes, los cuales deben recorrer varias etapas y en cada etapa se debe seleccionar el participante e ingresar la cantidad de kilómetros que ha recorrido, el sistema debe permitir ingresar datos hasta que se seleccione la opción de finalizar competencia donde debe decir cuantos kilómetros ha recorrido cada participante.
print ('Competencia de atletismo')

cons1 = 'Participante 1'
cons2 = 'Participante 2'


var_corredor = input('Nombre del corredor ')
var_numerocorredor = input('NUMERO DEL CORREDOR')

var_corredor = input('Nombre del corredor ')
var_numerocorredor = input('Numero del corredor')
var_acumuladoP1int = 0
var_acumuladoP2int = 0
controlInt = True

while controlInt == True:
    opcionint = int(input('1'),var_corredor,'no',var_numerocorredor,'',var_acumuladoP1int,
    var_numerocorredor,'NO',var_numerocorredor,'',var_acumuladoP2int,'Km')
    opcionint = int(input('Selccione el partcipante-> '))


print('iNGRESE LOS KILOMETROS RECORRIDOS EN LA ETAPA 1')
VAR_etapa1par1 = int(input('Kilometros recorridos por el participante 1'))

VAR_etapa1par2 = int(input('Kilometros recorridos por el participante 2'))

import os 
os.system("cls")

print('iNGRESE LOS KILOMETROS RECORRIODS EN LA ETAPA 2')
VAR_etapa2par1 = int(input('Kilometros recorridos por el participante 1'))
VAR_etapa2par2 = int(input('Kilometros recorridos por el participante 2'))
import os 
os.system("cls")

print('iNGRESE LOS KILOMETROS RECORRIODS EN LA ETAPA 3')
VAR_etapa3par1 = int(input('Kilometros recorridos por el participante 1'))
VAR_etapa3par2 = int(input('Kilometros recorridos por el participante 2'))
import os 
os.system("cls")

print('iNGRESE LOS KILOMETROS RECORRIODS EN LA ETAPA 4')
VAR_etapa4par1 = int(input('Kilometros recorridos por el participante 1'))
VAR_etapa4par2 = int(input('Kilometros recorridos por el participante 2'))
import os 
os.system("cls")

print('iNGRESE LOS KILOMETROS RECORRIODS EN LA ETAPA 5')
VAR_etapa5par1 = int(input('Kilometros recorridos por el participante 1'))
VAR_etapa5par2 = int(input('Kilometros recorridos por el participante 2'))
import os 
os.system("cls")

var_total1 =(VAR_etapa1par1 + VAR_etapa2par1 + VAR_etapa3par1 + VAR_etapa4par1 + VAR_etapa5par1) 
var_total2 = (VAR_etapa1par2+VAR_etapa2par2+VAR_etapa3par2+VAR_etapa4par2+VAR_etapa5par2)

if var_total1 > var_total2:
    print('El participante 1 ha ganado con un total de',var_total1,'km recorriods')
    
else:
    print('El participante 2 ha ganado con un total de',var_total2,'KM recorridos')