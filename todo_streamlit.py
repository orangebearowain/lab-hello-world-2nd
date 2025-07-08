import streamlit as st

# Initialize task list in session state if not already present
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add task
def add_task(task):
    if task:
        st.session_state.tasks.append({'task': task, 'done': False})

# Function to delete task
def delete_task(task_index):
    del st.session_state.tasks[task_index]

# Function to mark task as done
def toggle_done(task_index):
    st.session_state.tasks[task_index]['done'] = not st.session_state.tasks[task_index]['done']

# Input to add new task
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    add_task(new_task)

# Display tasks
st.write("Tasks:")

for i, task in enumerate(st.session_state.tasks):
    # Checkbox for each task to toggle done/undone status
    if st.checkbox(task['task'], value=task['done'], key=f"task_{i}"):
        toggle_done(i)

    # Button to delete task
    if st.button(f"Delete task {i+1}", key=f"delete_{i}"):
        delete_task(i)

