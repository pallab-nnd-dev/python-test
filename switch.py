# This code runs only in python 3.10 or above versions
def number_to_string(pallab):
    match pallab:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
 

head = number_to_string(1)
print(head)