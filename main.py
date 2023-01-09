import os
from grammarRead import read_grammar_from_file
from recursive_descendent import recursive_descent

path_to_grammar = os.path.join(os.getcwd(), 'language_grammar.txt')

grammar = read_grammar_from_file(path_to_grammar)
print(grammar)
f = open('fip.in', 'r')
input = f.readline().strip().split(" ")
res, prodRules = recursive_descent(grammar, input)
print(res, prodRules)


