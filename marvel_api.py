from marvel import Marvel
from keys import pub, priv

marvel = Marvel(PUBLIC_KEY=pub, PRIVATE_KEY=priv)

characters = marvel.characters
comics = marvel.comics

start = input("\nWould you like to start? (yes/no): ")

if start.lower() == "yes":

    runAgain = True
    
    print("\nWelcome to Marvel HQ")

    while runAgain:
        print("\nWhat would you like to search for? ")
        print("\n1. Search character by Specific Name ")
        print("2. Search character by Name Starting With... ")
        print("3. Search for character's ID Number? ")
        print("4. Search Comic Book by Name ")
        print("5. Search Comic Book by Year ")
        print("6. Exit HQ ")

        choice = input("\npick your choice: ")

        if choice == "6":
            print("Exiting...")
            break

        match choice:
            case "1":
                nameOfCharacter = input("\nEnter Characters full name: ")
                response = characters.all(name= nameOfCharacter)

                if not response["data"]["results"]:
                    print("No character with that name")
                else:
                    character = response["data"]["results"]
                    moreInfo = input(f"\nWant to see more info about {character[0]['name']}?: ")
                    match moreInfo:
                        case 'yes'| 'Yes':
                            print(f"\n{character[0]['name']}")
                            print("Info: ")
                            print(f"Character ID Number: {character[0]['id']}")
                            print(f"Comic Available: {character[0]['comics']['available']}")

                            comicAppearence = input(f"\nWant to see {character[0]['name']} comic appearences? ")
                            match comicAppearence:
                                case 'yes' | 'Yes':
                                    print(f"\nHere are {character[0]['name']} comic appearences: ")
                                    for comic in character[0]['comics']['items']:
                                        print(f"\n-{comic['name']}")
                                        print("")
                                    runAgain = input("\nWant to exit Marvel HQ? (yes/no): ")
                                    if runAgain == "yes":
                                        continue
                                    else:
                                        break
                        case 'no'|'No':
                            comicAppearence = input(F"\nWant to look for {character[0]['name']}'s comic appearences? (yes/no): ")
                            if comicAppearence == "no":
                                print(f"\nHere is your character: {character[0]['name']}")
                                runAgain = input("Want to search for another character? (yes/no): ")
                                if runAgain == 'yes':
                                    continue
                                else:
                                    break
                            elif comicAppearence == "yes":
                                print(f"\nHere are {character[0]['name']}'s comic appearences: ")
                                for comic in character[0]['comics']['items']:
                                    print(f"\n-{comic['name']}")
                                    print("")
                                break
                            else:
                                break        
                break
            case "2":
                
                nameStartingWith = input("\nEnter character name starting with: ")
                response = characters.all(nameStartsWith= nameStartingWith)
                
                if not response["data"]["results"]:
                    print("No match found")
                else:
                    heroList = response["data"]["results"]
                    for index, hero in enumerate(heroList):
                        print(f"\n {index +1 }. {hero['name']}")
                    
                    character = int(input("\nPick your character by number: "))-1

                    if character >= 0 < len(heroList):
                        selectedCharacter = heroList[character]
                        print("\n Great choice!")
                        print(f"You picked {selectedCharacter['name']}")
                        
                        comicChoice = input("\nWant to see their comic apperences? (yes/no): ")
                        
                        match comicChoice:
                            case 'yes':
                                print(f"\nHere are {selectedCharacter['name']}'s comic appearences: ")
                                for book in selectedCharacter['comics']['items']:
                                    print(f"\n-{book['name']}")
                                characterInfo = input(f"\nWant more info on {selectedCharacter['name']}? (yes/no): ")
                                match characterInfo:
                                    case 'yes':
                                        print(f"\n{selectedCharacter['name']}")
                                        print("Info: ")
                                        print(f"Charcater ID: {selectedCharacter['id']}")
                                        print(f"Comics Available: {selectedCharacter['comics']['available']}")
                                        break
                                    case 'no':
                                        break
                                    case _:
                                        print("Invalid response")
                            case 'no':
                                characterInfo = input(f"\nWant more info on {selectedCharacter['name']}? (yes/no): ")
                                if characterInfo == 'yes':
                                    print(f"\n{selectedCharacter['name']}")
                                    print("Info: ")
                                    print(f"Character ID: {selectedCharacter['id']}")
                                    print(f"Comics Available: {selectedCharacter['comics']['available']}")
                                elif characterInfo == 'no':
                                    print(f"\nYou picked {selectedCharacter['name']} ")
                                else:
                                    print("\nInvald response")    
                            case _:
                                print("bye")        
                    else:
                        print("Wrong") 
                break
            case "3":
                break
            case "4":
                break
            case "5":
                break
else:
    print("\nGoodbye") 