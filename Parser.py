def is_simple_grammar(rules):
    for nt in rules:  # Iterate through each non-terminal in the grammar
        for rule in rules[nt]:  # Check all production rules for that non-terminal
            # Check if the rule contains more than one non-terminal (uppercase letters)
            if len([ch for ch in rule if ch.isupper()]) > 1:
                return False
    return True


def recursive_descent_parser(rules, input_string, start_symbol):
    def match(stack, index):
        if not stack:  # If stack is empty, check if input is fully consumed
            return index == len(input_string), stack, input_string[index:]
        if index >= len(input_string):  # If input is exhausted but stack isn't
            return False, stack, input_string[index:]

        top = stack.pop()
        current_char = input_string[index]

        if top.isupper():  # Non-terminal
            for rule in rules[top]:
                # Copy stack and attempt to apply the rule
                new_stack = stack[:]
                new_stack.extend(reversed(rule))  # Push rule in reverse
                accepted, final_stack, remaining = match(new_stack, index)
                if accepted:
                    return True, final_stack, remaining
            return False, stack, input_string[index:]  # No rules matched

        elif top == current_char:  # Terminal matches input
            return match(stack, index + 1)

        return False, stack, input_string[index:]  # Terminal doesn't match

    return match([start_symbol], 0)


def main():
    while True:  # Outer loop to allow multiple grammar checks
        print("👇 Grammars 👇")
        rules = {}  # Initialize grammar rules as a dictionary
        num_non_terminals = int(
            input("Enter number of non-terminals: ")
        )  # Ask for the number of non-terminals

        for _ in range(num_non_terminals):
            non_terminal = input("Enter non-terminal: ")
            rules[non_terminal] = []
            for i in range(1, 3):
                rule = input(
                    f"Enter rule number {i} for non-terminal '{non_terminal}': "
                )
                rules[non_terminal].append(rule)

        if not is_simple_grammar(rules):
            print("The Grammar isn't simple. ❌")
            print("Try again\n")
            continue

        print("The Grammar is Simple ✅")
        start_symbol = input("Enter the start symbol: ")

        while True:
            print("\n===================================")
            print("1- Another Grammar.\n2- Another String.\n3- Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                break
            elif choice == "2":
                input_string = input("Enter the string to be checked: ")
                accepted, stack, remaining = recursive_descent_parser(
                    rules, list(input_string), start_symbol
                )
                print(f"The input String: {list(input_string)}")
                print(f"Stack after checking: {stack}")
                print(f"The rest of unchecked string: {remaining}")
                if accepted:
                    print("Your input String is Accepted. ✅")
                else:
                    print("Your input String is Rejected. ❌")
            elif choice == "3":
                print("Exiting... ")  # Fixed exit emoji
                return
            else:
                print("Invalid choice! Try again")


if __name__ == "__main__":
    main()
