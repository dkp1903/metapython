# Decorators have side effects. In case of shared state, the context is on the decorator, not the function being decorated.

# In the below example, we might expect that call_count is overwritten for each time the function is called

# However, the variable is in the local scope of the dec and thus, will be statically updated

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Call count: {wrapper.call_count}")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def my_function():
    print("Function called")

my_function()  # Prints "Call count: 1" and "Function called"
my_function()  # Prints "Call count: 2" and "Function called"
