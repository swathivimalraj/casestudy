import mysql.connector as m
import webbrowser
import HTML
def connection():
    db = m.connect(host="localhost",user="root",password="root",db="casestudy",port="3306" )
    cursor = db.cursor(buffered=True)
    f = open('query.sql',"r");
    fil=f.read()
    sqlcommands=fil.split(';');
    #print (sqlcommands)
    for line in sqlcommands:
        try:
            cursor.execute(line)
            head=[i[0] for i in cursor.description]
            res=cursor.fetchall()
            for  r in cursor:
                try:
                    print (r)
                except:
                    print("Exception Thrown")
            res.insert(0,head)
            return res
        except:
            print("Exception Thrown")
 
    db.close()
#print(connection())
def htmlconnection(message):
    f = open('hi.html','w')
    f.write(message)
    f = open('hi.html','r')
    f.read()
    webbrowser.open_new_tab('hi.html')
    f.close()
#print(htmlconnection())

def tables_html():
    r=connection()
    #print(list(res))
    #table_data = res
    htmlcode = HTML.table(r)
    print htmlcode
    htmlconnection(htmlcode)
    
tables_html() 
