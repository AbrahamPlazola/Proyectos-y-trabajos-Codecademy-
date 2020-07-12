from script import sparse_search

data_one = ["Arthur", "", "", "", "", "", "Elise", "", "", "", "Gary", "", "Mimi", "", "", "", "Zachary"]
search_one = "Zachary"
print("Calling sparse_search.....")
ret = sparse_search(data_one, search_one)
print("Return Value: " + str(ret))

data_two = ["1", "", "", "2", "", "", "3", "", "5", "", "", "", "9", "12"]
search_two = "2"
print("\n\nCalling sparse_search.....")
ret = sparse_search(data_two, search_two)
print("Return Value: " + str(ret))
