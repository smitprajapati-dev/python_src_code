# These are some word we have to put when we want to find the character is available in string
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group

import re




x = "My name is Smit Prajapati, and I'm Software Engineer"

y = re.search("^My Smit", x)
if y:
    print("Yes we have match ")
else:
    print("No, we don't have any match")