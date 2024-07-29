import random

def main():
    instructions()

def instructions():
    print("Word Riddler is a word guessing game similar to Wheel of Fortune and Wordle combined.")
    ask = askAgain()
    if (ask in ["YES", "Y"]):
        
    
def askAgain():
    request = input("Would you like to play Word Riddler? Yes/No: ").upper()
    while request not in ["YES", "Y", "NO", "N"]:
        request = input("I'm sorry, but I don't understand. Enter yes to play and no to cancel: ")
    return request

def generateRandom():
    categories = [
        ["Books"]
        ["Movies"]
        ["U.S. States"]
    ]
    words = [
        ["A Court of Thorns and Roses", "Harry Potter", "Divergent", "Fourth Wing", "The Keeper of Stars"],
        ["Casablanca", "Deadpool", "Fall Guy", "Twister", "Wonka"],
        ["Oregon", "New Jersey", "Utah", "New Mexico", "Florida"]
    ]
    
    catnums = {}
    for i, category in enumerate(categories):
        catnums[category[0]] = i + 1
    
    num = random.randint(1, 4)
    

if __name__ == "__main__":
    main()
