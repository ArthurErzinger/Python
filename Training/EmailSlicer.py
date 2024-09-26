txt = input("Write you email here: ")

sliced = txt.split("@")

name = sliced[0]

print("Username: " + name)

domain = sliced[1]

print("Domain: " + domain)