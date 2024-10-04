#author__uy_thea
#date_October_3_2024
#section_bscpe2-2


value_list = [] #create a list for the all the values entered by the user
odd_list = [] #create a list that only contains odd integers from value_list

def get_the_value(): #create a function that will prompt the user to enter a value
    while True:
        try:
            value = int(input("Enter a value: "))
        except:
            print("Invalid")
        else:
            return value


def get_number_of_values(): #create a function that will ask the user how many values he/she wants
    while True:
        try:
            value = int(input("Enter the number of values: "))
        except:
            print("Invalid")
            continue
        else:
            return value

number_of_values = get_number_of_values()  #calling the function get_number_of_values


for value in range(number_of_values): #ask the user for the all the values they want
    value = get_the_value()
    value_list.append(value)


for value in value_list: #determine if the value is odd or even
    if value % 2 != 0:
        odd_list.append(value)
    else:
        pass


for square in odd_list: #calculate and print the square of all the odd integers
    print(f"The square of {square} is {square**2}")

#end of the program
