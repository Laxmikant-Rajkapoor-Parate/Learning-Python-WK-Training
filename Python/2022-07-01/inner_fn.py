# def outer_fn():
#     text = "Laxmikant"

#     def inner_fn():
#         new_text = text + " Parate"
#         print(new_text)

#     return inner_fn

# fn = outer_fn()
# fn()

def outer_fn():
    local_variable = 10

    def inner_fn():
        x = 10
        return x + local_variable
    
    return inner_fn()

print(outer_fn())