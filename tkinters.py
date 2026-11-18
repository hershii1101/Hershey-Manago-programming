
import tkinter as tk
from tkinter import messagebox
import json
import os
import hashlib

# ==============================
# ERSI PROGRAMMING GAME
# ==============================

FILE = "users.json"

BG = "#171326"
PANEL = "#241D38"
PURPLE = "#8B5CF6"
LIGHT_PURPLE = "#C4B5FD"
WHITE = "#FFFFFF"
GRAY = "#B8B2C8"
GREEN = "#22C55E"
RED = "#EF4444"

def load_users():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}

def save_users():
    with open(FILE, "w") as file:
        json.dump(users, file)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = load_users()

# ==============================
# LESSON MATERIALS
# ==============================

lesson_materials = {
    "Lesson 1 - Introduction to Programming":
    """INTRODUCTION TO PROGRAMMING

Programming is the process of creating instructions that tell a computer what to do.

An algorithm is a step-by-step procedure used to solve a problem.

Examples of programming languages:
• Python
• Java
• C++
• JavaScript

Programming is used to create applications, websites, games, and computer systems.""",

    "Lesson 2 - Python Basic Syntax":
    """PYTHON BASIC SYNTAX

Python is a programming language known for its simple and readable syntax.

1. print()
Displays information on the screen.
Example: print("Hello World")

2. Comments
Comments explain code and begin with #.
Example: # This is a comment

3. Variables
Variables store information.
Example: name = "Anna"

4. Constants
Constants are values that should not change.
Example: PI = 3.14

5. Basic Data Types
• int - whole numbers
• float - decimal numbers
• str - text
• bool - True or False""",

    "Lesson 3 - Arithmetic Operators":
    """ARITHMETIC OPERATORS

Arithmetic operators are used to perform mathematical operations.

+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
** Exponentiation
// Floor Division

Examples:
print(10 + 5)  # 15
print(10 - 5)  # 5
print(10 * 5)  # 50
print(10 / 5)  # 2.0""",

    "Lesson 4 - Basic Input and Output":
    """BASIC INPUT AND OUTPUT

The input() function allows users to enter information.

The print() function displays information on the screen.

Example:
name = input("Enter your name: ")
print("Hello", name)

Remember:
input() returns a string by default.

To convert input:
age = int(input("Enter your age: "))
price = float(input("Enter price: "))""",

    "Lesson 1 - Conditional Statements":
    """CONDITIONAL STATEMENTS

Conditional statements allow a program to make decisions.

The main conditional statements are:
• if
• elif
• else

Example:

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

The program checks the condition before executing an instruction.""",

    "Lesson 2 - Logical Operators":
    """LOGICAL OPERATORS

Logical operators combine or reverse conditions.

1. AND
Returns True when both conditions are True.

2. OR
Returns True when at least one condition is True.

3. NOT
Reverses the result of a condition.

Example:

age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")""",

    "Lesson 1 - Iteration and Loops":
    """ITERATION AND LOOPS

Loops repeat a block of code.

1. FOR LOOP
Used to repeat code a specific number of times.

Example:
for i in range(5):
    print(i)

2. WHILE LOOP
Repeats while a condition is True.

Example:
x = 1
while x <= 5:
    print(x)
    x += 1

Other loop statements:
• break - stops the loop
• continue - skips the current iteration"""
}

# ==============================
# QUIZ QUESTIONS
# Format: question, choices, correct answer
# ==============================

