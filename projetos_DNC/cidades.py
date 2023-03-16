cidades = [
    ("São Paulo", 12325232),
    ("Rio de Janeiro", 6747815),
    ("Brasília", 3055149),
    ("Salvador", 2849337),
    ("Fortaleza", 2669342),
    ("Belo Horizonte", 2523794),
    ("Manaus", 2199391),
    ("Curitiba", 1948626),
    ("Recife", 1645727),
    ("Porto Alegre", 1488252)
]

# Imprime as cidades em ordem decrescente de população
for cidade, populacao in sorted(cidades, key=lambda x: x[1], reverse=True):
    print(f"{cidade} - {populacao}")
