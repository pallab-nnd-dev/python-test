def multiply_values(x,y):
    """Calculate product of two inputs. 
    
    Parameters
    ----------
    x : int or float
    y : int or float

    Returns
    ------
    z : int or float
    """
    z = x - y
    return z

# Call function with numeric values
print(multiply_values(x = 0.7, y = 25.4))
print(multiply_values(0.7,25.4))
print(multiply_values(y = 25.4, x = 0.7))
