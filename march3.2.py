#keyword argument
def my_func(name,age):
    print(f"welcome {name}.You're {age} years old")
#my_func("tina",25)
#my_func(25,"tina") 
my_func(name="tina",age=25)  
my_func("tina",age=25)
#my_func(name="tina",25)  