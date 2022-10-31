def format_name(f_name, l_name):
    """Docstring:it takes the first and last name
    as input and returns the formatted output  in the title format"""
    return (f_name.title() + " " + l_name.title())

lname,fname = input("what is your last name? "), input("what is your first name? ")
print(format_name(fname, lname))