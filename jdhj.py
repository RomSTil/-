import random

def generate_expression():
    expression = ""
    for i in range(1, 10):
        expression += str(i) + " "
        if i < 9:
            expression += random.choice(["+", "-", ""]) + " "
    return expression

def generate_all_expressions():
    operators = ["+", "-", ""]
    expressions = []
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                for op4 in operators:
                    for op5 in operators:
                        for op6 in operators:
                            for op7 in operators:
                                for op8 in operators:
                                    expression = "1 " + op1 + " 2 " + op2 + " 3 " + op3 + " 4 " + op4 + " 5 " + op5 + " 6 " + op6 + " 7 " + op7 + " 8 " + op8 + " 9"
                                    expressions.append(expression)
    return expressions

num_expressions = 5  # Количество выражений, которое нужно сгенерировать

for _ in range(num_expressions):
    expression = generate_expression()
    print(expression)

expressions = generate_all_expressions()
print("\nВсе возможные варианты выражений:")
for expression in expressions:
    print(expression)

print("Генерация выражений завершена!")