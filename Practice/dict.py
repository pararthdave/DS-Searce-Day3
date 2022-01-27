#hashtable can be implemented using dictionaries in python, it has a key and a value pair functionality
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)
print("Brand: ",dict['brand']) #on calling key value is returned, get function can also be used to perform this task

family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(family['child1'])  #nested dictionary printing    
print("Clearing Dictonary:",family.clear())
print(family)