import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Calculator Application")
    root.geometry("300x300")
    root.configure(bg="#ADD8E6")  # Light blue background color

    # Create a frame for the top box
    frame1 = tk.Frame(root, bg="#FFA500", bd=5, relief="solid", borderwidth=1)  # Orange color, round border
    frame1.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.1, anchor="n")

    # Create a label with the text
    label_text = "Calculator Application"
    label = tk.Label(frame1, text=label_text, font=("Arial", 24, "bold"), bg="#FFA500", fg="black")  # Bold font, orange color, black foreground
    label.pack(expand=True)

    # Create a frame for the pink box
    frame2 = tk.Frame(root, bg="#FFC0CB", bd=5, relief="solid", borderwidth=1)  # Light pink color, round border
    frame2.place(relx=0.5, rely=0.18, relwidth=0.45, relheight=0.75, anchor="n")  # Adjusted rely parameter

    # Create a text field for input and output
    global text_input_output
    text_input_output = tk.Text(frame2, font=("Arial", 28), bg="white", fg="black")
    text_input_output.place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.1)

    # Create calculator buttons
    buttons_frame = tk.Frame(frame2, bg="#FFC0CB")
    buttons_frame.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.75)

    button_texts = [
        ("7", "Arial", 28), ("8", "Arial", 28), ("9", "Arial", 28), ("/", "Arial", 28),
        ("4", "Arial", 28), ("5", "Arial", 28), ("6", "Arial", 28), ("*", "Arial", 28),
        ("1", "Arial", 28), ("2", "Arial", 28), ("3", "Arial", 28), ("-", "Arial", 28),
        ("0", "Arial", 28), ("C", "Arial", 28), ("=", "Arial", 28), ("+", "Arial", 28)
    ]

    row = 0
    col = 0
    for text, font_name, font_size in button_texts:
        if text == "=":
            command = button_equal
        elif text == "C":
            command = button_clear
        else:
            command = lambda char=text: button_click(char)
        button = tk.Button(buttons_frame, text=text, font=(font_name, font_size, "bold"), padx=40, pady=8, command=command)
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()

def button_click(char):
    current_text = text_input_output.get("1.0", "end-1c")
    if current_text == "Error":
        text_input_output.delete("1.0", tk.END)
    text_input_output.insert(tk.END, char)

def button_clear():
    text_input_output.delete("1.0", tk.END)

def button_equal():
    try:
        expression = text_input_output.get("1.0", tk.END)
        result = eval(expression)
        text_input_output.delete("1.0", tk.END)
        text_input_output.insert(tk.END, str(result))
    except Exception as e:
        text_input_output.delete("1.0", tk.END)
        text_input_output.insert(tk.END, "Error")

if __name__ == "__main__":
    main()
