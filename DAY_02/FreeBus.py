'''
passanger is female 
carry address proof
from ts free
form andra 50 %
nithrer ap nor ts 10 %

'''
g=input("Enter Gender : ").lower()
proof=(input("Enter True or False : ")).lower()=='true'

'''
Using bool(input("Enter True or False : ")) would not work as expected if you're trying to interpret "True" or "False" as boolean values. The bool() function simply converts any non-empty string to True and an empty string to False. So if you enter "True" or "False", it will return True for both, because both are non-empty strings.

Here's how bool(input()) works:

If the input is any non-empty string (e.g., "True", "False", "Hello"), bool() will return True.
If the input is an empty string (""), bool() will return False.
'''
state =input("Enter State : ").upper()

if(g=="female"):
    if proof and state=="TS":
        print("Free\n")
    elif proof and state=="AP" :
        print("50 Free\n")
    elif proof :
        print("10 Free")
    else :
        print(" Please Carry Proof\n")
else :
    print("sorry Free is only for Female")



