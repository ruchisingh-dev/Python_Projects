def madlib():
    name = input("Name: ")
    adj1 = input("Adjective: ")
    noun1 = input("Noun: ")
    verbPast = input("Verb (Past tense): ")
    adj2 = input("Adjective: ")
    noun2 = input("Noun: ")
    verb = input("Verb: ")
    adverb = input("Adverb: ")
    place = input("Place: ")
    adj3 = input("Adjective: ")


    madlib = f"One day, {name} found a {adj1} map hidden in their {noun1}. Excited, they {verbPast} to the {adj2} forest in search of the hidden {noun2}. As they {verb} deeper into the woods, they {adverb} discovered a {place}. It was filled with {adj3} treasures beyond their wildest dreams!"

    print(madlib)