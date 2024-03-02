# Based on the corrected code from Task 1, further enhance the program to
# recommend additional items like "hat" or "boots" based on the weather.

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater" #changed equal signs to equal comparison operators
clothing2 = "hat" if weather == "sunny" else "boots" #added second variable for additional recommendations
print(clothing, clothing2)