# SAT-compiler-DPLL-solver
Three programs consisting of Frontend, DPLLsolver, and Backend. 
Input comes from "mazeinput.txt" which should provide a specified maze problem and the number of steps for the desired path to obtain all the treasures. For instance, a maze that looks like 
## Frontend 
Outputs CNF clauses for a maze problem taken from "mazeinput.txt" to be put into DPLLsolver as well as a key at the bottom to be used for Backend
## DPLLsolver
generates the truth values of the generated atoms from Frontend and leaves the key at the bottom untouched for Backend to use
## Backend
Backend uses the key from frontend and the atoms' values to find the path through the maze in the specified steps given from "mazeinput.txt". 
Outputs to a file "path.txt"
