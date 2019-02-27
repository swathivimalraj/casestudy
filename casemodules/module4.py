import mysql.connector as m
import webbrowser
import HTML
class mod4:
    def htmlconnection(self,message):
        try:
            with open('hi.html','w') as f:
               f.write(message)
        except IOError:
            print "Could not write into the file:", f
        try:
            with open('hi.html','r') as f:
               f.read()
               webbrowser.open_new_tab('hi.html')
        except IOError:
            print "Could not read the file:", f      
          

