import time
while True:
    f = open("result.txt", 'r')
    f1 = open('to_do.txt', 'w')
    mas = []
    for line in f:
        mas.append(line.split(" "))
    id_chat = []
    for i in range(len(mas)):
        if mas[i][0] not in id_chat:
            id_chat.append(mas[i][0])
    result = []
    for i in range(len(id_chat)):
        for j in range(len(mas)):
           if id_chat[i] == mas[j][0]:
               if len(mas[j]) == 3:
                  phone = mas[j][2]
               else:
                  name = mas[j][2]
                  last_name = mas[j][3]
                  text = []
                  for k in range(4, len(mas[j])):
                      text.append(mas[j][k])
        a = [id_chat[i], phone, name, last_name, text]
        result.append(a)
    for i in range(len(result)):
       s = ''
       for j in range(len(result[i][4])):
           s += result[i][4][j] + " "
       f1.write(str(result[i][1][0:len(result[i][1])-1]) + " " + str(result[i][2]) + " " + str(result[i][3]) + " " + str(s) + "\n")
    f1.close()
    f.close()
    time.sleep(60)