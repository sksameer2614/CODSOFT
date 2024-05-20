import tkinter as tk
import random
import string

# Function to create the main window
def create_window():
    root = tk.Tk()
    root.title("Password Generator")
    root.configure(bg="#ADD8E6")  # Set light blue background color
    return root

# Function to validate mobile number length and change background color
def validate_mobile(entry):
    mobile_number = entry.get()
    if len(mobile_number) != 10:
        entry.config(bg="red")
        return False
    else:
        entry.config(bg="white")
        return True

# Function to validate username and change background color
def validate_username(entry):
    username = entry.get()
    if any(char.isdigit() for char in username):
        entry.config(bg="red")
        return False
    else:
        entry.config(bg="white")
        return True

# Function to validate password length and change background color
def validate_password_length(entry):
    length = entry.get()
    if not length.isdigit() or int(length) < 8 or int(length) > 16:
        entry.config(bg="red")
        return False
    else:
        entry.config(bg="white")
        return True

# Function to generate a random password
def generate_password(username, mobile_number, length):
    # Count the number of characters and digits in the username
    num_chars_username = sum(1 for char in username if char.isalpha())
    num_digits_username = sum(1 for char in username if char.isdigit())
    
    # Count the number of digits in the mobile number
    num_digits_mobile = sum(1 for char in mobile_number if char.isdigit())
    
    # Calculate the number of characters and digits to include in the password
    num_chars = min(num_chars_username, length // 2)
    num_digits = min(num_digits_mobile, length - num_chars)
    
    # Generate the password with characters from the username and digits from the mobile number
    characters = list(username) * num_chars + [char for char in mobile_number if char.isdigit()] * num_digits
    
    # Add additional characters from string.ascii_letters and string.digits
    characters += [char for char in string.ascii_letters + string.digits if char not in characters]
    
    # Shuffle the characters to make the password random
    random.shuffle(characters)
    
    # Return a password of specified length
    return ''.join(random.choices(characters, k=length))

# Function to handle button click event and generate password
def generate_password_click(username_entry, mobile_entry, password_length_entry, generated_password_entry):
    username = username_entry.get()
    mobile_number = mobile_entry.get()
    length = password_length_entry.get()

    # Validate username, mobile number, and password length
    is_valid_username = validate_username(username_entry)
    is_valid_mobile = validate_mobile(mobile_entry)
    is_valid_length = validate_password_length(password_length_entry)

    if is_valid_username and is_valid_mobile and is_valid_length:
        password = generate_password(username, mobile_number, int(length))
        generated_password_entry.delete(0, tk.END)  # Clear previous content
        generated_password_entry.insert(0, password)  # Insert generated password

# Function to reset all input fields
def reset_fields(username_entry, mobile_entry, password_length_entry, generated_password_entry):
    username_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)

    # Reset background colors to white
    username_entry.config(bg="white")
    mobile_entry.config(bg="white")
    password_length_entry.config(bg="white")
    generated_password_entry.config(bg="white")

# Function to change the color of the generated password field to green
def accept_password(generated_password_entry):
    generated_password_entry.config(bg="green")

# Function to create the title box
def create_title_box(window, width=650, height=55):  # Modified width and height
    title_frame = tk.Frame(window, bg="#FFB6C1", width=width, height=height, bd=1, relief=tk.SOLID)  # Light pink background with border
    title_frame.pack_propagate(False)  # Prevent frame from resizing to its contents
    title_frame.pack(pady=20)  # Increased gap between title box and green box

    title_label = tk.Label(title_frame, text="Password Generator", font=("Arial", 16, "bold"), bg="#FFB6C1")  # Light pink background with bold text
    title_label.pack(expand=True)

# Function to create the green box
def create_green_box(window, width=650, height=550):  # Same width and height as title box
    green_frame = tk.Frame(window, bg="#90EE90", width=width, height=height, bd=1, relief=tk.SOLID)  # Light green background with border
    green_frame.pack_propagate(False)  # Prevent frame from resizing to its contents
    green_frame.pack(pady=20)  # Increased gap between title box and green box

    # Add Username text and text field in the same line
    username_label = tk.Label(green_frame, text="Username:", font=("Arial", 20, "bold"), bg="#90EE90")  # Bold font
    username_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 10))  # Increased gap between label and entry

    username_entry = tk.Entry(green_frame, font=("Arial", 20), bd=1, relief=tk.SOLID)
    username_entry.grid(row=0, column=1, padx=(10, 20), pady=(20, 10))  # Increased gap between label and entry

    # Add Mobile Number text and text field in the same line
    mobile_label = tk.Label(green_frame, text="Mobile Number:", font=("Arial", 20, "bold"), bg="#90EE90")  # Bold font
    mobile_label.grid(row=1, column=0, padx=(20, 10), pady=(20, 10))  # Increased gap between label and entry

    mobile_entry = tk.Entry(green_frame, font=("Arial", 20), bd=1, relief=tk.SOLID)
    mobile_entry.grid(row=1, column=1, padx=(10, 20), pady=(20, 10))  # Increased gap between label and entry

    # Add Password Length text and text field in the same line
    password_length_label = tk.Label(green_frame, text="Password Length:", font=("Arial", 20, "bold"), bg="#90EE90")  # Bold font
    password_length_label.grid(row=2, column=0, padx=(20, 10), pady=(20, 10))  # Increased gap between label and entry

    password_length_entry = tk.Entry(green_frame, font=("Arial", 20), bd=1, relief=tk.SOLID)
    password_length_entry.grid(row=2, column=1, padx=(10, 20), pady=(20, 10))  # Increased gap between label and entry

    # Add Generated Password text and text field in the same line
    generated_password_label = tk.Label(green_frame, text="Generated Password:", font=("Arial", 20, "bold"), bg="#90EE90")  # Bold font
    generated_password_label.grid(row=3, column=0, padx=(20, 10), pady=(20, 10))  # Increased gap between label and entry

    generated_password_entry = tk.Entry(green_frame, font=("Arial", 20), bd=1, relief=tk.SOLID)
    generated_password_entry.grid(row=3, column=1, padx=(10, 20), pady=(20, 10))  # Increased gap between label and entry

    # Increased vertical gap below generated password field

    # Add Generate Password button
    generate_button = tk.Button(green_frame, text="Generate Password", font=("Arial", 16, "bold"), bg="blue", fg="white",
                                command=lambda: generate_password_click(username_entry, mobile_entry, password_length_entry, generated_password_entry))
    generate_button.grid(row=4, columnspan=2, pady=30)  # Increased gap below the button

    # Add Accept and Reset buttons
    accept_button = tk.Button(green_frame, text="Accept", font=("Arial", 16, "bold"), bg="green", fg="white",
                               command=lambda: accept_password(generated_password_entry))
    accept_button.grid(row=5, column=0, padx=(30, 10), pady=20)  # Increased horizontal and vertical gaps

    reset_button = tk.Button(green_frame, text="Reset", font=("Arial", 16, "bold"), bg="red", fg="white",
                             command=lambda: reset_fields(username_entry, mobile_entry, password_length_entry, generated_password_entry))
    reset_button.grid(row=5, column=1, padx=(10, 30), pady=20)  # Increased horizontal and vertical gaps

# Create the main window
root = create_window()

# Calculate the width for both the title and green boxes
box_width = 650

# Create the title box with custom width and height
create_title_box(root, width=box_width)

# Create the green box with the same width and height
create_green_box(root, width=box_width)

# Run the application
root.mainloop()
