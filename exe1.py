expense = [2200,2350,2600,2130,2190]

#In Feb, how many dollars you spent extra compare to January?
extraExp = expense[1]- expense[0]
print(extraExp)

#Find out your total expense in first quarter (first three months) of the year.
quatExp= 0
for i in range(len(expense)):
    if i > 2:
        break
    else:
        quatExp = quatExp+ expense[i]
print(quatExp)

#Find out if you spent exactly 2000 dollars in any month
flag = 0
for i in expense:
    if i == 2000:
        print("Expense exact 2000 found")
    else:
        print("No match found")   

#abobe problem in one line:
a = 2000 in expense
print(a)

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list    
expense.append(1980)
print(expense)

'''You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

expense[3] = 1930
print(expense)

heros=['spider man','thor','hulk','iron man','captain america']

#Length of the list
print(heros)
length = len(heros)
print("length of the list is:", length)

#Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

'''You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'''

heros.remove(('black panther'))
print(heros)
heros.insert(3,'black panther')
print(heros)

'''Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.'''
#heros[1:3] = ["doctor strange"]
#print(heros)

#above problem with loop
dup = ''
for i in range(len(heros)):
    if heros[i] == "thor" or heros[i] == "hulk":
        heros[i] = "doctor strange"
print(heros)
for i in range(len(heros)):
    for j in range(i+1,len(heros)):
        if heros[j] == heros[i]:
            print(heros[j],"- to be remove")
            dup = heros[j]
heros.remove(dup)
print(heros)

#Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)


#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function.

print("Enter the Max number:")
max = int(input()) 
odds = []

for i in range(0,max+1):
    #print(i)
    if i % 2 != 0:
        odds.append(i) 
print(odds)

