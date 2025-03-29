import matplotlib.pyplot as plt
from matplotlib_venn import venn3

estados = {
    "São Paulo": ["Automobilística", "Têxtil", "Petroquímica"],
    "Minas Gerais": ["Automobilística", "Têxtil"],
    "Rio de Janeiro": ["Têxtil", "Petroquímica"],
    "Rio Grande do Sul": ["Automobilística", "Têxtil", "Petroquímica"],
    "Paraná": ["Automobilística", "Têxtil"],
    "Santa Catarina": ["Têxtil"],
    "Bahia": ["Automobilística", "Têxtil", "Petroquímica"],
    "Pernambuco": ["Automobilística", "Têxtil"],
    "Ceará": ["Têxtil"],
    "Amazonas": ["Petroquímica"]
}

conjunto_automobilistica = set()
conjunto_textil = set()
conjunto_petroquimica = set()

for estado, industrias in estados.items():
    if "Automobilística" in industrias:
        conjunto_automobilistica.add(estado)
    if "Têxtil" in industrias:
        conjunto_textil.add(estado)
    if "Petroquímica" in industrias:
        conjunto_petroquimica.add(estado)

# Pergunta 3.1: Quais estados têm Automobilística ou Têxtil?
estados_automobilistica_ou_textil = conjunto_automobilistica | conjunto_textil
print("Estados com Automobilística ou Têxtil:", estados_automobilistica_ou_textil)

# Pergunta 3.2: Quais estados têm Automobilística e Petroquímica?
estados_automobilistica_e_petroquimica = conjunto_automobilistica & conjunto_petroquimica
print("Estados com Automobilística e Petroquímica:", estados_automobilistica_e_petroquimica)

# Pergunta 3.3: Quais estados têm Automobilística mas não têm Petroquímica?
estados_automobilistica_sem_petroquimica = conjunto_automobilistica - conjunto_petroquimica
print("Estados com Automobilística, mas sem Petroquímica:", estados_automobilistica_sem_petroquimica)

# Pergunta 4.1: Quais estados não possuem a indústria Petroquímica?
estados_sem_petroquimica = set(estados.keys()) - conjunto_petroquimica
print("Estados sem a indústria Petroquímica:", estados_sem_petroquimica)

# Pergunta 4.2: Quais estados possuem somente a indústria Têxtil?
estados_so_textil = {estado for estado, industrias in estados.items() if industrias == ["Têxtil"]}
print("Estados com somente a indústria Têxtil:", estados_so_textil)

# Pergunta 4.3: O estado Paraná pertence ao conjunto de estados com Automobilística?
pertinencia_parana = "Paraná" in conjunto_automobilistica
print("O estado Paraná pertence ao conjunto de estados com Automobilística:", pertinencia_parana)

venn_labels = {
    '100': conjunto_automobilistica - conjunto_textil - conjunto_petroquimica,  # Apenas Automobilística
    '010': conjunto_textil - conjunto_automobilistica - conjunto_petroquimica,  # Apenas Têxtil
    '001': conjunto_petroquimica - conjunto_automobilistica - conjunto_textil,  # Apenas Petroquímica
    '110': conjunto_automobilistica & conjunto_textil - conjunto_petroquimica,  # Automobilística e Têxtil, sem Petroquímica
    '101': conjunto_automobilistica & conjunto_petroquimica - conjunto_textil,  # Automobilística e Petroquímica, sem Têxtil
    '011': conjunto_textil & conjunto_petroquimica - conjunto_automobilistica,  # Têxtil e Petroquímica, sem Automobilística
    '111': conjunto_automobilistica & conjunto_textil & conjunto_petroquimica,  # Todos
}

venn = venn3(subsets=(len(venn_labels['100']), 
                      len(venn_labels['010']), 
                      len(venn_labels['110']),
                      len(venn_labels['001']),
                      len(venn_labels['101']),
                      len(venn_labels['011']),
                      len(venn_labels['111'])),
             set_labels=('Autombilística', 'Têxtil', 'Petroquímica'))

for key, estados_na_regiao in venn_labels.items():
    if estados_na_regiao:
        venn.get_label_by_id(key).set_text("\n".join(sorted(estados_na_regiao)))
        
plt.title("Diagrama de Venn - Indústrias por Estado")
plt.show()
