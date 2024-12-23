# class MyClass1:
#     name=''

# c=MyClass1()
# c.name='Ram'
# print(c.name)

class Netflix:
    lang='English'
    watch={}
    def __init__(self,title,genre,year):
        self.title=title
        self.genre=genre
        self.year=year
N=Netflix('Pushpa 2',"Adventure",2024)
print(N.title)
print(N.genre)
print(N.lang)
print(N.year)
N2=Netflix('Animal','Violence',2023)
print()
print(N2.title)
print(N2.genre)
print(N2.lang)
print(N2.year)
