import cgi

form=cgi.FieldStorage()
type=[form.getvalue("Cancel"),form.getvalue("Accept")]

name=form.getvalue("Name")
salutation=form.getvalue("salutation")
email=form.getvalue("Email")
phone=form.getvalue("Phonenumber")
deliverydate=form.getvalue("deliverydate")

street=form.getvalue("street")
city=form.getvalue("city")
province=form.getvalue("province")
code=form.getvalue("code")

adress=street+" "+city+" "+province+" "+code



#Website content: (Done)

print "Content-type: text/html"
print



print """<!DOCTYPE html>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>


<title>Thanks</title>

    
</head>
    
<body>

<!--For the header-->
<img src="header.jpg" alt="library">"""


#<markup>

if type[0]=="Cancel":
    print '<p>Thanks for visiting our website! You might not find the book that you want. We will be providing more book in the future!<p>'

else:
    print """<p>Thank you %s %s for your purchase today.
    Your invoice has been emailed to %s and
    your requested products will be mailed to the following
    location:</p> <p> %s </p> <p> You expected deliver day would be:</p> <p> %s </p>"""%(salutation,name,email,adress,deliverydate)
    
print "</body></html>"


#<markup> finished

print """<!--Footer-->
<style>
div#footer {
clear : both;
margin-top : 19em;
text-align: center;
background-color: black;
padding: 1.5em;
    
}
#footer{
    font-family: cursive;
    color: white;
    text-align: center;
}
</style>
<div id="footer">
          <p>Copyright SINAN LIN.</p>
    
    </div>
"""
print "</body></html>"
