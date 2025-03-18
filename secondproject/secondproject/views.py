from django.shortcuts import HttpResponse

data=f"<hr><a href='/'>Home</a>\t<a href='/signup'</a>\t<a href='signin'>SignIn</a>"


def index(req):
    data=f"<hr><a href='/'>Home</a>  <a href='signup'> SignUp </a>\t<a href='signin'> SignIn </a>"
    return HttpResponse(f"<center><h1>Welcome to my page!{data}</h1></center>")

def signup(req):
    global username
    username = input("enter username=")
    return HttpResponse(f"<center><h1>SignUp Page{data}</h1></center>")
    
def signin(req):
    chkusername=input("enter username to signin=")
    if chkusername==username:
       next = f"<hr><h1><a href='/'>Logout</a>"
       return HttpResponse(f"<center><h1>Welcome {chkusername}!!!{next}</h1></center>")
    else:
        msg = f"<center><h1>Incorrect username!!! try again</h1></center>"
        next = f"<hr><h1><a href='/'>Click here to go back</a>"
        return HttpResponse(f"{msg}{next}")