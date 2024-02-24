person1 = "Jimi Hendrix"
person2 = "Eric Clapton"

print(person1 + " and " + person2 + " are good guitarists!")
print("{} and {} are good guitarists!".format(person1, person2))
print(f"{person1} and {person2} are good guitarists!")

adj = input("Adjective: ")
verb = input("Verb: ")

sentence = f"Play a electric guitar is very {adj}. With music, we can {verb}!!!"

print(sentence)