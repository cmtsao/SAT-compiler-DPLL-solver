import copy

def getinput():
    input= open("DPLLinput.txt", "r")
    afterzero= False
    clauses=[]
    remainder=[]
    for item in input:
        item= item.strip()
        if item == '0':
            afterzero=True
            remainder.append(item)
        elif afterzero==True:
            remainder.append(item)
        else:
            literal=[int(n) for n in item.split()]
            clauses.append(literal)
    input.close()
    return (clauses, remainder)

def findliteralsnum(clauses):
    literalnum=0
    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            literalnum=max(literalnum, abs(clauses[i][j]))
    return literalnum
       
def propagate(clauses, values, literal, bool):
    values.update({literal: bool})
    deleted=0
    i=0
    while i< len(clauses):
        j=0
        while j < len(clauses[i]):
            if (literal==clauses[i][j] and bool) or (literal+clauses[i][j]==0 and not bool):
                clauses.pop(i)
                i-=1
                deleted+=1
                break
            elif (literal+ clauses[i][j]==0 and bool) or (literal==clauses[i][j] and not bool):
                clauses[i].pop(j)
                j-=1
            j+=1
        i+=1
    return deleted

def easycases(clauses, values, literalnum):
    easyfound=False
    i=0
    while i<len(clauses):
        if len(clauses[i])==1:
            easyfound=True
            if clauses[i][0]<0:
                i=max(0, i-propagate(clauses, values, abs(clauses[i][0]), False))
            else:
                i=max(0, i-propagate(clauses, values, abs(clauses[i][0]), True))
        i+=1
    literalsnum=literalnum
    for x in range(1, literalsnum+1):
        possiblepure=x
        literalfound= False
        ispurelit= True
        j=0
        while j < len(clauses) and ispurelit:
            k=0
            while k < len(clauses[j]) and ispurelit:
                if not literalfound and (abs(clauses[j][k]) == possiblepure):
                    possiblepure=clauses[j][k]
                    literalfound=True
                elif literalfound and (abs(clauses[j][k])==abs(possiblepure)):
                    if clauses[j][k]==possiblepure:
                        k+=1
                        continue
                    else:
                        ispurelit=False
                k+=1
            j+=1
        if ispurelit and literalfound:
            if possiblepure <0:
                propagate(clauses, values, abs(possiblepure), False)
            else:
                propagate(clauses, values, abs(possiblepure), True)
            easyfound=True
    return easyfound


def solver(clauses, values, literalnum):
    literalsnum=literalnum
    while True:
        if len(clauses) == 0:
            return True
        for clause in clauses:
            if len(clause)==0:
                return False
        if not easycases(clauses, values, literalsnum):
            break
    clausecopy= copy.deepcopy(clauses)
    valuecopy=copy.deepcopy(values)
    for i in range(1, literalsnum+1):
        if i not in values.keys():
            propagate(clausecopy, valuecopy, abs(i), True)
            break  
    if solver(clausecopy, valuecopy, literalsnum):
        values.update(valuecopy)
        return True   
    clausecopy.clear()
    clausecopy= copy.deepcopy(clauses)
    valuecopy.clear()
    valuecopy= copy.deepcopy(values)
    propagate(clausecopy, valuecopy, i, False)
    if solver(clausecopy, valuecopy, literalsnum):
        values.update(valuecopy)
        return True

    return False


def main():
    inputtuple= getinput()
    clauses, remainder= inputtuple
    literalnum= findliteralsnum(clauses)
    values={}
    output= open("DPLLoutput.txt", "w")
    if solver(clauses, values, literalnum):
        for i in range(1, literalnum+1):
            if i not in values.keys():
                values[i]= True
        for x in sorted(values.keys()):
            string=str(x)
            output.write(string + " " + ("T" if values[x] else "F") + "\n")
        
    for string in remainder:
        output.write(string + "\n")

    output.close()

        
main()    