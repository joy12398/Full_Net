
in_file2 = open("MFO_LABELS.txt")

in_file3 = open("MFO_Guilty_Terms_All.txt")


out_file = open("MFO_All.txt", "w")

number = {}
for line in in_file3:
	clen = line.strip().split("\t")
	number[clen[0]] = clen[1]


for line in in_file2:
	clen = line.strip().split("\t")
	if clen[1] in number:
		out_file.write(clen[0]+"\t"+clen[1]+"\t"+number[clen[1]]+"\n")


