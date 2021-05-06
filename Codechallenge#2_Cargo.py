#Here is a solution to the Code Challenge#2

print ("Identifying Incoming Cargo Services")

alist = ["International", "Domestic", "Over the Road", "LTL", "Reefers"]

if "International" in alist:
    print("True")

for elem in alist:
    if "Int" in elem:
        print(elem)

#Here is our function

def Test_If_Substring(a, b):
    a1 = str(a)
    b1 = str(b)
    if a1 in b1:
        rstr = "True"
    if a1 not in b1:
        rstr = "False"
    return rstr

#Let's take an input
bstr = input("Please enter desired Cargo Service")
#And we will call the function
ans = Test_If_Substring(bstr, astr)
print("Please enter cargo value", ans)