
#Imaginary data
name="mike"
salutation="Mr."
adress="9380 university"
email="sinanl@sfu.ca"
phone="6047254251"
deliverydate="2015.8.05"
qbook1=1
qbook2=2
qbook3=3
css="mike.css"

#Calculation of the price

#For all the book, the price is $10.

def price(x):
    price=10*x*1.07
    return price

bcost1=price(qbook1)
bcost2=price(qbook2)
bcost3=price(qbook2)
totalcost=bcost1+bcost2+bcost3


print """<table>
<style>
    table, th, td{border: 1px solid black;
    text-align: center;}

    </style>
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
        %s
        </td>
        <td>
        %s
        </td>
      
    </tr>
<!--Third row-->  
    <tr>
    <th><img src="The_lesson.jpg" alt="Sam" width="50" ></br>The lesson of histroy</th>
        <td >
        %s
        </td>
        <td>
        %s
        </td>
        
    </tr>
<!--Fourth row-->
        <tr>
    <th><img src="Managing_oneself.jpg" alt="Sam" width="50" ></br>Managing oneself</th>
        <td>
        %s
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
"""%(qbook1,price(qbook1),qbook2,price(qbook2),qbook3,price(qbook3),(qbook1+qbook2+qbook3),price(qbook1+qbook2+qbook3))
