# 🗂️ File Management System using Python (CRUD Operations)

**📘 Overview**

This project is a File Management System built using Python, allowing users to perform fundamental CRUD (Create, Read, Update, Delete) operations directly from the command line.

It leverages Python’s built-in modules like pathlib and os to handle files efficiently and in a platform-independent way. The script provides an interactive experience for beginners exploring Python file handling.

**⚙️ Features**
Operation	Description
📝 Create:	Create new files directly from the terminal and optionally write data into them.
📖 Read:	Display the contents of any file in the current working directory.
✏️ Update:	Rename, overwrite, or append content to an existing file.
🗑️ Delete:	Safely remove files from the system after user confirmation.

**🧠 Breakdown of Workflow**
**1️⃣ View Available Files**

The program starts by listing all files and folders in the current directory using:
Path('').rglob('*')
This ensures you can see what files exist before performing any action.

**2️⃣ Choose an Operation**
You’ll be directed to select an option:

Press 1 for creating a file  
Press 2 for reading a file  
Press 3 for updating a file  
Press 4 for deleting a file

**3️⃣ Perform CRUD Operations**
📝 Create a File

Ask the user to name the new file.

Optionally allows if the user wants to write anything.

Prevents overwriting if the file already exists.

📖 Read a File

Displays the contents of the chosen file.

Ensures the file exists before reading.

✏️ Update a File

Offers three update modes:

Rename – Change the file’s name.

Overwrite – Replace the entire content.

Append – Add new text at the end.

🗑️ Delete a File

Safely deletes a file if it exists.

Provides confirmation messages for user awareness.

**💡 Concepts Demonstrated**

1. File handling (open, read, write, append)

2. Path management using pathlib.Path

3. OS operations (os.rename, os.remove)

4. Exception handling for robust error control


**🧰 Tech Stack**

Language: Python

Libraries: os, pathlib

**🌟 Why This Project Matters**

This project demonstrates:

1. Hands-on understanding of Python’s file handling process

2. Ability to write modular, user-interactive scripts

3. Awareness of error handling and clean coding practices

4. It’s an ideal example of how to blend logic, usability, and structure in a simple yet functional Python program.


