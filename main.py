import os
from grammarRead import read_grammar_from_file
from recursive_descendent import recursive_descent

path_to_grammar = os.path.join(os.getcwd(), 'grammarInput.txt')

grammar = read_grammar_from_file(path_to_grammar)
print(grammar)
f = open('C:\\Users\\Horia\\PycharmProjects\\LFTC-TeamProject\\LFTC-team\\secventa.in', 'r')
input = f.readline().strip().split(" ")
print(input)
recursive_descent(grammar, input)


