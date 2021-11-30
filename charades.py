import requests

print("Welcome to Charades!")
print("Directions:")
print("1. Choose a player to start.")
print("2. A word and animal will display and player has to act either of them out.")
print("3. The first person to guess the word or animal gets a point.")

temp = "1"
temp = input("4. Enter 1 to start: ")

while(temp != "0"):

  response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
  quoteResponse = requests.get("https://random-word-form.herokuapp.com/random/animal")

  print("The random word is:")
  print(response.text)

  print("Or act out this animal:")
  print(quoteResponse.text)
  
  temp = input("Enter 1 to start or 0 to exit: ")

