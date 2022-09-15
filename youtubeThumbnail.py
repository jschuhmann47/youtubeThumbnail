import webbrowser

url=input("Enter URL: (0 to exit) ")
while(True):
    if url=='0':
        break
    if "https://www.youtube.com/watch?v=" in url:
        id=url[32:43]
        break
    if "http://www.youtube.com/watch?v=" in url:
        id=url[31:42]
        break
    url=input("Invalid URL, enter a new one: (0 to exit) ")
if url!='0':
    print("ID: " + id)
    img="http://i3.ytimg.com/vi/"+id+"/maxresdefault.jpg"
    webbrowser.open(img)
