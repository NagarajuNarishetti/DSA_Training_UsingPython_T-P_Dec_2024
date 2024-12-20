''''
# 1.single level
class WhatsApp1:
    def text(self):
        print("Texting")
    def audiocall(self):
        print("Audio call")

class WhatsApp2(WhatsApp1):

    def payment(self):
        print("Payment")
    def videocall(self):
        print("VideoCall")
    def community(self):
        print("community")

w1=WhatsApp1()
w1.text()
# w1.payment Gives error bcoz  w1 is parent object and payment is method in child class
w2=WhatsApp2()
w2.payment() '''


'''
# 2.multilevel

class WhatsApp1:
    def text(self):
        print("Texting")
    def audiocall(self):
        print("Audio call")

class WhatsApp2(WhatsApp1):

    def payment(self):
        print("Payment")
    def videocall(self):
        print("VideoCall")
    def community(self):
        print("community")

class WhatsApp3(WhatsApp2):
    def viewOnce(self):
        print("View Once")
    def hdQuality(self):
        print("HD Quality")

w3= WhatsApp3()
w3.text()
w3.payment()
w3.viewOnce()  '''

'''
# 3.Multiple Inheritance

class WhatsApp1:
    def text(self):
        print("Texting")
    def audiocall(self):
        print("Audio call")

class WhatsApp2():

    def payment(self):
        print("Payment")
    def videocall(self):
        print("VideoCall")
    def community(self):
        print("community")

class WhatsApp3(WhatsApp1,WhatsApp2):
    def viewOnce(self):
        print("View Once")
    def hdQuality(self):
        print("HD Quality")

w3= WhatsApp3()
w3.text()
w3.payment()
w3.viewOnce()  '''

# 4.Heirachicel
class WhatsApp1:
    def text(self):
        print("Texting")
    def audiocall(self):
        print("Audio call")

class WhatsApp2(WhatsApp1):

    def payment(self):
        print("Payment")
    def videocall(self):
        print("VideoCall")
    def community(self):
        print("community")

w1=WhatsApp1()
w1.text()
# w1.payment Gives error bcoz  w1 is parent object and payment is method in child class
w2=WhatsApp2()
w2.payment() 