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
        if index < len(tasks):
            tasks.pop(index-1)
            update_listbox()

def complete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        if index < len(tasks):
            task = tasks.pop(index-1)
            tasks_completed.append(task)
            update_listbox()

def on_task_select(event):
    # Clear previous selection highlight (if any)
    listbox_tasks.selection_clear(0, tk.END)

    selected_task = listbox_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        # Highlight only the selected active task (blue)
        if index < len(tasks):
            listbox_tasks.itemconfig(index, {'bg': 'blue'})

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    listbox_tasks.insert(tk.END, "Tasks are:")
    for i, task in enumerate(tasks, start=1):
        listbox_tasks.insert(tk.END, f"{i}. {task}")
    if tasks_completed:
        # Insert an empty line to create a gap
        listbox_tasks.insert(tk.END, "")
        listbox_tasks.insert(tk.END, "Completed Tasks:")
        for task in tasks_completed:
            listbox_tasks.insert(tk.END, task)
            listbox_tasks.itemconfig(tk.END, {'bg': 'lightgreen'})

    # Highlight selected task again if any
    on_task_select(None)

def on_entry_click(event):
    if entry_task.get() == "Add Your Tasks...":
        entry_task.delete(0, tk.END)
        entry_task.config(fg='black')  # Change text color to black when clicked

def on_entry_leave(event):
    if entry_task.get() == "":
        entry_task.insert(0, "Add Your Tasks...")
        entry_task.config(fg='black')  # Change text color to grey when left empty

root = tk.Tk()
root.title("To-Do List Application")

# Set background color to light sky blue
root.configure(bg="lightblue")

# Create a frame for the title
title_frame = tk.Frame(root, bg="lightpink", bd=1, relief="solid")  # Reduced border density
title_frame.pack(pady=(50, 10), padx=400, fill="x")  # Reduced padding on both sides

# Create a label for the title
title_label = tk.Label(title_frame, text="To Do List Application", font=("Helvetica", 24, "bold"), fg="black", bg="lightpink")
title_label.pack(pady=10)

# Create a frame for the yellow box
yellow_frame = tk.Frame(root, bg="yellow", bd=1, relief="solid")  # Yellow color
yellow_frame.pack(pady=(10, 50), padx=400, fill="both", expand=True)

# Create entry for adding tasks
entry_task_frame = tk.Frame(yellow_frame, bg="yellow", bd=0)  # Set border density to 0
entry_task_frame.pack(pady=(20, 5), padx=20, fill="x")  # Adjusted padding

entry_task = tk.Entry(entry_task_frame, width=40, font=("Helvetica", 14), fg='black', bg="orange")  # Black color for text
entry_task.insert(0, "Add Your Tasks...")
entry_task.bind('<FocusIn>', on_entry_click)
entry_task.bind('<FocusOut>', on_entry_leave)
entry_task.pack(pady=10, padx=10)

# Create a frame for the violet box
violet_frame = tk.Frame(yellow_frame, bg="yellow", bd=0)  # Set border density to 0
violet_frame.pack(pady=5, padx=20)  # Adjusted padding

# Create a listbox for the tasks list
listbox_tasks = tk.Listbox(violet_frame, width=60, height=13, font=("Helvetica", 14), selectmode=tk.SINGLE, bg="violet",
                           selectbackground="violet", selectforeground="black", activestyle="none", exportselection=False)  # Updated properties
listbox_tasks.pack(pady=10, padx=10)

# Bind select event to listbox using a dedicated function for clarity
listbox_tasks.bind('<Button-1>', on_task_select)

# Create a frame for the buttons
button_frame = tk.Frame(yellow_frame, bg="yellow", bd=0)  # Set border density to 0
button_frame.pack(pady=(10, 20))  # Adjusted padding

# Create buttons
button_add = tk.Button(button_frame, text="Add Task", font=("Helvetica", 12), bg="orange", fg="black", width=12, height=1, command=add_task)
button_add.pack(side=tk.LEFT, padx=10)

button_remove = tk.Button(button_frame, text="Remove Task", font=("Helvetica", 12), bg="red", fg="black", width=12, height=1, command=remove_task)
button_remove.pack(side=tk.LEFT, padx=10)

button_complete = tk.Button(button_frame, text="Complete Task", font=("Helvetica", 12), bg="green", fg="black", width=14, height=1, command=complete_task)
button_complete.pack(side=tk.LEFT, padx=10)

# Initialize tasks list
tasks = []
tasks_completed = []

root.mainloop()
