import sys
from getdata import *
def deBrujin(data, k, d):
	matrix = []
	v = int(k)-1
	for seq in data:
		vet = seq.split('|')
		matrix.append(vet)
	matrix_splited = []
	for comp in matrix:
		aux = []
		for seq in comp: 
			vet1 = []
			vet2 = []
			vet3 = []
			vet1.append(seq[:v]) 
			vet2.append(seq[1:]) 
			vet3.append(vet1)
			vet3.append(vet2)
			aux.append(vet3)
		matrix_splited.append(aux)
	for tup in matrix_splited:
		print(tup)

	sort_list = []
	final = []
	head = 0
	last = 0
	i = 0
	for t in matrix_splited:
		flag = 0 
		for t2 in matrix_splited:
			if (t[0][0] == t2[0][1] and t[1][0] == t2[1][1]):
				flag = 1
				break
		if flag == 0:
			head = i
			break
		i+=1			
	sort_list.append(matrix_splited[head])
	matrix_splited.remove(matrix_splited[head])			
	i = 0
	for t in matrix_splited:
		flag = 0
		for t2 in matrix_splited:
			if (t[0][1] == t2[0][0] and t[1][1] == t2[1][0]):
				flag = 1
				break
		if flag == 0:
			last = i
			break
		i+=1					
	final.append(matrix_splited[last])
	matrix_splited.remove(matrix_splited[last])	

	n = 0
	i = 0
	print(sort_list)
	while (len(matrix_splited) >= n):
		vet = []
		vet = sort_list[n]
		print(vet[0][1])
		print(vet[1][1])
		for tup in matrix_splited:
			if  (vet[0][1] == tup[0][0] and vet[1][1] == tup[1][0]):
				print(tup[0][0])
				print(tup[1][0])
				print(tup)
				sort_list.append(tup)
				break
		n+=1
	print(final)
	sort_list.append(final[0])
	vertex_list = []
	for tup in sort_list:
		aux = []
		aux.append(tup[0][0])
		aux.append(tup[1][0])

		vertex_list.append(aux)
	aux = []	
	aux.append(sort_list[-1][0][1])
	aux.append(sort_list[-1][1][1])
	vertex_list.append(aux)

	edge_list = []
	i = 0
	for seq in vertex_list:
		if i+1 == len(vertex_list):
			break
		aux = []
		obj = vertex_list[i+1]
		aux.append(seq[0][0]+obj[0][0][-1])
		aux.append(seq[1][0]+obj[1][0][-1])
		print(aux)
		edge_list.append(aux)	
		i+=1
	result = ""
	for seq in edge_list:
		result += seq[0][0]
	result += edge_list[-1][0][1:]
	aux = ""
	for i in range(len(edge_list)-2,(len(edge_list)-2)-int(d), -1):
		aux += edge_list[i][1][0]
	result += aux[::-1]
	result += edge_list[-1][1]
	return result		

def main():
	s1 = ""
	s2 = ""
	if sys.version_info.major == 2:
		fasta = raw_input("Entre com o nome do arquivo.fasta:")
	elif sys.version_info.major == 3:
		fasta = input("Entre com o nome do arquivo.fasta: ")

	fst = Fasta_r()	

	while fst.setFile(fasta) == False:
		if sys.version_info.major == 2:
			fasta = raw_input("Entre com o nome do arquivo.fasta:: ")
		elif sys.version_info.major == 3:
			fasta = input("Entre com o nome do arquivo.fasta: ")

	with open('out.fasta', 'w+') as file_w:
		file_w.write(deBrujin(fst.getData(), fst.getK(), fst.getD()))	
main()
