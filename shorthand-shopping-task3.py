# Based on the clothing recommendation, suggest an accessory.
# For instance, if "sunglasses" were recommended, suggest "sunscreen" as an accessory.

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
clothing2 = "hat" if weather == "sunny" else "boots"
accessory = "sunscreen" if weather == "sunny" else "poncho" if weather == "rainy" else "chapstick" 
print(clothing, clothing2, accessory)