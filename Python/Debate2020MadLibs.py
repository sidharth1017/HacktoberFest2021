adjectiveOne = input("Enter an adjective: ")
town = input("Enter the name of a town: ")
brand = input("Enter a snack food brand: ")
celebrity = input("Enter the name of a celebrity: ")
country = input("Enter a country: ")
noun = input("Enter a noun: ")
adjectiveTwo = input("Enter another adjective: ")
interjectionOne = input("Enter an interjection: ")
profession = input("Enter a profession: ")
insult = input("Enter an insulting name: ")
interjectionTwo = input("Enter another interjection: ")
place = input("Enter a place: ")
number = input("Enter a number: ")
cocktail = input("Enter the name of a cocktail: ")

if adjectiveOne.startswith('a') or adjectiveOne.startswith('e') or adjectiveOne.startswith('i') or adjectiveOne.startswith('o') or adjectiveOne.startswith('u'):
  print("It is an", adjectiveOne, "night in the town of", town+".")
else:
  print("It is a", adjectiveOne, "night in the town of", town+".")

print("Donald Trump and Joe Biden take the stage at the", brand, "Stadium.")
print("The moderator,", celebrity+", asks the first question:")
print('"Mr. Biden, what are your thoughts on our relationship with', country+'?"')
print('"Look, here is the', noun+'," Biden says, "We need to enter into', adjectiveTwo, 'talks with', country+'."')
print('Trump interjects, "'+ interjectionOne+'! I have the best foreign policy anyone has ever thought of. I am a great', profession+', possibly the best', profession, 'the world has ever seen."')

if insult.startswith('a') or insult.startswith('e') or insult.startswith('i') or insult.startswith('o') or insult.startswith('u'):
  print('Biden says, "You are an', insult+'."')
else:
  print('Biden says, "You are a', insult+'."')

print(celebrity, 'says, "'+ interjectionTwo+'! I am so sick of this. I am going to', place, 'and having', number, cocktail+'s so I can forget ever agreeing to this."')