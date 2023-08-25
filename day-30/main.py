# try:
#     file = open("ahmed.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("ahmed.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise KeyError("Wrong key mate")


height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3m!")
bmi = weight / height ** 2
