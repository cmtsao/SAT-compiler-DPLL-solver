class Node:
    def __init__(self, name):
        self.name=name
        self.treasure=[]
        self.neighbors=[]
    
    def getname(self):
        return self.name
    
    def addtreasure(self, Treasure):
        self.treasure.append(Treasure)
    
    def addneighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def gettreasures(self):
        return self.treasure
    
    def getneighbors(self):
        return self.neighbors

class Maze:
    def __init__(self):
        maxsteps=0
        nodeslist=[]
        treasurelist=[]
        treasuremap={}

    def getinput(self):
        input= open("mazeinput.txt", "r")
        nodemap={}
        self.nodes= input.readline().split()
        self.treasurelist=input.readline().split()
        self.maxsteps=input.readline()
        self.treasuremap={}
        self.nodelist=[]
        for n in self.nodes:
            node= Node(n)
            nodemap.update({n: node})
            self.nodelist.append(node)
        for treasure in self.treasurelist:
            self.treasuremap[treasure]=[]
        for item in input:
            nodedets= item.split()
            node=nodemap[nodedets[0]]
            i=2
            while not nodedets[i]== "NEXT":
                self.treasuremap[nodedets[i]].append(node)
                node.addtreasure(nodedets[i])
                i+=1
            i+=1
            while i<len(nodedets):
                node.addneighbor(nodemap[nodedets[i]])
                i+=1
        input.close()
        
    def getmaxsteps(self):
        return int(self.maxsteps)
        
    def getnodes(self):
        return self.nodelist
    
    def gettreasurelist(self):
        return self.treasurelist
    
    def gettreasuremap(self):
        return self.treasuremap
    
def oneplaceattime(atommap, maxsteps, nodelist):
    oneplace=[]
    i=0
    while i<=maxsteps:
        j=0
        while j< len(nodelist)-1:
            k=j+1
            while k<len(nodelist):
                oneplace.append("-" + str(atommap[nodelist[j].getname() + " " + str(i)]) + " -" + str(atommap[nodelist[k].getname() + " " + str(i)]))
                k+=1
            j+=1
        i+=1
    return oneplace
  
def edgemove(atommap, maxsteps, nodelist):
    edgemoves=[]
    i=0
    while i< len(nodelist):
        j=0
        while j<maxsteps:
            neighbors=nodelist[i].getneighbors()
            neighboratoms=""
            k=0
            while k<len(neighbors):
                neighboratoms= " ".join([neighboratoms, str(atommap[neighbors[k].getname() + " " + str(j+1)])])
                k+=1
            edgemoves.append("-" + str(atommap[nodelist[i].getname() + " " + str(j)]) + neighboratoms)
            j+=1
        i+=1
    return edgemoves

def obtaintreasure(atommap, hasmap, maxsteps, nodelist):
    obtaintreasure=[]
    i=0
    while i< len(nodelist):
        j=0
        while j<= maxsteps:
            treasurelist=nodelist[i].gettreasures()
            k=0
            while k<len(treasurelist):
                obtaintreasure.append("-" + str(atommap[nodelist[i].getname() + " " + str(j)]) + " " + str(hasmap[treasurelist[k] + " " + str(j)]))
                k+=1
            j+=1
        i+=1
    return obtaintreasure

def getonce(hasmap, maxsteps, treasurelist):
    getonce=[]
    i=0
    while i< maxsteps:
        j=0
        while j< len(treasurelist):
            getonce.append("-" + str(hasmap[treasurelist[j] + " " + str(i)]) + " " + str(hasmap[treasurelist[j] + " " + str(i+1)]))
            j+=1
        i+=1
    return getonce

def attreasure(treasuremap, atommap, hasmap, maxsteps, treasurelist):
    attreasure=[]
    i=0
    while i< maxsteps:
        j=0
        while j< len(treasurelist):
            treasureatoms=""
            k=0
            while k< len(treasuremap[treasurelist[j]]):
                treasureatoms=" ".join([treasureatoms, str(atommap[treasuremap[treasurelist[j]][k].getname() + " " + str(i+1)])])
                k+=1
            attreasure.append(str(hasmap[treasurelist[j] + " " + str(i)]) + " -" + str(hasmap[treasurelist[j] + " " + str(i+1)]) + treasureatoms)
            j+=1
        i+=1
    return attreasure

def atstart(atommap):
    start=[]
    start.append(str(atommap["START 0"]))
    return start

def notreasurestart(hasmap, treasurelist):
    notreastart=[]
    i=0
    while i <len(treasurelist):
        notreastart.append("-" + str(hasmap[treasurelist[i] + " 0"]))
        i+=1
    return notreastart

def hasall(hasmap, maxsteps, treasurelist):
    hasalltrea=[]
    i=0
    while i< len(treasurelist):
        hasalltrea.append(str(hasmap[treasurelist[i] + " " + str(maxsteps)]))
        i+=1
    return hasalltrea

def generate():
    atoms=1
    maze=Maze()
    maze.getinput()
    i=0
    atommap={}
    hasmap={}
    maxsteps=maze.getmaxsteps()
    nodelist=maze.getnodes()
    treasurelist=maze.gettreasurelist()
    while i<=maxsteps:
        j=0
        while j<len(nodelist):
            atommap.update({nodelist[j].getname() + " " + str(i): atoms})
            atoms+=1
            j+=1
        i+=1
    i=0
    while i<= maxsteps:
        j=0
        while j<len(maze.gettreasurelist()):
            hasmap.update({maze.gettreasurelist()[j] + " " + str(i): atoms})
            atoms+=1
            j+=1
        i+=1
    constraints=[]
    constraints.extend(oneplaceattime(atommap, maxsteps, nodelist))
    constraints.extend(edgemove(atommap, maxsteps, nodelist))
    constraints.extend(obtaintreasure(atommap, hasmap, maxsteps, nodelist))
    constraints.extend(getonce(hasmap, maxsteps, treasurelist))
    constraints.extend(attreasure(maze.gettreasuremap(), atommap, hasmap, maxsteps, treasurelist))
    constraints.extend(atstart(atommap))
    constraints.extend(notreasurestart(hasmap, treasurelist))
    constraints.extend(hasall(hasmap, maxsteps, treasurelist))
    return atommap, constraints

    
def main():
    atommap, constraints= generate()
    output= open("DPLLinput.txt", "w")
    for clause in constraints:
        output.write(clause)
        output.write("\n")

    output.write("0" + "\n")
    for string in atommap.keys():
        output.write(str(atommap[string]) + " " + string + "\n")
    output.close()
    
main()
