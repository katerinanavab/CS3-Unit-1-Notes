def main():
    print("hello world")

    # Declare variables
    age = 17
    teacher = "me"
    is_fave_class = True
    my_grade = 99.99

    # Check the type of a variable
    type_of_age = type(age)
    print(type_of_age)

    # String formatting with f-strings 
    # f"String literal {variable}"
    print(f"The type of the variable age is: {type_of_age}")
    print(f"My age divided by 10: {age/10}")

    # Initialize args for function
    ingredients_list = ["chocolate chips", "cinnamon", "flour", "sugar", "butter", "eggs"]
    snickerdoodle = "mix everything and put in oven. there ya go!"
    temp = 300

    # Call a function
    bake_cookie(ingredients_list, snickerdoodle, temp)

    # Call a function with an optional argument
    bake_cookie(ingredients_list, snickerdoodle, temp, cutter="star")

    # Reviewing optional keyword arguments
    print(calculate_numbers(2, 3)) # goes with default, "add"
    print(calculate_numbers(2,3,"subtract")) 
    print(calculate_numbers(2,3,operation="subtract")) # specify keyword

    # Demonstrate modifying values while iterating
    # Note that you can mix data types in the same list!!!!!!!
    numbers = [5, 5, 6, 5.5, 7, 42, 70, "hi"]
    list_iteration(numbers)

    # Test different container types
    list_demo()
    tuple_demo()
    set_demo()
    dict_demo()


def list_demo():
    print("***LIST DEMO***")
    my_list = ["h", "e", "l", "l", "o"]

    # Add an item to list
    my_list.append("!")
    print(my_list)

    # Get the number of items
    print(len(my_list))

    # Use index to access specific item 
    print(my_list[0])
    print(my_list[4:6]) # item at index 4 (inclusive) until 6 (excluded)
    print(my_list[4:]) # item at 4 until the end
    # NEGATIVE INDEX is located from the end, back 2 spots
    print(my_list[-2:]) # item at 4 until the end

    # Remove the first 'l'
    my_list.remove("l")
    # Insert an item at a index
    my_list.insert(1,"l")
    print(my_list)

    # Check if a certain value exists in a list
    # x in sequence - boolean expression
    print("!" in my_list)

    # Sort our list in reverse order
    # order meaning "alphabetical"
    my_list.sort(reverse=True)
    print(my_list)

def tuple_demo():
    print("***TUPLE DEMO***")
    # Tuples are IMMUTABLE
    person = ('Courtney', 17, 'Brooklyn, NY')
    name, age, hometown = person
    # created multiple variables in one line
    print(name)
    print(age)
    print(hometown)


def set_demo():
    print("***SET DEMO***")
    my_set = set()
    my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # SETS are MUTABLE 
    my_set.add(0) # will insert in ORDER!
    my_set.remove(4)
    print(my_set)
    # Sets can only contain UNIQUE values
    my_set.add(8)
    print(my_set)

    # Useful math operations between two sets
    other_set = {2, 4, 6, 8, 10}
    print(my_set.union(other_set))
    print(my_set.intersection(other_set))
    print(my_set.difference(other_set))


def dict_demo():
    print("***DICTIONARY DEMO***")



def bake_cookie(ingredients, instructions, temperature, cutter="circle"):

    # Print the list of ingredients
    for item in ingredients:
        print(item)
    # Print the oven temperature setting
    print(f"Set the oven to {temperature} degrees Kelvin.")
    print() # line break
    # Print the instructions 
    print(instructions, end="\n \n") # use optional keyword arg for line break
    # Tell them which cookie cutter to use
    print(f"Now use a {cutter} cookie cutter")

def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    # elif means ELSE IF
    elif operation == "subtract":
        return x - y 

# Different ways to modify values while iterating
def list_iteration(input_list):
    # 1. Create a new list as you loop
    new_list = []
    for item in input_list:
        new_list.append(item * 2)
    print(new_list)

    # 2. LIST COMPREHENSION
    input_list = [item * 2 for item in input_list]
    print(input_list)



if __name__ == "__main__":
    main()
