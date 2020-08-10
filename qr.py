from MyQR import myqr  
import random
import string
def qr(line):
    line = line.strip('\n')
    name = line + ".jpg"
    name = name.replace('/','-')
    myqr.run(words=str(line),save_name=name)
    print("生成："+name+"\n")
def creat():
    sen = ''
    list = random.sample('QWERTYUIOPLKJHGFDSAZXCVBNM1234567890',random.randint(17,18)) 
    for x in range(len(list)-1):
        sen += list[x]
        sens = 'P.URL.CN/' + sen
    return sens
while True:
    qr(creat())