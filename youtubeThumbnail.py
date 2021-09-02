import webbrowser

url=input("Enter URL: ")
flag=False
while(not flag):
    if "https://www.youtube.com/watch?v=" in url:
        id=url[32:43]
        flag=True
    elif "http://www.youtube.com/watch?v=" in url:
        id=url[31:42]
        flag=True
    else:
        url=input("Not a valid URL, enter a new one: ")
print("ID: " + id)
urlnueva="http://i3.ytimg.com/vi/"+id+"/maxresdefault.jpg"
webbrowser.open(urlnueva)
