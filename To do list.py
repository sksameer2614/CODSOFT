import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)

def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        tasks.pop(index)
        update_listbox()

def complete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        task = tasks[index]
        tasks_completed.append(task)
        tasks.pop(index)
        update_listbox()

def on_entry_click(event):
    if entry_task.get() == "Add Your task":
        entry_task.delete(0, tk.END)
        entry_task.config(fg='black')

def on_entry_leave(event):
    if entry_task.get() == "":
        entry_task.insert(0, "Add Your task")
        entry_task.config(fg='grey')

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    listbox_tasks.insert(tk.END, "Tasks are:")
    for i, task in enumerate(tasks, start=1):
        listbox_tasks.insert(tk.END, f"{i}. {task}")
        listbox_tasks.itemconfig(tk.END, {'bg': 'violet'})
    for task in tasks_completed:
        listbox_tasks.insert(tk.END, task)
        listbox_tasks.itemconfig(tk.END, {'bg': 'lightgreen'})

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="lightblue")  # Set background color to light blue

# Create listbox
listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.configure(bg="violet")  # Set background color of listbox to violet
listbox_tasks.pack(pady=5)

# Create entry
entry_task = tk.Entry(root, width=60)
entry_task.insert(0, "Add Your task")
entry_task.configure(fg="grey")  # Set default text color to grey
entry_task.bind('<FocusIn>', on_entry_click)
entry_task.bind('<FocusOut>', on_entry_leave)
entry_task.pack(pady=5)

# Create buttons
frame_buttons = tk.Frame(root, bg="lightblue")
frame_buttons.pack(pady=5)

button_add = tk.Button(frame_buttons, text="Add Task", command=add_task, bg="blue", fg="white")  # Set background color to blue and text color to white
button_add.grid(row=0, column=0, padx=5)

button_remove = tk.Button(frame_buttons, text="Remove Task", command=remove_task, bg="red", fg="white")  # Set background color to red and text color to white
button_remove.grid(row=0, column=1, padx=5)

button_complete = tk.Button(frame_buttons, text="Complete Task", command=complete_task, bg="yellowgreen")  # Set background color to yellowgreen
button_complete.grid(row=0, column=2, padx=5)

# Initialize tasks list
tasks = []
tasks_completed = []

root.mainloop()
