import mysql.connector as m
import webbrowser
import HTML
import module2 as mm
import module3 as m3
import module4 as m4

monthname=[
    'JAN',
    'FEB',
    'MAR',
    'APR',
    'MAY',
    'JUN',
    'JUY',
    'AUG',
    'SEP',
    'OCT',
    'NOV',
    'DEC',
    ]
li={
    "JAN":"'%-01-%'",
    "FEB":"'%-02-%'",
    "MAR":"'%-03-%'",
    "APR":"'%-04-%'",
    "MAY":"'%-05-%'",
    "JUN":"'%-06-%'",
    "JUY":"'%-07-%'",
    "AUG":"'%-08-%'",
    "SEP":"'%-09-%'",
    "OCT":"'%-10-%'",
    "NOV":"'%-11-%'",
    "DEC":"'%-12-%'",
    }
if __name__ == "__main__":
     o4=m4.mod4()
     o3=m3.mod3()
     o2=mm.mod2()
     output=[]
     for i in monthname:
          output.append(o2.connection(i))
     print output
     html_code=''
     count=-1
     for j in output:
         count=count+1
         print count
         html_code+=o3.tables_html(j,monthname,count)
     o4.htmlconnection(html_code)

