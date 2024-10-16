
def get_input():
    while True:
        try:
            x = int(input(" x: "))
            y = int(input("y "))
            return x, y
        except ValueError:
            print("Lūdzu ievadiet veselu skaitli.")

def calculate_expressions(x, y):
    result_1 = (2 + x) / (x * y)
   
    result_2 = 5 * x**3 - x**2 + 7 * x - 6
   
    result_3 = (x * y)**0.5
   
    result_4 = (2 * x * y) / (5 * y)
   
    return result_1, result_2, result_3, result_4

def main():
    x, y = 5, 2  
   
    results = calculate_expressions(x, y)
   
    for i, result in enumerate(results, 1):
        print(f"{i}) rezultats = {result}")

if __name__ == "__main__":
    main()
