if __name__ == "__main__":
#import the add function from add_0.py
    from add_0 import add
#assign values to variables a and b
    a = 1
    b = 2
#call the add function with arguments a and b
    result = add(a, b)
#print the result using string formatting
    print(f"{a} + {b} = {result}\n")
