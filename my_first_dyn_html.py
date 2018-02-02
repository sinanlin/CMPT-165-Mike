Python 2.7.6 (v2.7.6:3a1db0d2747e, Nov 10 2013, 00:42:54) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print "Content-type: text/html"
print

print'<head> <title>My first web script</title>\
<style> tr{background-color:rgb(140,223,140);\
border:solid white;  } td{font-weight:bold;\
   font-family:fantasy;  padding:1em; </style>\
</head>\
\ <body>\
<h1>The first web script of Albert</h1>\
<p>This is a dynamically generated web page.</p>\
<table>\ <tr>\
<td style="text-align:center;">Coffee</td>\
<td style="text-align:center;">Amount of milk to<br>make 1 cup (236 ml)</td>\
</tr>\<tr>\
<td>Espresso</td>\
<td>0 ml</td>\</tr>\
<tr>\<td>Latte</td>\
<td rowspan="2">100ml</td>\
</tr>\
<tr>\<td>Cappuccino</td>\
</tr>\<tr>\
<td>Americano</td>\
<td rowspan="2">30ml</td>\
</tr>\<tr>\
<td>Macchiatto</td>\
</tr>\</table>\</body>\</html>'
