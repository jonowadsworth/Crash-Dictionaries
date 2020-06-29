# Nesting a dictionary within a list.
# Syntax seems to be:
#       dict
#       dict
#       dict
#list[dict1, dict2,dict3] etc

alien_0 = {'Colour': 'Green', 'Points': 10}
alien_1 = {'Colour': 'Yellow', 'Points': 5}
alien_2 = {'Colour': 'Red', 'Points': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

# More realistically, get the program to create the aliens for you
# first, make an empty LIST for storing the aliens:

aliens_list = []
# Now make 30 aliens using range()
for alien_number in range(30): #simple range call for 20 of whatever code comes now
    new_alien = {'Colour': 'Green', 'Points': 10} # create a dictionary and give it these characteristics
    aliens_list.append(new_alien) # update the blank aliens_list 30 times in this loop with the new dict
    # of the new alien we created above.

#show the first 5 aliens
for alien in aliens_list[:5]:
    print(alien)
print("...")

# to confirm number of created aliens, use LEN to get the length of a list as usual
print(f"The total number of aliens loose is: {len(aliens_list)}")
