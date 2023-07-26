from collections import UserDict
from pdb import post_mortem
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
import mysql.connector as sql
cu=""
un=""
pno=""
ps=""
em=""
cun=""
pss=""
pr="0"
ui="yooo"
d1={
   'y1':'roo',
   'mail':'roo',
   'phn':'roo'
}
dd={}
ds="LOGIN"
m2="."
m3="."
co=1
m = sql.connect(host="localhost",user="root",password="26papapapa",database="dmt")
curs=m.cursor()
# Create your views here.


def thanks1(requests):
   return render(requests,'thanks1.html')

def about(requests):
   return render(requests,'about.html')

def thanks2(requests):
   return render(requests,'thanks2.html')

def thanks(requests):
   return render(requests,'thanks.html')

def create(request):
     if request.method=="POST":
      #   username=request.POST.get('username')
      #   password=request.POST.get('password')
      #   lastname =request.POST.get('NUMBER')
      #   email =request.POST.get('email')
        
      #  #   print(username,password,)
      #   user = User.objects.create_user(username=username,email=email,last_name =lastname, password=password)
      #   user.save()
        global un,ps,em,pno
      #   m = sql.connect(host="localhost",user="root",password="26papapapa",database="dmt")
        cursor=m.cursor()

        d=request.POST
        for key,value in d.items():
           if key == "username" :
              un = value
           if key == "email" :
              em = value
           if key == "NUMBER" :
              pno = value
           if key == "password" :
              ps = value         
        cursor.execute("insert into users values('{}','{}','{}',{})".format(un,em,pno,ps))
        m.commit()
        messages.success(request,'YOUR ACCOUNT IS CREATED PLEASE LOGIN NOW')
        return render(request,'login.html')

     return render(request,'create.html')


def index(request):
   #  print(request.user)
   #  if request.user.is_anonymous:
   #   return redirect("/login")
    co=2
    return render(request, 'index.html')
    #  return HttpResponse('<h1>Page not')
 
def logi(request):
   global cun,pss,d1,ds,m2,m3,ui,co

   if request.method == "POST":
          
         #  m = sql.connect(host="localhost",user="root",password="26papapapa",database="dmt")
         #  curs=m.cursor()
          d=request.POST
          for key,value in d.items():

           if key == "email" :
              cun = value
           if key == "password" :
              pss = value         
          d = "select * from users where mail = '{}' and pass = '{}'".format(cun,pss)
          curs.execute(d)
          t = tuple(curs.fetchall())
         #  curs.execute("insert into users values ('yo','1@11','123','221')")
         #  m.commit()
          if t!=():
           dd = {
               'yo' : list(t)[0][0]
               
           }
           d1 = {
               'yo' : list(t)[0][0],
               'mail': list(t)[0][1],
               'phn': list(t)[0][2]

               
           }
           ds = list(t)[0][0]
           m2 = list(t)[0][1]
           m3 = list(t)[0][2]
           ui = ds
           return redirect("/display")
           return render(request, 'index.html',dd)
          else :
             dd = {
                'y1': "ENTER CORRECT DETAILS"
             }
             return render(request,'login.html',dd)
     
   return render(request,'login.html')
    
    
   #  return render(request, 'login.html')     
      #   t= tuple(curs.fetchall())
      #   if t!=():
      #      return render(request, 'index.html')




      #   if user is not None:
      #        # A backend authenticated the credentials
      #        print(password,12344221)
      #        login(request,user)
             
      #        return  redirect("/")
     
      #   else:
              
      #         messages.warning(request,'INVALID')
      #         return render(request, 'login.html')
         # No backend authenticated the credentials
   #   return render(request, 'login.html')


def logou(request):
    logout(request)
    messages.success(request,'YOU LOGGED OUT SUCCESSFULLY')
    return redirect("/login")

def cre(request):
   return redirect("create.html")

def pro(request):
   global d1
   d1={
      'y1':ds,
      'mail':m2,
      'phn':m3
   }
   return render(request,'profile.html',d1)







def cart(request):
   
    c = "show tables like '{}'".format(ui)
    curs.execute(c)
    f=tuple(curs.fetchall())
   
    if f!=():
          return redirect("/cartin")
          return render(request,'index.html')
    else :   
      d= "create table {} (id varchar(10),pr varchar(10)) ".format(ui)
      curs.execute(d)
      m.commit()
      # de={ 'uu': f }
      return redirect("/cartin")
      return render(request,'index.html')
    return redirect("/login")





def cartin(request):
           global cu,pr
           m = sql.connect(host="localhost",user="root",password="26papapapa",database="dmt")
           curs=m.cursor()
           
           if request.method=="POST":
               d=request.POST
               for key,value in d.items():
                if key == "tt" :
                 cu = value
                if key == "pp" :
                 pr = value
               curs.execute("insert into {} values('{}','{}')".format(ui,cu,pr))
               m.commit() 

           
           d = "select * from {}".format(ui)
           curs.execute(d)
           t = tuple(curs.fetchall())
           
           if t!=():
              
            d11 = {
               'yo' : list(t)}


            return render(request,'cart.html',d11) 
             
           else:
            return render(request,'ccart.html') 
           return render(request,'cart.html',d11) 



# def  addp(request):
#    if request.method=="POST":
#      m = sql.connect(host="localhost",user="root",password="26papapapa",database="dmt")
#      curs=m.cursor()
#      d=request.POST
#      for key,value in d.items():
#            if key == "tt" :
#               cun = value
#      curs.execute("insert into {} values('{}')".format(ui,cun))
#      m.commit()
#      return render(request,'ccart.html')           

#      return render(request,'ccart.html')           


def display(request):
   
     d = "select * from menu"
     curs.execute(d)
     t = tuple(curs.fetchall())
     d11 = {
               'yy' : list(t)}
     return render(request,'display.html',d11)

def remove(request):
              if request.method=="POST":
               d=request.POST
               for key,value in d.items():
                if key == "tt" :
                 cu = value
                if key == "pp" :
                 pr = value
               curs.execute("delete from {} where id = '{}' AND pr = '{}'".format(ui,cu,pr))
               m.commit()
              return redirect('/cart')