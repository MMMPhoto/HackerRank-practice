string = 'ABCDCDC'
sub_string = 'CDC'
count = 0        
index = string.find(sub_string)
while (index >= 0):
    count +=1
    index += 1
    string = string[index:]
    index = string.find(sub_string)
print(count)
