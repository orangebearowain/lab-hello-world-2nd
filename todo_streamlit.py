import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def add_task(task):
    if task:
        st.session_state.tasks.append({'task': task, 'done': False})

def delete_task(task_index):
    del st.session_state.tasks[task_index]

def toggle_done(task_index):
    st.session_state.tasks[task_index]['done'] = not st.session_state.tasks[task_index]['done']

new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    add_task(new_task)

st.write("Tasks:")

for i, task in enumerate(st.session_state.tasks):
    if st.checkbox(task['task'], value=task['done'], key=f"task_{i}"):
        toggle_done(i)

    if st.button(f"Delete task {i+1}", key=f"delete_{i}"):
        delete_task(i)