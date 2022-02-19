#functions with outputs
f_name = input("What is your first name?")

l_name = input("What is your last name?")



def format_name(fname, lname):
  """Takes the first and last name and 
  format it so that the first letter is capitalized."""
  formated_f_name = fname.title()
  formated_l_name = lname.title()
  fullname = print(f"{formated_f_name} {formated_l_name}")
  return fullname

format_name(f_name, l_name)