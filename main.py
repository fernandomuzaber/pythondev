# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


#Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
#
# greet_with("Fer", "Piriapolis")

#Keyword Argument

def greet_with(location , name):
    print(f"Hello  {name}, how are you all in {location}?")

greet_with( name="Fer", location="Piriapolis")