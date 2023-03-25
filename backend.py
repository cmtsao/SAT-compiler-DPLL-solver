def generate():
    input=open("DPLLoutput.txt", "r")
    values={}
    atommap={}
    for line in input:
        if line.strip()=='0':
            break
        item= line.split()
        values[item[0]]= item[1] 
    for line in input:

        item=line.split()
        atom, *rest= item
        atommap[atom]= " ".join([*rest])
    input.close()

    output=open("path.txt", "w")
    if len(values)==0:
        output.write("NO SOLUTION")
    else:
        for atom in values.keys():
            if atommap.get(atom) is not None and values[atom] == "T":
                output.write(atommap[atom][0: atommap[atom].index(" ")] + " ")
    
    output.close()
    
def main():
    generate()

main()