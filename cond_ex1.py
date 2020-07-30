# Name: cond_ex1.py
#
# Description:
#
# This program prints prices of tickets depending on age.


def main():
    age=int(input("\nEnter your age: "))
    if age<=16:
        print("Your ticket costs {0:1} pounds".format(6/2))
    elif age>=60:
        print("Your ticket costs {0:1} pounds".format(6/3))
    else:
        print ("Your ticket costs {0:1} pounds".format(6))
    print ("BYE")

if __name__ == "__main__":
    main()
