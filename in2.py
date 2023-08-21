def findname(name):

  phonebook = {"John Doe": "123-456-7890", "Jane Doe": "987-654-3210"}

  if name in phonebook:
    del phonebook[name]
    print(f"Deleted {name}'s phone number from the phonebook.")
  else:
    print(f"{name} is not in the phonebook.")

findname("John Doe")
