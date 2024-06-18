def madlib():
    adj1 = input("Adjective: ")
    noun1 = input("Noun: ")
    pluralNoun1 = input("Plural Noun: ")
    adj2 = input("Adjective: ")
    place = input("Place: ")
    verbPast = input("Verb (past tense): ")
    adverb = input("Adverb: ")
    noun2 = input("Noun: ")

    madlib = (
        f"Once upon a time in a {adj1} forest, there was a magical {noun1} that could talk to {pluralNoun1}.One day, a {adj2} traveler came from {place}. The traveler {verbPast} with the magical {noun1} and learned the secrets of the forest.They lived {adverb} ever after with their new {noun2} friend."
    )

    print(madlib)


