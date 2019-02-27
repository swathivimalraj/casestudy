import mysql.connector as m
import webbrowser
import HTML
class mod3:
    def tables_html(self,r,monthname,i):
        #print(list(res))
        #table_data = res
        #for k in monthname:
        htmlcode="<b>"+monthname[i]+"</b>"
        htmlcode+= HTML.table(r)
        print htmlcode
        return htmlcode
