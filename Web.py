import streamlit as st
import functions

Todos=functions.get_todos()

def add_todo():
    todo=st.session_state["New"]+"\n"
    Todos.append(todo)
    functions.write_todos(Todos)

#sequence matters
st.title("My To-Do App")
st.subheader("Hi! welcome")
st.write("This App will help you to make your schedule")

for index, todo in enumerate(Todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        Todos.pop(index)
        functions.write_todos(Todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label= "", placeholder ="Enter the new To-Do",
              key='New', on_change=add_todo)