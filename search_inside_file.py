import subprocess
import tkinter as tk

import pyperclip as pyperclip


def search_files():
    search_path = path_entry.get()
    file_type = file_type_entry.get() if file_type_entry.get() != "" else "*"
    search_term = search_term_entry.get()

    # Replace placeholders with user inputs
    powershell_script = f'foreach ($file in Get-ChildItem -Path "{search_path}" -Filter "*.{file_type}" -Recurse | Select-String -Pattern "{search_term}" | Select-Object -Unique Path) {{ $file.Path }}'

    # Run PowerShell script
    process = subprocess.Popen(['powershell.exe', '-Command', powershell_script], stdout=subprocess.PIPE)
    result = process.communicate()[0].decode('utf-8')
    pyperclip.copy(result)
    # Update result label
    result_label.config(text=result)

# Create the main window
window = tk.Tk()
window.title("File Search")

# Create the input fields
path_label = tk.Label(window, text="Folder Path:")
path_label.grid(row=0, column=0, padx=5, pady=5)
path_entry = tk.Entry(window, width=50)
path_entry.grid(row=0, column=1, padx=5, pady=5)

file_type_label = tk.Label(window, text="File Extension:")
file_type_label.grid(row=1, column=0, padx=5, pady=5)
file_type_entry = tk.Entry(window, width=50)
file_type_entry.grid(row=1, column=1, padx=5, pady=5)

search_term_label = tk.Label(window, text="Search String:")
search_term_label.grid(row=2, column=0, padx=5, pady=5)
search_term_entry = tk.Entry(window, width=50)
search_term_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the search button
search_button = tk.Button(window, text="Search", command=search_files)
search_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create the result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the app
window.mainloop()
