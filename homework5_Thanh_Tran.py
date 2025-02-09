pokemon_list = ["Garchomp", "Rayquaza", "Palkia", "Pikachu", "Dialga", "Girantina"]

# Print all items
print("The items in the list are:", pokemon_list)

# Print the first two items
print(f"The first two items in the list are: {pokemon_list[0]}, {pokemon_list[1]}")

# Print the middle two items
print(f"The middle two items in the list are: {pokemon_list[2]}, {pokemon_list[3]}")

# Print the first and last items
print(f"The first and last items in the list are: {pokemon_list[0]}, {pokemon_list[-1]}")

# Tuple Exercise
menu = ("Ribeye", "Sirloin", "Flank", "T-bone", "New York Strip")

# Print each item using a loop
print("Original menu:")
for item in menu:
    print(item)

# Update the menu by creating a new tuple with two replacements
new_menu = ("Ribeye", "Sirloin", "Flank", "Skirt", "Filet Mignon")

# Print the revised menu
print("Revised menu:")
for item in new_menu:
    print(item)