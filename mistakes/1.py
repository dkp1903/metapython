# While looking through the Localstack codebase, I was able to find extensive use of decorators

# I find these analogous to annotations in Java

# However, in python, the lower your decorator is, the higher priority it's given. The same rule doesn't apply in Java, and can be overridden/customized using @Order.

# This is one place where one needs to be careful


def correl_id(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("CorrelID")
        return func(*args, **kwargs)
    return wrapper

def null_adder(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(None)
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add_correl_id_and_null_if_not_found():
    print("CorrelationID added")

my_function()
