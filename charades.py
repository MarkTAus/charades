import requests

print("Welcome to Charades!")
print("Directions:")
print("1. Choose a player to start.")
print("2. Word will display and player has to act the word out.")
print("3. The first person to guess the word or phrase gets a point.")

response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
quoteResponse = requests.get("https://yusufnb-quotes-v1.p.rapidapi.com/widget/~einstein.json")

print("The random word is:")
print(response.text)

print("Guess who said this quote!")
print(quoteResponse)
