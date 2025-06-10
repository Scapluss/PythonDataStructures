favorite_things = ("KGF", "Gangster Touch", "Of Mice and Men")
print("Favorite things: ", favorite_things)
try:
    favorite_things[0] = "Pushpa"
except TypeError:
    print("Oops! Tuples cannot be changed.")
print("Length of tuple: ", len(favorite_things))