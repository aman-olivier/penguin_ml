import streamlit as st 
st.title("My to-Do list Creator")
if "my_todo_list" not in st.session_state:
    st.session_state.my_todo_list = ["buy groceries","learn Streamlit", "Learn python"]
new_todo = st.text_input("what do you need to do?")
if st.button("Add the new to-do item"):
    st.write("Adding a new item to the list")
    st.session_state.my_todo_list.append(new_todo)
st.write("my new to-do list is ", st.session_state.my_todo_list)