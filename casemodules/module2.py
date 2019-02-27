import mysql.connector
from module1 import li
class mod2:
    def connection(self,monthname):
        db = mysql.connector.connect(host="localhost",user="root",password="root",db="casestudy",port="3306" )
        cursor = db.cursor()
        q='select m_id,s_id,s_name,exam_date AS EXAM_DATE,french AS FRENCH,english AS ENGLISH,maths as MATHS,science AS SCIENCE,social AS SOCIAL,total AS TOTAL,Result,if(Result="PASS",rank() over (partition by Result_set.result order by Result_set.total desc),"-") AS RANK_student from(SELECT m.m_id,s.s_id,s.s_name,m.exam_date,m.maths ,m.english ,m.science  ,m.social ,m.french ,IF(m.maths>=50 and m.english>=50 and m.science>=50 and m.french>=50 and m.social>=50, "PASS","FAIL") as Result,(m.maths + m.english + m.science +m.social +m.french) AS Total FROM student_table s join mark_table m on m.s_id=s.s_id where m.exam_date like '+str(li[monthname])+')as Result_set;'
        cursor.execute(q)
        head=[i[0] for i in cursor.description]
        try:
            res=cursor.fetchall()
        except Exception as exc:
            print(exc)
        res.insert(0,head)
        return res
        db.close()
    #print(connection())
