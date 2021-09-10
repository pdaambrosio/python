is_vertebrate = input()
classification = input()
food_chain = input()

vertebrate = {'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'}, 'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}}}
invertebrate = {'invertebrado': {'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'}, 'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}}

if is_vertebrate in vertebrate:
    for key, value in vertebrate.items():
        if classification in value:
            for chain, animal in value.get(classification).items():
                if food_chain == chain:
                    print(animal)
elif is_vertebrate in invertebrate:
    for key, value in invertebrate.items():
        if classification in value:
            for chain, animal in value.get(classification).items():
                if food_chain == chain:
                    print(animal)
