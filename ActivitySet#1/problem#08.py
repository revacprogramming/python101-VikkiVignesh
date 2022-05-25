# Files
"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
filename=input("Enter a filename :")
fhandle=open(filename)
count=0
total=0
for line in fhandle:
  if line.startswith("X-DSPAM-Confidence:"):
     s=line.split()
     v=float(s[1])
     count+=1
     total+=v
print("count",count,"Total",total)
average=total/count
print("Average:",average)
   
