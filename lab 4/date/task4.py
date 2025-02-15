from datetime import datetime  
 
date1_str = input("Enter first date: YYYY-mm-dd hh:mm:ss : ")  
date2_str = input("Enter second date: YYYY-mm-dd hh:mm:ss : ")  

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")  
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")  

difference = abs((date1 - date2).total_seconds())

print(difference)  
