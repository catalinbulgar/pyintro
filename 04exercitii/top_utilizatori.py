lista_filme = [
    {
        'nume': 'George',
        'filme': ['Shrek', 'Bond', 'Fight Club']
    },
    {
        'nume': 'Cristian',
        'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
    },
    {
        'nume': 'Stefan',
        'filme':   ['Fight Club', 'Slumdog Milionare']
    }
]
persoana = None
numar_filme = 0
for i in lista_filme:
    if numar_filme < len(i['filme']):
        numar_filme = len(i['filme'])
        persoana = i['nume']

print(f'{persoana}: {numar_filme}')
