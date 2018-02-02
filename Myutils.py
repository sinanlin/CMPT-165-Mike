
def get_strandard_html(title,css,version,markup):


    #Assign value to title
    if(title==""):
        title="Dynamic generated webpage";

    #Header
    if(version >=5):
        z="<!DOCTYPE html> <html>"
    else:
        z='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
    

    if(css!=""):
        y="""<head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>"""+title+"""</title> <link rel="stylesheet" href="%s" type="text/css"> </head><body> """%css

    else:
        y="""<head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>"""+title+"""</title> </head> <body>"""


    #Fill in Markup

    #Close
    
    c="""</body></html>"""
    return z+y+markup+c



