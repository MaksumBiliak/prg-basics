###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open("it_company.csv" , 'r') as file:
   i=0
   content=""
   for line in file:
      if job_title in line:
         content=content + str(i) +"." +line
         i+=1
print(content)