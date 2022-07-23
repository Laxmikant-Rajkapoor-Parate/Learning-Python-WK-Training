# global_var = 10

# def fun():
#     global_var = 20

# fun()
# print(global_var)

global_var = 10

def fun():
    global global_var
    global_var = 20

fun()
print(global_var)