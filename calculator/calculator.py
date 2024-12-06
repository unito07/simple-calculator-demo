class Calculator:
    """A simple calculator class to demonstrate project structure"""

    def add(self, x, y):
        """Add two numbers"""
        return x + y

    def subtract(self, x, y):
        """Subtract y from x"""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y

    def divide(self, x, y):
        """Divide x by y"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    calc = Calculator()
    print("Simple Calculator")
    print("-" * 20)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter operation (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice!")
            continue
            
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            
            if choice == '1':
                result = calc.add(x, y)
                print(f"{x} + {y} = {result}")
            elif choice == '2':
                result = calc.subtract(x, y)
                print(f"{x} - {y} = {result}")
            elif choice == '3':
                result = calc.multiply(x, y)
                print(f"{x} * {y} = {result}")
            elif choice == '4':
                try:
                    result = calc.divide(x, y)
                    print(f"{x} / {y} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()