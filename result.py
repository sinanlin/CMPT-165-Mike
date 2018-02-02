import cgi

form=cgi.FieldStorage()


name=form.getvalue("Name")
birthyear=int(form.getvalue("Birth year"))
gender=form.getvalue("salutation")
area=[form.getvalue("BIO"),form.getvalue("BUS"),form.getvalue("CHEM"),form.getvalue("CMPT"),form.getvalue("CRIM"),form.getvalue("FPA"),form.getvalue("PHY"),form.getvalue("OTHER")]
age=2015-birthyear

   

print "Content-type: text/html"
print


print """<!DOCTYPE html>
<html>
<head>
<title>Simple Web Script</title>
</head>
<body>"""



#<markup>

print "<h1> Hello "+name+" thank you for visiting my website! </h1>"


#Displine 
if  area[3] == "on":
    
    print '<p> Seems like we are in the same faculty; would be nice if we could meet one day!. </p>'

else:
    print '<p> Seems like you are from a different program;  no wonder why we have never met! </p>'


#Gender and age
    

if age>=18 and age<=30 and gender=="Mr.":
    
    print"<p> Please visit again and hope we can keep in touch. </p>"

else:
    print"<p> Have a pleasant day! </p>"

#<markup> finished.


print """</body></html>"""

