my_info = {"name": "Prabhnoor", "age": "21", "city": "San Jose"}

my_info["favorite color"] = "Blue"
my_info["city"] = "Los Angeles"

print("Keys: ", end="")
key_list = list(my_info.keys())
for i in range(len(key_list)):
    if i < len(key_list) - 1:
        print(key_list[i], end=", ")
    else:
        print(key_list[i])

print("Values: ", end="")
value_list = list(my_info.values())
for i in range(len(value_list)):
    if i < len(value_list) - 1:
        print(value_list[i], end=", ")
    else:
        print(value_list[i])