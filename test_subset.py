
in_file = open("PPI_Network_Kept.txt")

in_file2 = open("MFO_All.txt")

Notes_out = open("PPI_Nodes.json", "w")

Links_out = open("PPI_Links.json", "w")


#step 1: find uniq nodes
unq = []
for line in in_file:
	clen = line.strip().split("\t")
	if clen[0] not in unq:
		unq.append(clen[0])
	if clen[1] not in unq:
		unq.append(clen[1])

ii=0
dic = {}
for item in unq:
	dic[item] = ii
	ii+=1


goterm = {}
for line in in_file2:
	clen = line.strip().split("\t")
	if clen[0] not in goterm:
		goterm[clen[0]] = clen[1]+" ("+clen[2]+")"
	else:
		goterm[clen[0]] = goterm[clen[0]]+", "+clen[1]+" ("+clen[2]+")"

in_file.close()
in_file = open("PPI_Network_Kept.txt")
for line in in_file:
	clen = line.strip().split("\t")
	if clen[0] not in goterm:
		goterm[clen[0]] = "No term"


in_file.close()
in_file = open("PPI_Network_Kept.txt")
claus = []
for line in in_file:
	claus.append(line.strip().split("\t"))

in_file.close()
in_file = open("PPI_Network_Kept.txt")
claus2 = []
for line in in_file:
	claus2.append(line.strip().split("\t"))

clster = {}
kk=0
for item in claus:
	item_curr = item[0]
	for item2 in claus2:
		if item2[0] == item_curr:
			clster[item2[0]] = kk
			clster[item2[1]] = kk
	kk+=1
in_file.close()


# #step 2: make the nodes in json format

jj=0
out_file.write("[\n")
out_file.write("[\n")
for item in unq:
	if item in goterm:
		Nodes_out.write('{\n"children": null,\n"cluster": '+str(clster[item])+',\n"id": '+str(dic[item])+',\n"count": '+'"'+str(goterm[item])+'"'+',\n"size": 125.0,\n"word": "'+str(item)+'"\n},'+"\n")
		jj+=1

Nodes_out.close()


 in_file.close()
 in_file = open("PPI_Network_Kept.txt")
 jj=0
 for line in in_file:
 	clen = line.strip().split("\t")
 	Links_out.write("[\n"+str(dic[clen[0]])+",\n"+str(dic[clen[1]])+",\n"+str(jj)+"\n],\n")
 	jj+=1

Links_out.close()



