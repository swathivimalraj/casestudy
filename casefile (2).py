import mysql.connector as m
import webbrowser
def connection():
    db = m.connect(host="localhost",user="root",password="root",db="casestudy",port="3306" )
    cursor = db.cursor(buffered=True)
    f = open ('quries.sql',"r");
    fil=f.read()
    sqlcommands=fil.split(';');
    #print (sqlcommands)
    for line in sqlcommands:
            cursor.execute(line);
            for  r in cursor:
                    print (r)
        #cursor.execute(fil)
        #res=cursor.fetchone()
    #print res
    db.close()
print(connection())
def htmlconnection():
    f = open('helloworld.html','r')
    f.read()
    f.close()

    webbrowser.open_new_tab('helloworld.html')
print(htmlconnection())
