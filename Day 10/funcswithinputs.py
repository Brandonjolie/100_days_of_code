def format_name(f_name, l_name):
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return (formatted_fname, formatted_lname, f_name)


val = format_name('bjolie', 'jest')
print(val)
