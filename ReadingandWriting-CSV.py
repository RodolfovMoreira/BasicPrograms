linha_recebida = []
linha_processada = []
lista_completa = []
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
		print(line)
		linha_recebida = [x.strip() for x in line.split(',')] #Creating an list witout commas
		print(linha_recebida)
		linha_processada = [int(i) for i in linha_recebida] #Transforming list into integer
		

		lista_completa.append(linha_processada)





file = open('testfile.txt','a') 
mat,bolsa,periodo = retorna_valorpraimpressao(linha_processada)
file.write(mat + ',' + bolsa + ',' + periodo + '\n')  
file.close() 