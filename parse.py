def parse(filename):
   final = ""
   with open(filename, "r") as myfile:
       for the_line in myfile:
           if str(the_line).strip() == "(":
               final += "("
           else:
               final += str(the_line).strip() + ","
   return eval(final)