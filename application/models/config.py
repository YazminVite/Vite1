import web

db_host = '	l9dwvv6j64hlhpul.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'qju6nyyzi9ss6ksu'
db_user = 'w2llgsiqdbnsqzpz'
db_pw = 'p38zizijujan7jb0'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
