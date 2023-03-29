# SAT-compiler-DPLL-solver
Three programs consisting of Frontend, DPLLsolver, and Backend. 
Input comes from "mazeinput.txt" which should provide a specified maze problem and the number of steps for the desired path to obtain all the treasures. For instance, a maze that looks like ![image](https://user-images.githubusercontent.com/105821443/228684339-5aee68b6-4c38-480f-bccf-d4937920abc7.png) <br />
would be: <br />
> START A B C D E F G  H <br />
GOLD WAND RUBY <br />
5 <br />
START TREASURES NEXT A C <br />
A TREASURES GOLD NEXT START B D<br />
B TREASURES RUBY NEXT A D E<br />
C TREASURES RUBY NEXT START D F G<br />
D TREASURES NEXT A B C E G<br />
E TREASURES NEXT B D H<br />
F TREASURES WAND NEXT C G<br />
G TREASURES NEXT C D F H<br />
H TREASURES GOLD WAND NEXT G<br />
>
where the first line is all the nodes in the maze, the second is all the treasures present in the maze, and the third line is the desired number of steps to obtain all the treasures. <br />
Each subsequent line is the node with any present treasures after the TREASURES keyword ending the treasures list with the NEXT keyword and the a list of neighboring nodes. 
## Frontend 
Outputs CNF clauses for a maze problem taken from "mazeinput.txt" to be put into DPLLsolver as well as a key at the bottom to be used for Backend
## DPLLsolver
Generates the truth values of the generated atoms from Frontend and leaves the key at the bottom untouched for Backend to use
## Backend
Backend uses the key from frontend and the atoms' values to find the path through the maze in the specified steps given from "mazeinput.txt". 
Outputs to a file "path.txt"
