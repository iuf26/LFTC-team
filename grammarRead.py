# from grammar import Grammar
# from production import Production
#
# def read_grammar_from_file(in_file):
#     """
#     Function to read a grammar from file
#     @param: in_file - file to read the grammar from
#     """
#     with open(in_file, "r") as f_d:
#         line = f_d.readline().strip()
#         productions = []
#         terminals = line.split(' ')
#         line = f_d.readline().strip()
#         non_terminals = line.split(' ')
#         line = f_d.readline().strip()
#         start_sym = line
#         line = f_d.readline().strip()
#         while line != "":
#             segments = line.split('->')
#             productions_on_line = segments[1].split('|')
#             for prod in productions_on_line:
#                 production = Production(segments[0].replace(" ", ""), prod.split())
#                 productions.append(production)
#             line = f_d.readline().strip()
#         return Grammar(start_sym, terminals, non_terminals, productions)

from grammar import Grammar
from production import Production


def read_grammar_from_file(in_file):
    """
    Function to read a grammar from file
    @param: in_file - file to read the grammar from
    """
    #TO DO: Extract terminals and non terminals
    with open(in_file, "r") as f_d:

        #liste pentru fiecare simbol ce apare in partea dreapta respectiv stanga a productiilor
        left_part_of_production_list = []
        right_part_of_production_list = []
        productions = []
        terminals = []
        non_terminals = []

        line = f_d.readline().strip()
        start_sym = line[0]
        while line != "":
            segments = line.split('->')

            # aici adaugam in liste fiecare symbol din stanga productiilor care nu este deja in lista
            left_part_of_production = segments[0].split(" ")
            for symbol in left_part_of_production:
                if (left_part_of_production_list.count(symbol)==0 and symbol!=""):
                    left_part_of_production_list.append(symbol)

            #aici adaugam in liste fiecare symbol din dreapta productiilor care nu este deja in lista
            right_part_of_production = segments[1].split(" ")
            for symbol in right_part_of_production:
                if (right_part_of_production_list.count(symbol)==0 and symbol!=""):
                    right_part_of_production_list.append(symbol)

            productions_on_line = segments[1].split('|')
            for prod in productions_on_line:
                production = Production(segments[0].replace(" ", ""), prod.split())
                productions.append(production)
            line = f_d.readline().strip()

        # orice symbol din partea stanga stim sigur ca e neterminal => lista de neterminale = lista simboluri stanga
        # pentru terminali verificam toata lista de simboluri dreapta si excludem ce apare si in stanga si rezulta lista de terminali
        for symbol in right_part_of_production_list:
            if (left_part_of_production_list.count(symbol)>0):
                right_part_of_production_list.remove(symbol)

        non_terminals = left_part_of_production_list
        terminals = right_part_of_production_list

        for prod in productions:
            idx = 0
            while idx < len(prod.get_right_term()) - 1:
                if prod.get_right_term()[idx] in non_terminals and prod.get_right_term()[idx + 1] in terminals:
                    print(Grammar(start_sym, terminals, non_terminals, productions))
                    raise ValueError("Nu se accepta gramatici recursive la stanga")
                idx += 1




        return Grammar(start_sym, terminals, non_terminals, productions)