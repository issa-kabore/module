import re

"""
[]	A set of characters	"[a-m]"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or

\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper cas
"""


def get_words(string):
    regex = r"\b(\w+)\b"
    return re.findall(regex, string)


def words_with_n_chars(string, n):
    if n <= 0: return []
    regex = r"\b(\w{" + str(n) + r"})\b"
    return re.findall(regex, string)


def check_phone_number(tel):
    regex = r"0{1}[1-7]{1}(-[0-9]{2}){4}"
    return re.search(regex, tel)


def check_mail(email):
    regex = r".+@(\w+)\.[a-z]+"
    # regex = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
    return re.search(regex, email)
