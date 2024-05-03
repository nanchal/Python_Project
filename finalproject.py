import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys


AND_Table=[  #Table for AND
    ["INPUT 1(A)", "INPUT 2(B)", "OUTPUT(A.B)"],
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [1,1,1]
]

OR_Table=[  #Table for OR
    ["INPUT 1(A)", "INPUT 2(B)", "OUTPUT(A+B)"],
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [1,1,1]
]

NOT_Table=[  #Table for NOT
    ["INPUT(A)", "OUTPUT(A)"],
    [0,1],
    [1,0]
]

NAND_Table=[  #Table for NAND
    ["INPUT 1(A)", "INPUT 2(B)", "OUTPUT(A.B)"],
    [0,0,1],
    [1,0,1],
    [0,1,1],
    [1,1,0]
]

NOR_Table=[  #Table for NOR
    ["INPUT 1(A)", "INPUT 2(B)", "OUTPUT(A+B)"],
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [1,1,1]
]

XOR_Table=[  #Table for XOR
    ["INPUT 1(A)", "INPUT 2(B)", "OUTPUT(A.B)"],
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [1,1,0]
]

XNOR_Table=[  #Table for XAND
    ["INPUT 1(A)", "INPUT 2(B)", "OUTPUT(A.B)"],
    [0,0,1],
    [1,0,0],
    [0,1,0],
    [1,1,1]
]

# Function to read quiz questions from file
def read_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            question, answer = line.strip().split('|')
            questions.append((question, answer))
    return questions

# Function to add new question to file
def add_question(filename, question, answer):
    with open(filename, 'a') as file:
        file.write(question + '|' + answer + '\n')

# Function to display truth table
def display_truth_table(truth_table):
    for row in truth_table:
        print("|".join(str(cell).ljust(10) for cell in row))

# Function to display gate image
def display_gate_image(gate):
    img_path = r'C:\Users\Lenovo\OneDrive\Desktop\gate.png'  # Change path to your gate image
    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Quiz function
def quiz():
    print("Welcome to the Logic Gate Quiz!")
    print("Answer the following questions:")
    score = 0
    # Read questions from file
    questions = read_questions('quiz_questions.txt')
    random.shuffle(questions)  # Shuffle questions
    # Ask questions
    for question, answer in questions:
        user_answer = input(question + "\nYour answer: ").strip().lower()
        if user_answer == answer.lower():
            score += 1
    print("Quiz completed! Your score:", score, "/", len(questions))
    # Analyze score...
    if score == len(questions):
        print("Congratulations! You scored full marks. You have a strong understanding of logic gates.")
    elif score >= len(questions) / 2:
        print("Good job! You have a decent understanding of logic gates. Keep practicing for improvement.")
    else:
        print("You need improvement. Review the concepts and try again.")

# Function to play the game
import random

# Function to generate a random logic gate puzzle
def generate_logic_gate_puzzle():
    gates = ['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XOR', 'XNOR']
    inputs = random.choices([0, 1], k=2)  # Generate random input values
    gate = random.choice(gates)  # Select a random gate
    output = None
    # Compute the output based on the selected gate
    if gate == 'AND':
        output = inputs[0] and inputs[1]
    elif gate == 'OR':
        output = inputs[0] or inputs[1]
    elif gate == 'NOT':
        output = not inputs[0]
    elif gate == 'NAND':
        output = not (inputs[0] and inputs[1])
    elif gate == 'NOR':
        output = not (inputs[0] or inputs[1])
    elif gate == 'XOR':
        output = inputs[0] != inputs[1]
    elif gate == 'XNOR':
        output = inputs[0] == inputs[1]
    return inputs, gate, output

# Function to play the logic gate puzzle game
def play_logic_gate_puzzle_game(num_puzzles):
    print("Welcome to the Logic Gate Puzzle Game!")
    print("Solve the following logic gate puzzles:")

    correct_answers = 0
    # Generate and solve logic gate puzzles
    for i in range(num_puzzles):
        inputs, gate, output = generate_logic_gate_puzzle()
        print(f"Puzzle {i+1}: Inputs: {inputs}, Gate: {gate}")
        user_input = input("Enter the output (True/False): ").lower()
        if user_input == str(output).lower():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")

    print(f"Game Over! You solved {correct_answers} out of {num_puzzles} puzzles.")


