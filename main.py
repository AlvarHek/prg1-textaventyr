# Här skriver du
import random
namn = input("vad ska spelarens namn vara? ")
print(f" {namn} ska till träningen men {namn} vet inte vart hen ska av. {namn} har tre alternativ: östra, centrala och hörnefors. Det tar 10 minuter att byta om när man är framme i hallen.")
print("östra stannar 7:40 och det tar 7 minuter att cykla från östra till hallen.")
print("centrala stannar 7:45 och det tar 6 minuter att cykla från centrala till hallen")
print("hörnefors är 30 km bort och den tar 2 timmar att cykla till hallen")
val1 = input(f"vars hoppar {namn} av? ").lower()
if val1 == "östra":
    print (f"{namn} är bytt om och redo för träningen")
    filler = input("")
elif val1 == "centrala":
    print (f"{namn} behövde skynda till hallen om blev lite sen. tränaren är arg men du kan träna ändå")
    filler = input("")
elif val1 == "hörnefors":
    print(f" {namn} kom aldrig fram till hallen och missade träningen. träneren är arg och du får inte spela match i helgen")
    exit()
else:
    print("jävla idiot det var inte en av alternativen")
    exit()
print(f"Efter träningen och skolan ska {namn} hem. {namn} kan välja mellan östra och centrala.{namn} slutar skolan 15:30 och tåget från östra går 15:40 och den från centrala går 15:45")
val2 = input(f"Vägen till centrala har mycket trafik och risken att bli överkörd är ganska hög. Vilken tåg ska {namn} ta? ").lower()
överkörd = random.randint(1, 7)
if val2== "centrala" and överkörd == 7:
    print(f"{namn} skulle till centrala men blev överkörd av en lastbil på vägen dit")
elif val2 == "centrala":
    print(f"{namn} cyklade till centrala och var i tid för tåget och han blev inte överkörd")
elif val2 == "östra":
    print(f"{namn} cyklade till östra och var i tid för tåget")
else:
    print("idiot det var inte en av alternativen")
