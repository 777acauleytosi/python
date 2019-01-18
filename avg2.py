# avg2.py
# A program to average three scores
# by: Macauley Tosi

def main():
    print("This program averages three scores you give.")
    x = eval(input("Enter your first score from 1 to 100 "))
    y = eval(input("Enter your second score from 1 to 100 "))
    z = eval(input("Enter your thrid score from 1 to 100 "))
    for i in range (1):
        i = (x + y + z) / 3
        print (" your average is a")
        print(i)
    input("Press the <Enter> key to quit.")
main ()
