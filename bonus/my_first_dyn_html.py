print "Content-type: text/html"
print

print'<head>\
<title>My first web script</title>\
<style>\
tr{background-color:rgb(140,223,140);\
border:solid white;\
  }\
td{font-weight:bold;\
   font-family:fantasy;\
   padding:1em;\
	}\
</style>\
</head>\
\
<body>\
<h1>The first web script of Albert</h1>\
<p>This is a dynamically generated web page.</p>\
<table>\
<tr>\
<td style="text-align:center;">Coffee</td>\
<td style="text-align:center;">Amount of milk to<br>make 1 cup (236 ml)</td>\
</tr>\
<tr>\
<td>Espresso</td>\
<td>0 ml</td>\
</tr>\
<tr>\
<td>Latte</td>\
<td rowspan="2">100ml</td>\
</tr>\
<tr>\
<td>Cappuccino</td>\
</tr>\
<tr>\
<td>Americano</td>\
<td rowspan="2">30ml</td>\
</tr>\
<tr>\
<td>Macchiatto</td>\
</tr>\
</table>\
</body>\
</html>'
