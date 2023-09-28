codes = {
        'A' : '%', 'a' : '9', 
         'B' : '@', 'b' : '#',
         'C' : '-', 'c' : '!',
         'D' : '[', 'd' : ';',
         'E' : '2', 'e' : '3',
         'F' : '{', 'f' : '~',
         'G' : '`', 'g' : '$',
         'H' : 'n', 'h' : 'M',
         'I' : '|', 'i' : '+',
         'J' : '=', 'j' : '8',
         'K' : '^', 'k' : '(',
         'L' : '&', 'l' : ')',
         'M' : '_', 'm' : '4',
         'N' : '7', 'n' : ':',
         'O' : '.', 'o' : '<',
         'P' : '>', 'p' : '?',
         'Q' : '"', 'q' : '/',
         'R' : '5', 'r' : '6',
         'S' : 'p', 's' : 'l',
         'T' : 'u', 't' : 'R',
         'U' : 'W', 'u' : 'F',
         'V' : 'a', 'v' : 'b',
         'W' : 'q', 'w' : 'g',
         'X' : 'z', 'x' : 'S',
         'Y' : 'h', 'y' : 'd',
         'Z' : ',', 'z' : 'c',
         ' ' : ' ', '.' : ']',
         ':' : 'e'
         }


security_txt = open('info_security.txt', 'r')

txt_file = security_txt.read()

outfile = open('encrypted.txt', 'w')

for word in txt_file.split():
    for letter in txt_file:
        outfile.write(codes[letter])

outfile.close()