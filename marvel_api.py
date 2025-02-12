from marvel import Marvel
from keys import pub, priv

marvel = Marvel(PUBLIC_KEY=pub, PRIVATE_KEY=priv)

characters = marvel.characters
comics = marvel.comics
creators = marvel.creators

start = input("\nWould you like to start? (yes/no): ").lower()

if start.lower() == "yes":

    runAgain = True
    
    print("\nWelcome to Marvel HQ")