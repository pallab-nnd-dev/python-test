
def fun1(msg): # outer function
    
    def fun2(msg2): # inner function
        print(msg)
        print(msg2)
    fun2("Hello 2 Again")



fun1("Hello")
