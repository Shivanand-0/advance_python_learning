# def my_decorater(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper

# def say_hello():
#     print("guten morgen!!!!")


# # method1
# exec_decorater=my_decorater(say_hello)
# exec_decorater()

# #method2
# @my_decorater
# def say_hello():
#     print("guten morgen!!!!")


# say_hello()



# decorater aplication (in autharization, logger,)

def my_decorater(func):
    def wrapper(user):
        if user=="admin":
            return func(user)
        else:
            print("you are not allowed to access!")
    return wrapper

@my_decorater
def dashboard(user):
    print("Welcome to Dashboard!")

dashboard("shiv")


