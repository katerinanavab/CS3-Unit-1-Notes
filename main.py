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


if __name__ == "__main__":
    main()
