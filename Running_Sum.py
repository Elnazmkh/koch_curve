
def running_sum():
    """
    Returns the running sum of some numbers that user enters up until a 0 is enterd.

    Parameters :
    None

    Returns :

    sum1 (float) : running sum of numbers given by user.

    """
    sum = 0
    b = input("Enter Numbers to add (enter 0 to stop): ")
    while b != "0":
        try :
            sum = sum + float(b)
            b = input("Next Number :")
        except:
            print("Not a valid Number")
            b = input("Next Number :")
    return sum


print("the Sum is : " + str(running_sum()))