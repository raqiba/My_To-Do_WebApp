FILEPATH='todos.txt'
def get_todos(filepath=FILEPATH):
    """this function will read the content
    present in the file in the parameter of filepath"""
    with open(filepath, 'r') as file:
        Todos_func = file.readlines()
        return Todos_func

def write_todos(todos_argument,filepath=FILEPATH):
    """this function going to add content in the respective file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_argument)
#this function is not returning anything as it is behaving as a procedure, if we return something it will be none


if __name__ == "__main__":
    print("Hello")
    print(get_todos())