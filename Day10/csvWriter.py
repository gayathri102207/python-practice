import  csv
with open("Day10/StudentData.csv",'w') as data:
    writer=csv.writer(data)
    writer.writerow(["s.no","Name","Dept"])
    writer.writerow(["16","Gayathri","AI&DS"])
    writer.writerow(["31","Pratheksha","AI&DS"])