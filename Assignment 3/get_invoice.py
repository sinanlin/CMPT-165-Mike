import cgi

form=cgi.FieldStorage()

name=form.getvalue("Name")
salutation=form.getvalue("salutation")
email=form.getvalue("Email")
phone=form.getvalue("Phonenumber")
deliverydate=form.getvalue("deliverydate")
qbook1=int(form.getvalue("sam"))
qbook2=int(form.getvalue("history"))
qbook3=int(form.getvalue("manage"))

street=form.getvalue("street")
city=form.getvalue("city")
province=form.getvalue("province")
code=form.getvalue("code")

adress=street+" "+city+" "+province+" "+code






import random 
import time
from datetime import date
today = date.today()



#Calculation of the price

#For all the book, the price is $10.

def price(x):
    price=10*x*1.07
    return price

bcost1=price(qbook1)
bcost2=price(qbook2)
bcost3=price(qbook2)
totalcost=bcost1+bcost2+bcost3





#Website content: 

print "Content-type: text/html"
print



print """<!DOCTYPE html>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>


<title>Invoice</title>
<link rel="stylesheet" href="style_sheet.css" type="text/css">

    
</head>
    
<body>

<!--For the header-->
<img src="header.jpg" alt="library">"""


#<markup>

print '<div id="invoice"> <h1> Hello, '+name+', thank you for shopping!</h1>'

#1,Invoice number (Done)

print '<p>Invoice number: '+str(random.randint(1,100))+'</p>'

#2,Visitor's personal data.(Done)

print '<p>',salutation,name,'<br>',adress,'</p>'

#3,Time and datae(Done)

print '<p> Date:'+str(today)+'<p>'


#4,Produce price, individule, Total
print """<table>
<style>
    table, th, td{border: 1px solid black;
    text-align: center;}

    </style>
    <form action="get_invoice.py">
<!--First row-->
    <tr>
    <th width="200">
    Book:
    </th>
    <th width="200">
    Quantity:
    </th>
    <th width="200">
    Price:
    </th>
    </tr>
<!--Second row-->
    <tr>
        <th><img src="Sam.jpg" alt="Sam" width="50" ></br>Sam Walton </th>
        <td>
        <input type="number" size="3" name="sam" value="%s"/>
        </td>
        <td>
        %s
        </td>
      
    </tr>
<!--Third row-->  
    <tr>
    <th><img src="The_lesson.jpg" alt="The lesson of history" width="50" ></br>The lesson of histroy</th>
        <td >
        <input type="number" size="3" name="history" value="%s"/>
        </td>
        <td>
        %s
        </td>
        
    </tr>
<!--Fourth row-->
        <tr>
    <th><img src="Managing_oneself.jpg" alt="Managing oneself" width="50" ></br>Managing oneself</th>
        <td>
        <input type="number" size="3" name="manage" value="%s"/>
        </td>
        <td>
        %s
        </td>
      
    </tr>
<!--Five row-->
        <tr>
    <th height="50">Total</th>
        <td>
        %s
        </td>
        <td >
        %s
        </td>

    </tr>
    
    </table>
    <input type="submit" value="Change Quantity"/>
    <input type="hidden" name="Name" value="%s"/>
    <input type="hidden" name="salutation" value="%s"/>
    <input type="hidden" name="Email" value="%s"/>
    <input type="hidden" name="Phonenumber" value="%s"/>
    <input type="hidden" name="deliverydate" value="%s"/>
    
    <input type="hidden" name="street" value="%s"/>
    <input type="hidden" name="city" value="%s"/>
    <input type="hidden" name="province" value="%s"/>
    <input type="hidden" name="code" value="%s"/>

    </form>
"""%(qbook1,price(qbook1),qbook2,price(qbook2),qbook3,price(qbook3),(qbook1+qbook2+qbook3),price(qbook1+qbook2+qbook3),name,salutation,email,phone,deliverydate,street,city,province,code)




#5,Bonus. Change order.



#6,form that redirect custormer.

print """
    <form action="act.py">
       

        <input type="submit" name="Cancel" value="Cancel" />
        <input type="submit" name="Accept" value="Accept" />
        <input type="hidden" name="Name" value="%s"/>
        <input type="hidden" name="salutation" value="%s"/>
        <input type="hidden" name="Email" value="%s"/>
        <input type="hidden" name="Phonenumber" value="%s"/>
        <input type="hidden" name="deliverydate" value="%s"/>
    
        <input type="hidden" name="street" value="%s"/>
        <input type="hidden" name="city" value="%s"/>
        <input type="hidden" name="province" value="%s"/>
        <input type="hidden" name="code" value="%s"/>
    </form>

    </div>
    """%(name,salutation,email,phone,deliverydate,street,city,province,code)


#<markup> finished.

print """<!--Footer-->
<div id="footer">
          <p>Copyright SINAN LIN.</p>
    
    </div>
"""


print "</body></html>"



