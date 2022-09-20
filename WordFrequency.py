with open('sometext.txt','r') as infile:
    text = infile.read().rstrip()

#print(text)

text_list = text.split()
#print(text_list)

#occurences = {item: text_list.count(item) for item in text_list}
#print(occurences)

for i in text_list:
    print(i, ' - ', text_list.count(i))