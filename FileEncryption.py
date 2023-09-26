codes = { 'A' : '%', 'a' : '9', 
         'B' : '@', 'b' : '#',
         'C' : '-', 'c' : '!',
         'D' : '[', 'd' : ';',
         'E' : '2', 'e' : '3'
        #finish this dict
         
         
         
         }


security_txt = open('info_security.txt', 'r')

txt_file = security_txt.read()

outfile = open('encrypted.txt', 'w')

for line in txt_file.split():
    for letter in txt_file:
        outfile.write(codes[letter])

outfile.close()