reviewer = {
    "PRELIMS": {
        "Lesson 1 - Introduction to Programming": [
            ("What is programming?",
             ["Creating computer instructions", "Playing games", "Browsing websites", "Watching videos"], 0),
            ("What is an algorithm?",
             ["A computer virus", "A step-by-step procedure", "A programming language", "A computer part"], 1),
            ("Which is a programming language?",
             ["Microsoft Word", "Google Chrome", "Python", "Windows"], 2)
        ],

        "Lesson 2 - Python Basic Syntax": [
            ("Which function displays output?",
             ["input()", "print()", "type()", "int()"], 1),
            ("What symbol is used for comments in Python?",
             ["//", "/*", "#", "$"], 2),
            ("Which is a valid variable assignment?",
             ["name = 'Ana'", "name == 'Ana'", "name : 'Ana'", "name => 'Ana'"], 0),
            ("Which data type stores whole numbers?",
             ["str", "float", "bool", "int"], 3),
            ("Which data type stores text?",
             ["int", "str", "float", "bool"], 1),
            ("Which data type stores True or False?",
             ["bool", "str", "int", "float"], 0),
            ("Which is commonly used for a constant name?",
             ["myValue", "my value", "PI", "2PI"], 2)
        ],

        "Lesson 3 - Arithmetic Operators": [
            ("Which operator is used for addition?",
             ["-", "*", "+", "/"], 2),
            ("What is the result of 10 % 3?",
             ["3", "1", "0", "10"], 1),
            ("Which operator is used for exponentiation?",
             ["//", "**", "%", "/"], 1)
        ],

        "Lesson 4 - Basic Input and Output": [
            ("Which function accepts user input?",
             ["print()", "input()", "type()", "str()"], 1),
            ("Which function displays information?",
             ["input()", "int()", "print()", "float()"], 2),
            ("What is the default data type returned by input()?",
             ["int", "float", "bool", "str"], 3)
        ]
    },

    "MIDTERMS": {
        "Lesson 1 - Conditional Statements": [
            ("Which statement checks a condition?",
             ["if", "print", "input", "break"], 0),
            ("Which statement is used when the if condition is false?",
             ["for", "else", "while", "continue"], 1),
            ("Which keyword checks another condition?",
             ["and", "or", "elif", "not"], 2),
            ("What is the purpose of conditional statements?",
             ["Repeat code", "Store information", "Display pictures", "Make decisions"], 3)
        ],

        "Lesson 2 - Logical Operators": [
            ("Which operator requires both conditions to be True?",
             ["and", "or", "not", "if"], 0),
            ("Which operator returns True if at least one condition is True?",
             ["and", "or", "not", "else"], 1),
            ("Which operator reverses a condition?",
             ["and", "or", "not", "elif"], 2),
            ("What is True and True?",
             ["False", "None", "True", "Error"], 2),
            ("What is True or False?",
             ["False", "True", "None", "Error"], 1)
        ]
    },

    "FINALS": {
        "Lesson 1 - Iteration and Loops": [
            ("What is the purpose of a loop?",
             ["Store data", "Repeat instructions", "Create variables", "Delete files"], 1),
            ("Which loop is commonly used with range()?",
             ["if", "while", "for", "else"], 2),
            ("Which loop continues while a condition is True?",
             ["while", "if", "else", "break"], 0),
            ("What does break do?",
             ["Starts a loop", "Skips a condition", "Repeats code", "Stops a loop"], 3),
            ("What does continue do?",
             ["Ends the program", "Skips the current iteration", "Creates a variable", "Prints output"], 1),
            ("What does range(5) generate?",
             ["1 to 5", "1 to 4", "0 to 4", "0 to 5"], 2)
        ]
    }
}

# ==============================
# MAIN APPLICATION
# ==============================

