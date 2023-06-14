def rename_nonterminals(grammar):
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

def print_productions(grammar):
    print('')
    for nonterminal, productions in grammar.items():
        print(f"{nonterminal} -> ", end='')
        for i, production in enumerate(productions):
            if i == len(productions) - 1:
                print(f'{production}', end='')  # Último elemento, imprime sem espaço
            else:
                print(production + ' | ', end='')  # Não é o último elemento, imprime com vírgula
        print()
    

def remove_empty_productions(grammar):
    for nonterminal, productions in grammar.items():
        grammar[nonterminal] = [production for production in productions if production != 'λ']

grammar = {
    'S': ['aAd', 'A'],
    'A': ['Bc', 'λ'],
    'B': ['Ac', 'a'],
}

remove_empty_productions(grammar)
#rename_nonterminals(grammar)
print_productions(grammar)


