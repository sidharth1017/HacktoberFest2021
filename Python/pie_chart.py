#import the packages
import matplotlib.pyplot as plt
#ask the user for the partitions
print("Enter your titles of your partitions here")
Partition = input('>'), input(''), input(''), input('')
#input the sizes
print("print the size of each partition respectively")
sizes = [input(">"), input(">"), input(">"), input(">")]
#make the pichart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=Partition, autopct='%1.1f%%', shadow=True, startangle=90)         
ax1.axis('equal')
plt.show()