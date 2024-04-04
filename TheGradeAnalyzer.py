#Test Average and Grade

#Enter 5 test scores
test1 = int(input('Enter score 1: '))
test2 = int(input('Enter score 2: '))
test3 = int(input('Enter score 3: '))
test4 = int(input('Enter score 4: '))
test5 = int(input('Enter score 5: '))

total = [test1, test2, test3, test4, test5]
total.sort()

def average (total):
    return sum(total)/len(total)

def highest (total):
    ia = total[-1]
    return ia

def lowest (total):
    ib = total[0]
    return ib

def determine_score(grade):

    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'


avg = average(total)
abc_grade = determine_score(avg)
high = highest(total)
low = lowest(total)

print("That's a(n): " + str(abc_grade))
print('Average grade is: ' + str(avg))
print("the highest grade is: " + str(high))
print("the lowest grade is: " +str(low))