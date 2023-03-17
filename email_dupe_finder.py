import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def find_duplicate_emails(email_list):
    # Create a dictionary to store each email and the number of times it appears
    email_dict = {}
    # Regular expression pattern to match email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Search for email addresses in each line of the email list
    for line in email_list:
        emails = re.findall(pattern, line)
        # If one or more emails are found, add them to the dictionary and increment the count
        for email in emails:
            if email in email_dict:
                email_dict[email] += 1
            else:
                email_dict[email] = 1
    # Create a list of duplicates
    duplicates = [email for email, count in email_dict.items() if count > 1]
    # Sort the list of duplicates
    duplicates.sort()
    # Return the list of duplicates
    return duplicates


def open_file():
    # Clear the textbox
    textbox.delete('1.0', tk.END)
    # Open the file dialog
    file_path = filedialog.askopenfilename()
    if file_path:
        # Open the selected file
        with open(file_path, 'r') as file:
            # Read the file and split it into lines
            email_list = file.read().splitlines()
            # Find the duplicates
            duplicates = find_duplicate_emails(email_list)
            # Get the number of duplicates
            num_duplicates = len(duplicates)
            # Insert the number of duplicates into the textbox
            textbox.insert(tk.END, f'Number of duplicates: {num_duplicates}\n\n')
            # Insert the duplicates into the textbox
            for email in duplicates:
                textbox.insert(tk.END, email + '\n')
                
def copy_to_clipboard():
    # Get the text from the textbox
    text = textbox.get('1.0', tk.END)
    # Copy the text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo('Copy to Clipboard', 'All text has been copied to the system clipboard.')
    

# Create the GUI window
root = tk.Tk()
root.title('Duplicate Email Checker')
root.geometry('800x600')

# Set the font
font_style = ('Courier', 12)

# Create the instruction label
instruction_label = tk.Label(root, text='Click the "Open File" button to choose a file to check for duplicate emails.', font=font_style, bg='black', fg='#00ff00')
instruction_label.pack(pady=10)

# Create the open file button
open_file_button = tk.Button(root, text='Open File', command=open_file, font=font_style, bg='black', fg='blue')
open_file_button.pack()

# Create the textbox
textbox = tk.Text(root, font=font_style, bg='black', fg='#00ff00')
textbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the copy to clipboard button
copy_button = tk.Button(root, text='Copy All', command=copy_to_clipboard, font=font_style, bg='black', fg='blue')
copy_button.pack(pady=10)

# Run the GUI
root.mainloop()