# Main program
print("WELCOME TO THE DIGITAL WORLD!\nChoose any option and find your gate:)")
print("\nHave a look at the following menu:-\n1. Introduction\n2. Truth Table\n3. Gate Display\n4.  Applications\n5. Quiz\n6. Game\n7. Exit")

welcome = True

while welcome:
    choice = int(input("Enter number as per the above provided menu: "))

    if choice == 1:
        gate = input("Enter the gate for introduction: ")
        if gate.lower()=="and":
            print("Defination of AND GATE:-\nIn digital electronics, Basic logic gate which is AND gate is one of the basic logic gate that performs the logical multiplication of inputs applied to it.\n"
          "It generates a high or logic 1 output, only when all the inputs applied to it are high or logic 1. Otherwise, the output of the AND gate is low or logic 0.\n\n"
          "Properties of AND GATE:-\n1. AND gate can accept two or more than two input values at a time.\n2. When all of the inputs are logic 1, the output of this gate is logic 1.\n\n"
          "Boolean Expression for AND GATE:-\nZ=A.B, where A and B are inputs to the AND gate, while Z denotes the output of the AND gate.")

        elif gate.lower()=="or":
            print("Defination of OR GATE:-\nIn digital electronics, there is a type of basic logic gate which produces a low or logic 0 output only when its all inputs are low or logic 0.\n"
           "For all other input combinations, the output of the OR gate is high or logic 1.\n"
           "An OR gate can be designed to have two or more inputs but only one output.\n"
           "The primary function of the OR gate is to perform the logical sum operation.\n\n"
           "Properties of OR GATE:-\n1. It can have two or more input lines at a time.\n2. When all of the inputs to the OR gate are low or logic 0, the output of it is low or logic 0.\n\n"
           "Boolean Expression for OR GATE:-\nZ=A+B, where A and B are inputs to the OR gate, while z denotes the output of the OR gate.")

        elif gate.lower()=="not":
            print("Defination of NOT GATE:-\nIn digital electronics, the NOT gate is another basic logic gate used to perform compliment of an input signal applied to it.\n"
              "It takes only one input and one output. The output of the NOT gate is complement of the input applied to it. Therefore, if we apply a low or logic 0 output to the NOT gate is gives a high or logic 1 output and vice-versa.\n"
              "The NOT gate is also known as inverter, as it performs the inversion operation.\n\n"
              "Properties of NOT GATE:-\n1. The output of a NOT gate is complement or inverse of the input applied to it.\n2. NOT gate takes only one output.\n\n"
              "Boolean Expression for NOT GATE:-\nZ=A complement. where A is input and z is the outside denoting complement of input.")

        elif gate.lower()=="nor":
            print("Defination of NOR GATE:-\nThe NOR gate is a type of universal logic gate that can take two or more inputs but one output.\n"
              "It is basically a combination of two basic logic gates i.e., OR gate and NOT gate. Thus, it can be expressed as,\nNOR Gate = OR Gate + NOT Gate\n\n"
              "Properties of NOR GATE:-\n1. A NOR gate can have two or more inputs and gives an output.\n2. A NOR gate gives a high or logic 1 output only when its all inputs are low or logic 0.\n\n"
              "Boolean Expression for NOR GATE:-\nZ=A+B complement, where A and B are input and Z is output")

        elif gate.lower()=="nand":
            print("Defination of NAND GATE:-\nIn digital electronics, the NAND gate is another type of universal logic gate used to perform logical operations.\nThe NAND gate performs the inverted operation of the AND gate.\n"
              "Similar to NOR gate, the NAND gate can also have two or more input lines but only one output line.\n\n"
              "Properties of NAND GATE:-\n1. NAND gate can take two or more inputs at a time and produces one output based on the combination of inputs applied.\n2. NAND gate produces a low or logic 0 output only when its all inputs are high or logic 1.\n\n"
              "Boolean for NAND GATE:-\nZ=A.B complement, where A and B are input and Z is output")

        elif gate.lower()=="xor":
            print("Defination of XOR GATE:-\nIn digital electronics, there is a specially designed logic gate named, XOR gate, which is used in digital circuits to perform modulo sum. It is also referred to as Exclusive OR gate or Ex-OR gate.\n"
              "The XOR gate can take only two inputs at a time and give an output. The output of the XOR gate is high or logic 1 only when its two inputs are dissimilar.\n\n"
              "Properties of XOR GATE:-\n1. It can accept only two inputs at a time. There is nothing like a three or more input XOR gate.\n2. The output of the XOR gate is logic 1 or high, when its inputs are dissimilar.\n\n"
              "Boolean Expression for XOR GATE:-\nZ=A modulo sum B or (A.B complement + A complement.B), where A and B are input and Z is output")

        elif gate.lower()=="xnor":
            print("Defination of XNOR GATE:-\nThe XNOR gate is another type of special purpose logic gate used to implement exclusive operation in digital circuits.\n"
              "It is used to implement the Exclusive NOR operation in digital circuits. It is also called the Ex-NOR or Exclusive NOR gate. It is a combination of two logic gates namely, XOR gate and NOT gate. Thus, it can be expressed as,\n"
              "XNOR Gate = XOR Gate + NOT Gate\n"
              "The output of an XNOR gate is high or logic 1 when its both inputs are similar. Otherwise the output is low or logic 0.\n"
              "Hence, the XNOR gate is used as a similarity detector circuit.\n\n"
              "Properties of XNOR GATE:-\n1. XNOR gate takes only two inputs and produces one output.\n2. The output of the XNOR gate is high or logic 1 only when it has similar inputs.\n\n"
              "Boolean Expression for XNOR GATE:-\nZ=A.B + A.B complement, where A and B are input and Z is output")

        else:
            print("Invallid Gate Entered!")

    elif choice == 2:
        gate = input("Enter the gate for Truth Table (AND, OR, NOT, NAND, NOR, XOR, XNOR): ")
        if gate.upper() == "AND":
            display_truth_table(AND_Table)
        elif gate.upper() == "OR":
            display_truth_table(OR_Table)
        elif gate.upper() == "NOT":
            display_truth_table(NOT_Table)
        elif gate.upper() == "NAND":
            display_truth_table(NAND_Table)
        elif gate.upper() == "NOR":
            display_truth_table(NOR_Table)
        elif gate.upper() == "XOR":
            display_truth_table(XOR_Table)
        elif gate.upper() == "XNOR":
            display_truth_table(XNOR_Table)
        else:
            print("Invalid gate entered!")
            
    elif choice == 3:
        gate = input("Enter the gate for Viewing Gate (AND, OR, NOT, NAND, NOR, XOR, XNOR): ")
        if gate.lower() == "and":
            display_gate_image("AND")
        elif gate.lower() == "or":
            display_gate_image("OR")
        elif gate.lower() == "not":
            display_gate_image("NOT")
        elif gate.lower() == "nand":
            display_gate_image("NAND")
        elif gate.lower() == "nor":
            display_gate_image("NOR")
        elif gate.lower() == "xor":
            display_gate_image("XOR")
        elif gate.lower() == "xnor":
            display_gate_image("XNOR")
        else:
            print("Invalid gate entered!")

    elif choice==4:
        print("Logic gates are the fundamental building blocks of all digital circuits and devices like computers. Here are some key digital devices in which logic gates are utilized to design their circuits:\n"
          "Computers\nMicroprocessors\nMicrocontrollers\nDigital and smart watches\nSmartphones, etc.")
    elif choice == 5:
        quiz()  # Call the quiz function
    elif choice == 6:
        num_puzzles = int(input("Enter the number of logic gate puzzles you want to solve: "))
        play_logic_gate_puzzle_game(num_puzzles)
    elif choice == 7:
        print("Thank You For Visiting. Have A Great Day:)")
        welcome = False
    else:
        print("Invalid option chosen")

    if welcome:
        ask = input("Do You Want To Re-enter(y/n): ")
        if ask.lower() != "y":
            print("Thank You For Visiting. Have A Great Day:)")
            welcome = False
