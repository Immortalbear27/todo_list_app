# Initialise the list of To-do tasks
todos = []

# Obtain the user's inputs and add them to the list
# Displays the list of options in list format
while True:
    user_text = input("Enter a todo: ")
    if user_text != 'exit':
        todos.append(user_text)
    if user_text == "exit":
        print(todos)
        break