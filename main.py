# Initialisation of required variables:
todos = []
user_text = ""
todo = ""

# Fetch the user's input, and perform the corresponding task:
# add - Let's the user add one or multiple tasks to their to-do list
# show - The user's to-do list will be printed
# exit - The program terminates
while True:
    user_text = input("Type add, show or exit to access the relevant areas: ")
    user_text = user_text.strip().capitalize()
    
    if user_text == 'Add':
        while todo != 'Done':
            todo = input("Enter a task: ")
            if todo == 'Done':
                todo = ""
                break
            todos.append(todo.capitalize())
    elif user_text == 'Show':
        for item in todos:
            print(item)
    elif user_text == 'Exit':
        break
    else:
        print('That command is not acceptable')
        
print('It was fun working with you. Goodbye for now!')