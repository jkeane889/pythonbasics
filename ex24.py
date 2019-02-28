print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

# Here we are creating a long string inside triple quotes
poem = '''
    \tThe lovely world
    with logic so firmly planted
    cannot discern \n the needs of love
    nor coprehend passion from intuition
    and requires an explanation
    \n\twhere there is none.
    '''

# here we are calling the function print and printing our string "poem" to the console
print("-----------")
print(poem)
print("-----------")

# here we define a new function "secret_formula" and assign variables to be called, whereby it returns the values of
#  jelly_beans, jars and crates
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("with a starting point of: {}".format(start_point))
# it's just like with an "f" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Here we take our defined constant, "start_point", and divide it by 10.
start_point = start_point / 10

print("We can also do that this way: ")
formula = secret_formula(start_point)
# this is an easy way to apply a list to format a string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
