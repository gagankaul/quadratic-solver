import cmath

print("\nWelcome to the Quadratic Solver App\n\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two part: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

#Get user input
num_eq = int(input("\nHow many equations would you like to solve today? "))

#Defining a function to solve a quadratic equation

def quadsolver():
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your vlaue of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
  
    x1 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)

    print(f"\nThe solutions to {a}x^2 + {b}x + {c} = 0 are:")
    print("\n\tx1 = " + str(x1))
    print("\n\tx2 = " + str(x2))

for i in range (num_eq):
    print("\nSolving equation #" + str(i+1))
    print("---------------------------------------\n")
    quadsolver()
print("\nThank you for using the Quadratic Solver App. Goodbye!")