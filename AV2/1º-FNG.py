def rename_nonterminals(grammar):
    print('')
    print('Renomeando os não terminais:')
    nonterminals = list(grammar.keys())
    renamed_nonterminals = {}
    next_number = 1

    for nonterminal in nonterminals:
        if nonterminal.startswith('A') and nonterminal[1:].isdigit():
            renamed_nonterminals[nonterminal] = nonterminal
        else:
            renamed_nonterminals[nonterminal] = f'A{next_number}'
            next_number += 1

    for nonterminal in renamed_nonterminals:
        productions = grammar[nonterminal]
        new_productions = []

        for production in productions:
            new_production = production

            for nonterm, renamed_nonterm in renamed_nonterminals.items():
                new_production = new_production.replace(nonterm, renamed_nonterm)

            new_productions.append(new_production)

        grammar[renamed_nonterminals[nonterminal]] = new_productions
        del grammar[nonterminal]
    print_productions(grammar)

def print_productions(grammar):
    print('')
    for nonterminal, productions in grammar.items():
        print(f"{nonterminal} -> ", end='')
        for i, production in enumerate(productions):
            if i == len(productions) - 1:
                print(f'{production}', end='')
            else:
                print(production + ' | ', end='')
        print()
    
def remove_empty_productions(grammar):
    print('')
    print('Removendo λ:')
    for nonterminal, productions in grammar.items():
        grammar[nonterminal] = [production for production in productions if production != 'λ']
    print_productions(grammar)

def lambda_location():
    print('Eliminação de produções vazias:')
    for nonterminal, productions in grammar.items():
        for production in productions:
            if production == 'λ':
                #print(nonterminal)
                eliminate_empty_productions(nonterminal)
    

def eliminate_empty_productions(nonterminalTarget):
    for nonterminal, productions in grammar.items():
        if nonterminal != nonterminalTarget:
            for production in productions:
                if nonterminalTarget in production:
                    temp_production = production.replace(nonterminalTarget, "")
                    if temp_production == '':
                        grammar[nonterminal].append('λ')
                    else:
                        grammar[nonterminal].append(temp_production)
                    
    print_productions(grammar)

        

def have_any_unitary_prod(grammar):
    print('')
    print('Removendo produções unitárias:')
    for non_terminal, productions in grammar.items():
        for production in productions:
            if len(production) == 1 and production[0] in grammar.keys():
                index = grammar[non_terminal].index(production)
                for key,value in grammar.items():
                    if grammar[non_terminal][index] == key:
                       productionsKey = grammar[key]
                       for production2 in productionsKey:
                           grammar[non_terminal].append(production2)
                del grammar[non_terminal][index]
    print_productions(grammar)



grammar = {
    'S': ['aAd', 'A'],
    'A': ['Bc', 'λ'],
    'B': ['Ac', 'a'],
}

lambda_location()
remove_empty_productions(grammar)
have_any_unitary_prod(grammar)

rename_nonterminals(grammar)
#print(encontrar_nao_terminais_lambda(grammar))
#print_productions(grammar)

