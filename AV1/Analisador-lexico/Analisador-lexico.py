def is_special(character):

    # Define os Caracteres Especiais Válidos
    special = "!@#$%^&*()_+-=[]{};':\"\\|,.<>/?~` "

    if character in special:
        return True
    else:
        return False

def is_math_operator(character):

    # Define os Operadores Matemáticos Válidos
    mathOperators = "+-*\/"

    if character in mathOperators:
        return True
    else:
        return False

def is_math_symbols(character):

    # Define os caracteres especiais válidos
    mathSymbols = "()[]{}@#!="

    if character in mathSymbols:
        return True
    else:
        return False

def is_math_character(character):

    # Define as letras que compõem operações matemáticas
    math_letters = "xXyYzZtTwW"

    if character in math_letters:
        return True
    else:
        return False

def is_any_letter(character):

    # Define o alfabeto de letras 
    any_letter = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZàÀâÂÅãÃüäöÄăĂƁɃĈƇČÇƊÐéÉêÊẼƑƒǦƓĜḦɦĤĦİŦƗĴƘǨŁN̈ÑŊƝÖØƟƤⱤŜŠŞȘŢƬȚƮŬÜŲɄⱲƳỸŶȲŽȤⱯȜƄĸⱩℲǶƼЧɊƢƦſƧǷƜⱾⱿƵⱭÆɅÐƐƏƎƔɪƖƷƆŒßƩÞþȢƱωƲɁɓƀĉƈčçɗðêêẽƒƒǧɠĝḧɦĥħi̇ŧɨĵƙǩłn̈ñŋɲöøɵƥɽŝšşșţƭțʈŭüųʉⱳƴỹŷȳžȥɐȝƅĸⱪⅎƕƽчɋƣʀſƨƿɯȿɀƶɑæʌðɛəǝɣɪɩʒɔœßʃþþȣʊωʋɂ"

    if character in any_letter:
        return True
    else:
        return False


entryData= input('Insira a Cadeia:')
#中文
passed = True
mathExpression = False

for i in range(10):
    if(entryData == ''):
        break
    
    if entryData[0].isdigit():
        print('Começou com um número, é reservado pelo sistema.')
        passed = False
        break

    lenght = len(entryData)
    if(is_math_operator(entryData[lenght-1])) :
            print('Nao Aceita Cadeias Que Terminem Com Operadores Matematicos Ou Caracteres Especiais.')
            passed = False
            break

    if(i >= len(entryData)):
        break
    
    print(entryData[i])

    if(not is_math_operator(entryData[i]) and not is_any_letter(entryData[i]) and not is_math_symbols(entryData[i]) and not is_special(entryData[i]) and not entryData[i].isdigit()):
        print('Cadeia Contém Caracter Não Latino.')
        passed = False
        break

    if(is_math_character(entryData[i])):
        mathExpression = True

        #Não aceita cadeias que contenham um único digito que seja x, y, z, t ou w.
        if(len(entryData) == 1):
            print('Cadeia Não Aceita')
            passed = False
            break

        if(i > 0 and i < len(entryData) and i < 9):
            if(not is_math_operator(entryData[i-1]) and not is_math_symbols(entryData[i-1]) and not entryData[i-1].isdigit()):
                is_math_character(entryData[i-1])
                print('Cadeia Não É Uma Expressão Matemática, Porém Possui Números, Operadores Matemáticos ou Palavras Reservadas.')
                passed = False
                break
        if(i+1 != len(entryData)):
            if(not is_math_operator(entryData[i+1]) and not is_math_symbols(entryData[i+1]) and not entryData[i+1].isdigit()):
                print(entryData[i+1])
                print('Cadeia Não É Uma Expressão Matemática, Porém Possui Números, Operadores Matemáticos ou Palavras Reservadas.')
                passed = False
                break
        
if(passed):
    print('Cadeia Aceita.')
    if mathExpression == True:
        print('Expressão matemática.')