class ErsiGame:

    def __init__(self, root):
        self.root = root
        self.root.title("ERSI PROGRAMMING GAME")
        self.root.geometry("950x650")
        self.root.minsize(750, 550)
        self.root.configure(bg=BG)

        self.current_user = None
        self.current_period = None
        self.current_lesson = None
        self.questions = []
        self.question_index = 0
        self.score = 0
        self.answer_buttons = []

        if not users:
            self.register_screen()
        else:
            self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def title(self, parent, text, size=25):
        tk.Label(
            parent,
            text=text,
            font=("Arial", size, "bold"),
            bg=parent["bg"],
            fg=WHITE
        ).pack(pady=12)

    def button(self, parent, text, command, color=PURPLE):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 12, "bold"),
            bg=color,
            fg=WHITE,
            activebackground=LIGHT_PURPLE,
            activeforeground=BG,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )

    def entry(self, parent, placeholder):
        tk.Label(
            parent,
            text=placeholder,
            bg=PANEL,
            fg=GRAY,
            font=("Arial", 11)
        ).pack(anchor="w", pady=(8, 3))

        field = tk.Entry(
            parent,
            font=("Arial", 13),
            bg="#352B4D",
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            show="*" if "Password" in placeholder else ""
        )
        field.pack(fill="x", ipady=9)
        return field

    # ==========================
    # REGISTER
    # ==========================

    def register_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg=PANEL, padx=45, pady=30)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title(frame, "CREATE YOUR ACCOUNT", 23)

        tk.Label(
            frame,
            text="Register first before entering the reviewer.",
            bg=PANEL,
            fg=GRAY,
            font=("Arial", 10)
        ).pack(pady=5)

        self.reg_username = self.entry(frame, "Username")
        self.reg_password = self.entry(frame, "Password")
        self.reg_confirm = self.entry(frame, "Confirm Password")

        self.button(
            frame,
            "CREATE ACCOUNT",
            self.register
        ).pack(fill="x", pady=20)

        if users:
            self.button(
                frame,
                "BACK TO LOGIN",
                self.login_screen,
                "#514568"
            ).pack(fill="x")

    def register(self):
        username = self.reg_username.get().strip()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()

        if not username or not password or not confirm:
            messagebox.showwarning("Missing Information", "Please complete all fields.")
            return

        if username in users:
            messagebox.showerror("Account Exists", "That username is already registered.")
            return

        if password != confirm:
            messagebox.showerror("Password Error", "Passwords do not match.")
            return

        users[username] = hash_password(password)
        save_users()

        messagebox.showinfo(
            "Success",
            "Account created successfully! Please log in."
        )
        self.login_screen()

    # ==========================
    # LOGIN
    # ==========================

    def login_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg=PANEL, padx=45, pady=35)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title(frame, "ERSI PROGRAMMING GAME", 23)

        tk.Label(
            frame,
            text="LOGIN TO CONTINUE",
            bg=PANEL,
            fg=LIGHT_PURPLE,
            font=("Arial", 12, "bold")
        ).pack(pady=8)

        self.login_username = self.entry(frame, "Username")
        self.login_password = self.entry(frame, "Password")

        self.button(
            frame,
            "LOGIN",
            self.login
        ).pack(fill="x", pady=20)

        self.button(
            frame,
            "CREATE NEW ACCOUNT",
            self.register_screen,
            "#514568"
        ).pack(fill="x")

    def login(self):
        username = self.login_username.get().strip()
        password = self.login_password.get()

        if username not in users:
            messagebox.showerror("Login Failed", "Account not found. Please register first.")
            return

        if users[username] != hash_password(password):
            messagebox.showerror("Login Failed", "Incorrect password.")
            return

        self.current_user = username
        messagebox.showinfo("Welcome", "Login successful!")
        self.home_screen()

    # ==========================
    # HOME / PERIOD SELECTION
    # ==========================

    def home_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both")

        self.title(frame, "ERSI PROGRAMMING GAME", 30)

        tk.Label(
            frame,
            text=f"Welcome, {self.current_user}!",
            bg=BG,
            fg=LIGHT_PURPLE,
            font=("Arial", 15, "bold")
        ).pack(pady=5)

        tk.Label(
            frame,
            text="SELECT YOUR EXAMINATION PERIOD",
            bg=BG,
            fg=GRAY,
            font=("Arial", 13)
        ).pack(pady=15)

        for period in ["PRELIMS", "MIDTERMS", "FINALS"]:
            self.button(
                frame,
                period,
                lambda p=period: self.period_screen(p)
            ).pack(pady=10, ipadx=45)

        self.button(
            frame,
            "LOG OUT",
            self.logout,
            "#514568"
        ).pack(pady=25)

    def period_screen(self, period):
        self.current_period = period
        self.clear_screen()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both")

        self.title(frame, period + " REVIEWER", 27)

        tk.Label(
            frame,
            text="SELECT A LESSON TO REVIEW",
            bg=BG,
            fg=GRAY,
            font=("Arial", 12)
        ).pack(pady=10)

        for lesson in reviewer[period]:
            self.button(
                frame,
                lesson,
                lambda l=lesson: self.lesson_screen(l)
            ).pack(pady=8, ipadx=10)

        self.button(
            frame,
            "BACK",
            self.home_screen,
            "#514568"
        ).pack(pady=20)

    # ==========================
    # LESSON REVIEW
    # ==========================

    def lesson_screen(self, lesson):
        self.current_lesson = lesson
        self.clear_screen()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=20)

        self.title(frame, lesson, 20)

        text_frame = tk.Frame(frame, bg=PANEL)
        text_frame.pack(fill="both", expand=True, pady=10)

        text_widget = tk.Text(
            text_frame,
            wrap="word",
            font=("Arial", 12),
            bg=PANEL,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=20
        )
        text_widget.pack(fill="both", expand=True)

        text_widget.insert("1.0", lesson_materials.get(lesson, "No lesson material available."))
        text_widget.config(state="disabled")

        self.button(
            frame,
            "START QUIZ",
            self.start_quiz
        ).pack(pady=10)

        self.button(
            frame,
            "BACK TO LESSON MENU",
            lambda: self.period_screen(self.current_period),
            "#514568"
        ).pack()

    # ==========================
    # QUIZ
    # ==========================

    def start_quiz(self):
        self.questions = reviewer[self.current_period][self.current_lesson]
        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True, padx=40, pady=25)

        total = len(self.questions)

        self.title(frame, "QUIZ TIME!", 27)

        tk.Label(
            frame,
            text=f"QUESTION {self.question_index + 1} OF {total}",
            bg=BG,
            fg=LIGHT_PURPLE,
            font=("Arial", 13, "bold")
        ).pack(pady=10)

        question, choices, correct = self.questions[self.question_index]

        question_box = tk.Frame(frame, bg=PANEL, padx=20, pady=25)
        question_box.pack(fill="x", pady=20)

        tk.Label(
            question_box,
            text=question,
            bg=PANEL,
            fg=WHITE,
            font=("Arial", 16, "bold"),
            wraplength=750,
            justify="center"
        ).pack()

        self.answer_buttons = []

        for index, choice in enumerate(choices):
            btn = self.button(
                frame,
                f"{index + 1}. {choice}",
                lambda i=index: self.check_answer(i),
                "#352B4D"
            )
            btn.pack(fill="x", pady=6)
            self.answer_buttons.append(btn)

        tk.Label(
            frame,
            text=f"CURRENT SCORE: {self.score}",
            bg=BG,
            fg=GRAY,
            font=("Arial", 11)
        ).pack(pady=15)

    def check_answer(self, selected):
        question, choices, correct = self.questions[self.question_index]

        for btn in self.answer_buttons:
            btn.config(state="disabled")

        if selected == correct:
            self.score += 1
            self.answer_buttons[selected].config(bg=GREEN)
            messagebox.showinfo("Correct!", "Great job! Your answer is correct.")
        else:
            self.answer_buttons[selected].config(bg=RED)
            self.answer_buttons[correct].config(bg=GREEN)
            messagebox.showerror(
                "Incorrect!",
                f"The correct answer is: {choices[correct]}"
            )

        self.question_index += 1

        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.result_screen()

    # ==========================
    # RESULTS
    # ==========================

    def result_screen(self):
        self.clear_screen()

        total = len(self.questions)
        percentage = (self.score / total) * 100

        if percentage >= 90:
            remark = "EXCELLENT!"
        elif percentage >= 80:
            remark = "VERY GOOD!"
        elif percentage >= 75:
            remark = "PASSED!"
        else:
            remark = "KEEP PRACTICING!"

        frame = tk.Frame(self.root, bg=PANEL, padx=45, pady=35)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title(frame, "QUIZ COMPLETED!", 27)

        tk.Label(
            frame,
            text=f"{self.current_lesson}",
            bg=PANEL,
            fg=LIGHT_PURPLE,
            font=("Arial", 12, "bold"),
            wraplength=450
        ).pack(pady=8)

        tk.Label(
            frame,
            text=f"{self.score} / {total}",
            bg=PANEL,
            fg=WHITE,
            font=("Arial", 35, "bold")
        ).pack(pady=8)

        tk.Label(
            frame,
            text=f"YOUR SCORE: {percentage:.1f}%",
            bg=PANEL,
            fg=LIGHT_PURPLE,
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        tk.Label(
            frame,
            text=remark,
            bg=PANEL,
            fg=GREEN if percentage >= 75 else RED,
            font=("Arial", 18, "bold")
        ).pack(pady=12)

        self.button(
            frame,
            "RETAKE QUIZ",
            self.start_quiz
        ).pack(fill="x", pady=6)

        self.button(
            frame,
            "REVIEW LESSON AGAIN",
            lambda: self.lesson_screen(self.current_lesson)
        ).pack(fill="x", pady=6)

        self.button(
            frame,
            "BACK TO LESSON MENU",
            lambda: self.period_screen(self.current_period),
            "#514568"
        ).pack(fill="x", pady=6)

        self.button(
            frame,
            "HOME",
            self.home_screen,
            "#514568"
        ).pack(fill="x", pady=6)

    # ==========================
    # LOGOUT
    # ==========================

    def logout(self):
        confirm = messagebox.askyesno(
            "Logout",
            "Are you sure you want to log out?"
        )

        if confirm:
            self.current_user = None
            self.login_screen()


# ==============================
# RUN THE GAME
# ==============================

root = tk.Tk()
app = ErsiGame(root)
root.mainloop()
