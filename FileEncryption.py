code = {'A':'!', 'B':'@', 'C':'#', 'D':'$', 'E':'%', 'F':'^', 'G':'&',
        'H':'*', 'I':'(', 'J': ')', 'K':'-', 'L':'=', 'M':'_', 'N':'+',
        'O':'`', 'P':'~', 'Q':';', 'R':':', 'S':"'", 'T':'"', 'U':'[',
        'V':'{', 'W':']', 'X':'}', 'Y':'|', 'Z':',', 'a':"<", 'b':'.',
        'c':'>', 'd':'/', 'e':'?', 'f': '1', 'g':'2', 'h':'3', 'i':'4',
        'j':'5', 'k':'6', 'l':'7', 'm':'8', 'n':'á', 'o':'é', 'p':'í',
        'q':'ó', 'r':'ú', 's':'ý', 't':'ñ', 'u':'â', 'v':'ê', 'w':'î',
        'x':'ô', 'y':'û', 'z':'æ'}

infile = open('info_security.txt','r')
infile_read = infile.read()
outfile = open('encrypted.txt','w')

for i in infile_read:
        if i in code:
                outfile.write(code[i])
        else:
                outfile.write(i)

outfile.close()

readfile = open('encrypted.txt','r')
file_read = readfile.read()

for i in file_read:
        if not i in code.values() or i == '.' or i == ' ':
                print(i, end='')
        else:
                for x, y in code.items():
                        if i==y:
                                print(x, end='')
