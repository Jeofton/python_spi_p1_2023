senha = "ch1CoD01du"

senha = senha.lower()
valida = False

if len(senha) == 6:
    if not senha.isdigit() and not senha.isalpha():
        if "doi" not in senha and 'tinga' not in senha and 'ringa' not in senha:
            if not senha.startswith('t') and not senha.endswith('f'):
                valida = True

if(valida):
    print('Você ´eum héroi')
else:
    print('Perdeu pleiboi!')
