import requests

print("Welcome to Charades!")
print("Directions:")
print("1. Choose a player to start.")
print("2. Word will display and player has to act the word out.")
print("3. The first person to guess the word or phrase gets a point.")
print("4. Press 1 to start.")

temp = 1
temp = input("Enter 1 to start: ")

while(temp != 0):

  response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
  quoteResponse = requests.get("https://random-word-form.herokuapp.com/random/animal")

  print("The random word is:")
  print(response.text)

  print("Act out this animal:")
  print(quoteResponse)
  
  temp = input("Enter 1 to start or 0 to exit.: ")
