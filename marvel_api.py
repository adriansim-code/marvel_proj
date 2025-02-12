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
        print("4. Exit HQ ")

        choice = input("\npick your choice: ")

        if choice == "4":
            print("Exiting...")
            break

        match choice:
            case "1":
                nameOfCharacter = input("\nEnter Characters full name: ")
                response = characters.all(limit = 100, nameStartsWith= nameOfCharacter)

                if not response["data"]["results"]:
                    print("No character with that name")
                    print("Try again")
                    continue
                else:
                    # Cycling through charcters 
                    heroList = response["data"]["results"]
                    for index, hero in enumerate(heroList):
                        print(f"\n {index +1 }. {hero['name']}")
                    
                    character = int(input("\nPick your character by number: "))-1

                    # Makes sure you picked a charcter from the list 
                    if character >= 0 < len(heroList):
                        selectedCharacter = heroList[character]
                        print("\n Great choice!")

                        # Grabs all infomation regarding charcters description and comics
                    moreInfo = input(f"\nWant to see more info about {selectedCharacter['name']}?: ").lower()
                    description = selectedCharacter["description"]
                    match moreInfo:
                        case 'yes':
                            print(f"\n{selectedCharacter['name']}")
                            if description:
                                print(f"Description: {description}")
                            else:
                                print(f"Description: No description available")
                            print("Charcater Info: ")
                            print(f"ID Number: {selectedCharacter['id']}")
                            print(f"Comic Available: {selectedCharacter['comics']['available']}")
                            print(f"Series Available: {selectedCharacter['series']['available']}")
                            print(f"Stories Available: {selectedCharacter['stories']['available']}")
                            print(f"Events Available: {selectedCharacter['events']['available']}")

                            # Shows first 100 comic's of character
                            comicAppearence = input(f"\nWant to see {selectedCharacter['name']} comic appearences? ").lower()
                            comics_response = marvel.characters.comics(selectedCharacter['id'], limit=100)
                            match comicAppearence:
                                case 'yes':
                                    print(f"\nHere are {selectedCharacter['name']}'s first 100 comic appearences: ")
                                    for index, book in enumerate(comics_response['data']['results'][:100], start=1):
                                        print(f"\n-{index}. {book['title']}")
                                    
                                    # Makes sure to exit or run program again
                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == "yes":
                                        continue
                                    else:
                                        break
                                case 'no':
                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == "yes":
                                        continue
                                    else:
                                        break

                        case 'no':
                            comicAppearence = input(F"\nWant to look for {selectedCharacter['name']}'s comic appearences? (yes/no): ").lower()
                            comics_response = marvel.characters.comics(selectedCharacter['id'], limit=100)
                            
                            # Prints character you choose without info or comic appearences
                            if comicAppearence == "no":
                                print(f"\nHere is your character: {selectedCharacter['name']}")
                                runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                if runAgain == 'yes':
                                    continue
                                else:
                                    break
                            # Asks for comic appearences if you didn't want to see info on character    
                            elif comicAppearence == "yes":
                                print(f"\nHere are {selectedCharacter['name']}'s first 100 comic appearences: ")
                                for index, book in enumerate(comics_response['data']['results'][:100], start=1):
                                    print(f"\n-{index}. {book['title']}")

                                # Asks to run program again or exit 
                                runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                if runAgain == 'yes':
                                    continue
                                elif runAgain == 'no':
                                    break
                                else:
                                    print("Invaild response")
                                    break   
                                
                            else:
                                print("Invaid response")
                                break        
                break
            case "2":
                
                nameStartingWith = input("\nEnter character name starting with: ")
                response = characters.all(limit = 100, nameStartsWith= nameStartingWith)

                
                if not response["data"]["results"]:
                    print("No match found")
                    continue
                else:
                    heroList = response["data"]["results"]
                    for index, hero in enumerate(heroList):
                        print(f"\n {index +1 }. {hero['name']}")
                    
                    character = int(input("\nPick your character by number: "))-1

                    if character >= 0 < len(heroList):
                        selectedCharacter = heroList[character]
                        print("\n Great choice!")
                        
                        comicChoice = input("\nWant to see their comic appearences? (yes/no): ").lower()
                        comics_response = marvel.characters.comics(selectedCharacter['id'], limit=100)

                        match comicChoice:
                            case 'yes':
                                print(f"\nHere are {selectedCharacter['name']}'s first 100 comic appearences: ")
                                for index, book in enumerate(comics_response['data']['results'][:100], start=1):
                                    print(f"\n-{index}. {book['title']}")
                                
                                characterInfo = input(f"\nWant more info on {selectedCharacter['name']}? (yes/no): ").lower()
                                description = selectedCharacter["description"]

                                match characterInfo:
                                    case 'yes':
                                        print(f"\n{selectedCharacter['name']}")
                                        if description: 
                                            print(f"Description: {description}")
                                        else:
                                            print(f"Description: No description available")
                                        print("Charcater Info: ")
                                        print(f"ID Number: {selectedCharacter['id']}")
                                        print(f"Comics Available: {selectedCharacter['comics']['available']}")
                                        print(f"Series Available: {selectedCharacter['series']['available']}")
                                        print(f"Stories Available: {selectedCharacter['stories']['available']}")
                                        print(f"Events Available: {selectedCharacter['events']['available']}")

                                        runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                        if runAgain == 'yes':
                                            continue
                                        elif runAgain == 'no':
                                            break
                                        else:
                                            print("Invaild response")
                                            break
                                    case 'no':
                                        runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                        if runAgain == 'yes':
                                            continue
                                        elif runAgain == 'no':
                                            break
                                        else:
                                            print("Invaild response")
                                            break
                                    case _:
                                        print("Invalid response")
                                        
                            case 'no':
                                characterInfo = input(f"\nWant more info on {selectedCharacter['name']}? (yes/no): ").lower()
                                description = selectedCharacter["description"]
                                if characterInfo == 'yes':
                                    print(f"\n{selectedCharacter['name']}")
                                    if description:
                                        print(f"Description: {description}")
                                    else:
                                        print(f"Descripton: No descrpition available")
                                    print("Charcater Info: ")
                                    print(f"ID Number: {selectedCharacter['id']}")
                                    print(f"Comics Available: {selectedCharacter['comics']['available']}")
                                    print(f"Series Available: {selectedCharacter['series']['available']}")
                                    print(f"Stories Available: {selectedCharacter['stories']['available']}")
                                    print(f"Events Available: {selectedCharacter['events']['available']}")

                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == 'yes':
                                        continue
                                    elif runAgain == 'no':
                                        break
                                    else:
                                        print("Invaild response")
                                        break
                                
                                elif characterInfo == 'no':
                                    print(f"\nYou picked {selectedCharacter['name']} ")
                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == 'yes':
                                        continue
                                    elif runAgain == 'no':
                                        break
                                    else:
                                        print("Invaild response")
                                        break
                                else:
                                    print("\nInvald response")    
                            case _:
                                print("bye")        
                    
                    else:
                        print("Invalid input ") 
                break
            case "3":
                characterId = input("\nEnter character's name: ")
                response = characters.all(limit = 100, nameStartsWith= characterId)

                if not response["data"]["results"]:
                    print("No match found")
                    continue
                else:
                    characterId = response["data"]["results"]
                    for index, character in enumerate(characterId, start=1):
                        print(f"\n-{index}. {character['name']} ID Number: {characterId[0]['id']}")
                        

                    choice = int(input("\nPick the character you are looking for by number: "))-1

                    if choice >= 0 < len(characterId):
                        selectedCharacter = characterId[choice]

                    comicAppearence = input("\nWant to see their comic appearences? (yes/no): ").lower()
                    comics_response = marvel.characters.comics(selectedCharacter['id'], limit=100)

                    match comicAppearence:
                        case 'yes':
                            print(f"\nHere are {selectedCharacter['name']}'s first 100 comic appearences: ")
                            for index, book in enumerate(comics_response['data']['results'][:100], start=1):
                                print(f"\n-{index}. {book['title']}")
                            
                            characterInfo = input(f"\nWant more info on {selectedCharacter['name']}? (yes/no): ").lower()
                            description = selectedCharacter["description"]

                            match characterInfo:
                                case 'yes':
                                    print(f"\n{selectedCharacter['name']}")
                                    if description:
                                        print(f"Description: {description}")
                                    else:
                                        print(f"Description: No description available")
                                    print("Charcater Info: ")
                                    print(f"ID Number: {selectedCharacter['id']}")
                                    print(f"Comics Available: {selectedCharacter['comics']['available']}")
                                    print(f"Series Available: {selectedCharacter['series']['available']}")
                                    print(f"Stories Available: {selectedCharacter['stories']['available']}")
                                    print(f"Events Available: {selectedCharacter['events']['available']}")

                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == 'yes':
                                        continue
                                    elif runAgain == 'no':
                                        break
                                    else:
                                        print("Invaild response")
                                        break
                                    

                                case 'no':
                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == 'yes':
                                        continue
                                    elif runAgain == 'no':
                                        break
                                    else:
                                        print("Invaild response")
                                        break
                        
                        
                        case 'no':
                            characterInfo = input(f"\nWant more info on {selectedCharacter['name']}? (yes/no): ").lower()
                            description = selectedCharacter["description"]
                            creator_names = set()
                            for comic in comics_response["data"]["results"]:
                                for creator in comic["creators"]["items"]:
                                    creator_names.add(creator["name"])

                            match characterInfo:
                                case 'yes':
                                    print(f"\n{selectedCharacter['name']}")
                                    if description:
                                        print(f"Description: {description}")
                                    else:
                                        print(f"Description: No description available")
                                    print("Charcater Info: ")
                                    print(f"ID Number: {selectedCharacter['id']}")
                                    print(f"Comics Available: {selectedCharacter['comics']['available']}")
                                    print(f"Series Available: {selectedCharacter['series']['available']}")
                                    print(f"Stories Available: {selectedCharacter['stories']['available']}")
                                    print(f"Events Available: {selectedCharacter['events']['available']}")
                                    
                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == 'yes':
                                        continue
                                    elif runAgain == 'no':
                                        break
                                    else:
                                        print("Invaild response")
                                        break
                                    break
                                case 'no':
                                    runAgain = input("\nWould you like to search for another character? (yes/no): ").lower()
                                    if runAgain == 'yes':
                                        continue
                                    elif runAgain == 'no':
                                        break
                                    else:
                                        print("Invaild response")
                                        break
                            
                break
            
else:
    print("\nGoodbye")    