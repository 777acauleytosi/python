
def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print? "))
    for i in range(20) :
        x =  2.0 * x * (1 - x)
        print(x)
main()
