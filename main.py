import os
from grammarRead import read_grammar_from_file
from recursive_descendent import recursive_descent

path_to_grammar = os.path.join(os.getcwd(), 'grammarInput.txt')

grammar = read_grammar_from_file(path_to_grammar)
print(grammar)
f = open('D:\\FACULTATE-AN3-SEM1\\LFTC\\LABS\\Lab5-peEchipe\\secventa.in', 'r')
input = f.readline().strip().split(" ")
print(input)
recursive_descent(grammar, input)


