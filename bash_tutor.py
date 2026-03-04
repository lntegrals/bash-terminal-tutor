import marimo

__generated_with = "0.1.0"
app = marimo.App(title="Bash Terminal Tutor")

@app.cell
def title():
    marimo.md("""# 🖥️ Bash Terminal Tutor

Welcome to an interactive way to learn the bash terminal!""")


@app.cell
def navigation():
    marimo.md("""## 🚀 Getting Started

Select a lesson from the menu below to begin your bash journey!""")


@app.cell
def lesson_selector():
    import marimo as mo

    lesson = mo.ui.dropdown(
        label="Choose a Lesson",
        options=[
            "1. Navigation: ls, cd, pwd",
            "2. File Operations: mkdir, touch, rm",
            "3. Copy & Move: cp, mv",
            "4. Reading Files: cat, head, tail",
            "5. Search: grep, find",
            "6. Permissions: chmod, chown",
            "7. Pipes & Redirection: |, >, >>",
        ],
        value="1. Navigation: ls, cd, pwd",
    )
    lesson


@app.cell
def show_lesson():
    import marimo as mo

    lessons = {
        "1. Navigation: ls, cd, pwd": {
            "content": """
### 📂 Navigation Commands

**pwd** - Print Working Directory
```bash
$ pwd
/home/user
```
Shows you where you are in the filesystem.

**ls** - List Directory Contents
```bash
$ ls
Documents  Downloads  Pictures  Music

$ ls -la   # List all files with details
total 32
drwxr-xr-x  5 user  staff   160 Jan  1 12:00 .
drwxr-xr-x  1 root  root   4096 Jan  1 12:00 ..
```

**cd** - Change Directory
```bash
$ cd Documents    # Go into Documents
$ cd ..          # Go up one level
$ cd ~           # Go to home directory
$ cd -           # Go back to previous directory
```
""",
            "exercise": "Try: cd Documents"
        },
        "2. File Operations: mkdir, touch, rm": {
            "content": """
### 📄 File Operations

**mkdir** - Make Directory
```bash
$ mkdir myfolder        # Create a directory
$ mkdir -p a/b/c        # Create nested directories
```

**touch** - Create Empty File
```bash
$ touch myfile.txt     # Create an empty file
$ touch file1 file2    # Create multiple files
```

**rm** - Remove Files/Directories
```bash
$ rm myfile.txt        # Remove a file
$ rm -r myfolder      # Remove a directory and its contents
$ rm -f myfile        # Force remove (no prompt)
```
""",
            "exercise": "Try: mkdir practice && touch practice/hello.txt"
        },
        "3. Copy & Move: cp, mv": {
            "content": """
### 📋 Copy & Move

**cp** - Copy Files
```bash
$ cp file1.txt file2.txt       # Copy file
$ cp -r folder1 folder2         # Copy folder
$ cp *.txt backup/              # Copy all .txt files
```

**mv** - Move/Rename Files
```bash
$ mv oldname.txt newname.txt   # Rename file
$ mv file.txt folder/          # Move file to folder
```
""",
            "exercise": "Try: cp important.txt backup.txt"
        },
        "4. Reading Files: cat, head, tail": {
            "content": """
### 📖 Reading Files

**cat** - Concatenate & Display
```bash
$ cat myfile.txt                # Display entire file
$ cat file1.txt file2.txt       # Display multiple files
```

**head** - First Lines
```bash
$ head myfile.txt              # First 10 lines
$ head -n 5 myfile.txt         # First 5 lines
```

**tail** - Last Lines
```bash
$ tail myfile.txt              # Last 10 lines
$ tail -n 5 myfile.txt         # Last 5 lines
$ tail -f log.txt              # Follow (watch) a growing file
```
""",
            "exercise": "Try: head -n 5 /etc/passwd"
        },
        "5. Search: grep, find": {
            "content": """
### 🔍 Search Commands

**grep** - Search Within Files
```bash
$ grep "hello" myfile.txt              # Find lines with "hello"
$ grep -i "hello" myfile.txt           # Case-insensitive search
$ grep -r "hello" ./                   # Recursive search
$ grep -n "hello" myfile.txt          # Show line numbers
```

**find** - Search for Files
```bash
$ find . -name "*.txt"                # Find all .txt files
$ find . -type d                      # Find all directories
$ find . -mtime -7                    # Files modified in last 7 days
```
""",
            "exercise": "Try: grep -i 'error' logfile.txt"
        },
        "6. Permissions: chmod, chown": {
            "content": """
### 🔐 Permissions

**chmod** - Change Mode (Permissions)
```bash
$ chmod 755 script.sh         # rwxr-xr-x
$ chmod +x script.sh          # Make executable
$ chmod -w file.txt           # Remove write permission

# Permission codes:
# r = 4 (read), w = 2 (write), x = 1 (execute)
# Owner | Group | Others
```

**chown** - Change Owner
```bash
$ chown user:group file.txt
$ chown -R user:group folder/
```
""",
            "exercise": "Try: chmod +x myscript.sh"
        },
        "7. Pipes & Redirection: |, >, >>": {
            "content": """
### 🔗 Pipes & Redirection

**|** (Pipe) - Send output to another command
```bash
$ ls | grep ".txt"           # List only .txt files
$ cat file | head -5        # First 5 lines of file
```

**>** - Redirect Output (overwrite)
```bash
$ echo "hello" > file.txt   # Write to file (overwrites)
$ ls > files.txt            # Save listing to file
```

**>>** - Redirect Output (append)
```bash
$ echo "world" >> file.txt  # Append to file
```

**<** - Input Redirection
```bash
$ sort < unsorted.txt       # Sort contents of file
```
""",
            "exercise": "Try: cat file.txt | grep 'important'"
        },
    }
    
    selected = lesson.value
    info = lessons.get(selected, {})
    
    marimo.md(f"""
{info.get('content', '')}

---

### ✏️ Exercise

{info.get('exercise', 'Select a lesson')}
""")


@app.cell
def terminal():
    import marimo as mo

    marimo.md("""## 💻 Try It Yourself!

Use the terminal below to practice commands:""")


@app.cell
def terminal_output():
    import marimo as mo

    command = mo.ui.text(
        label="Enter a command",
        placeholder="e.g., ls -la",
    )
    command


@app.cell
def run_command():
    import subprocess
    import marimo as mo

    result = mo.ui.code_rendered()

    if command.value:
        try:
            output = subprocess.run(
                command.value,
                shell=True,
                capture_output=True,
                text=True,
                timeout=5,
            )
            out = output.stdout if output.stdout else output.stderr
            marimo.md(f"""```
$ {command.value}
{out if out else '(no output)'}
```""")
        except Exception as e:
            marimo.md(f"Error: {e}")
    else:
        marimo.md("Enter a command above to see output")


@app.cell
def progress():
    import marimo as mo

    marimo.md("""## 📊 Your Progress

| Lesson | Status |
|--------|--------|
| 1. Navigation | ⬜ Not Started |
| 2. File Operations | ⬜ Not Started |
| 3. Copy & Move | ⬜ Not Started |
| 4. Reading Files | ⬜ Not Started |
| 5. Search | ⬜ Not Started |
| 6. Permissions | ⬜ Not Started |
| 7. Pipes & Redirection | ⬜ Not Started |""")


@app.cell
def resources():
    marimo.md("""## 📚 More Resources

- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)
- [Explain Shell](https://explainshell.com/)

---

*Happy Learning! 🚀*
""")


if __name__ == "__main__":
    app.run()
