import webbrowser

url=input("Ingresar URL: ")
id=url[32:43]
print("ID: " + id)
urlnueva="http://i3.ytimg.com/vi/"+id+"/maxresdefault.jpg"
webbrowser.open(urlnueva)
