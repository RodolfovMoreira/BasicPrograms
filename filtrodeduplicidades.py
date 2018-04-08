linha_recebida = []
linha_processada = []
lista_completa = []
lista_final = []
mat = 0
bolsa = 0
periodo = 0

def retorna_valorpraimpressao(linha):
	a = str(linha[0])
	b = str(linha[1])
	c = str(linha[2])
	return a,b,c

with open('censo1.csv', encoding="utf8") as fp:
	for line in fp:
		linha_recebida = [x.strip() for x in line.split(',')] #Creating an list witout commas
		linha_processada = [int(i) for i in linha_recebida] #Transforming list into integer
		lista_completa.append(linha_processada)

elemento = 0
limite = len(lista_completa)
while (elemento < limite):
	if(elemento == len(lista_completa)-1):
		break
	if(lista_completa[elemento][0] == lista_completa[elemento+1][0]):
		lista_completa[elemento][2] = 3
		lista_final.append(lista_completa[elemento])
		while(lista_completa[elemento][0] == lista_completa[elemento+1][0]):
			print(lista_completa[elemento],'e',lista_completa[elemento+1])
			elemento = elemento + 2
	else:
		lista_final.append(lista_completa[elemento])
		elemento = elemento + 1

file = open('testfile.txt','a') 

for elemento in lista_final:
	mat,bolsa,periodo = retorna_valorpraimpressao(elemento)
	file.write(mat + ',' + bolsa + ',' + periodo + '\n')  

file.close()