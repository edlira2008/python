print("hello world")
 #loops / ciklet ose unaza


for nr in range(100):
     print(nr)
#numron prej 0 deri 9 per shkak te index totaj jane se 0-100/ 100 nr

print("----"*4)
for i in range(1,11):
      print(i) #dmth gjith -1 i bjen/numron prej nr te pare deri tek nr i dyt -1



#steps i tregon psh ka sa numra podon mi kalu psh dmth hap mi kap

for i in range (0,10,3):
    print(i)
    #0,3,6,9

print("-----"*3)

seasons=['spring','summer','autumn', 'winter','spring',
         'summer','autumn', 'winter','spring','summer',
         'autumn', 'winter','spring','summer','autumn', 'winter']

#for season in seasons:
#print(season) #iterastion over a list


#dyjat mujna mi bo ose qita nalt ose qita posht saj


for i in range(0,len(seasons),5):
    print(seasons[i])
    #ja nis numron prej 0, sa elemnete ika lista me nga 5 hapa tui  kalu



word='comupter works for us'
for c in word:
     print(c)
 #interon fjal per fjale
for c in word:
    if c.isalpha():
     print(c)

     #tregon a jon krejt 'c' shkronjaa a edhe tjera elemente perveq string


logs=['executed', 'execited','execited','error', 'execited','execited','execited']
for log in logs:
     if log =='error':
         break
     else:
         print(log)

for log in logs:
     if log =='error':
         continue
     else:
         print(log)
   #dmth nderpren ciklin ose loop ne mometin kur haset ni error me break
   #kurse me continue e sheh errorin po e vazhdon prap listen po pa  e paraqit errorin

 #key word per functions  sht DEF


