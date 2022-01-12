#while and for loops
#while loops
# x=0
# while (x<=5):
#   print(x)
#   x=x+1

  #for loops

# for x in range(4,11):
#       print(x)

#array
days=[" Monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for d in days:
    #if (d=="thursday"):break  #loop stops
    if (d=="friday"):continue  #skip d
    print(d)