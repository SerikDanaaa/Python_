import re 
txt = input()
pattern = re.search(r'^(pp2|PP2)[(a-zA-Z)|\s]+(midterm|MIDTERM)$', txt)
if pattern:
    print("YES")  
else:
    print("NO") 