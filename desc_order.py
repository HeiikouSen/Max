string = ["Max", "Juli","Alex", "Mira", "Nastay", "Sergo"]

def sotrOrder(string):
    string.sort(key=len)
    print(string)
    string.sort(reverse=True, key=len)
    return string
print(sotrOrder(string))
