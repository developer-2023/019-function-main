# To avoid problems with the order of functions there is a convention used as below.
# Main program is fixed into main() function.
# Scope of variables declared in function is local
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
 