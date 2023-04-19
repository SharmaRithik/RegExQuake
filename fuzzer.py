import random

# Define the tokens
ID = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
ASSIGN_OP = "="
ADD_OP = "+"
MULT_OP = "*"

# Generate random IDs
def generate_id():
    return "".join(random.choices(ID, k=random.randint(1, 10)))

# Generate random numbers
def generate_number():
    integer_part = "".join(random.choices(NUMBERS, k=random.randint(1, 10)))
    if random.random() < 0.5:
        return integer_part
    else:
        decimal_part = "".join(random.choices(NUMBERS, k=random.randint(1, 5)))
        return f"{integer_part}.{decimal_part}"

# Generate random expressions
def generate_expression():
    left = generate_id() if random.random() < 0.5 else generate_number()
    op = random.choice([ADD_OP, MULT_OP])
    right = generate_id() if random.random() < 0.5 else generate_number()
    return f"{left} {op} {right}"

# Generate the test file
with open("test_file.txt", "w") as f:
    for i in range(1000):
        left = generate_id()
        op = ASSIGN_OP
        right = generate_number() if random.random() < 0.5 else generate_expression()
        line = f"{left} {op} {right} {ADD_OP if random.random() < 0.5 else MULT_OP} {generate_id()}\n"
        f.write(line)
