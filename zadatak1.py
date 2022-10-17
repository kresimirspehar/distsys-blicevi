lista1 = ["Stol", "Stolica", "Krevet", "Fotelja"]

def provjeri(x):
    assert isinstance(x,list) and all([isinstance(i, str)for i in x])
    return {(i):(x[::-1]) for i,x in enumerate(x)}

print(provjeri(lista1))
