import csv

rows = []

with open("summer.csv", 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print("Please enter numbers 1,2,3,4 or 5 for the following questions:\n1. Who won _____ (Bronze/Gold) in the year ______? \n2. How many prizes were awarded for _______(Country) in the year ________?\n3. Where was it held in the year __________?\n4. How many prizes did __________(Country) get? When, where?\n5. Who won women’s ________ in _______?\n")
question = int(input())
attributes = []

count = 0

if question == 1:
    print("Enter the type of medal(Bronze/Gold/Silver) and the year\n")
    attributes = input().split(' ')
    flag=1
    atheletes=[]
    if len(attributes) == 2:
        for x in rows:
            if x[0] == attributes[1] and x[-1] == attributes[0]:
                atheletes.append(x[4])
                flag=0
        if flag:
            print("Enter appropriate data")
        else:
            print(f"The atheletes who won {attributes[0]} in {attributes[1] } are \n{list(set(atheletes))}")
            print(len(list(set(atheletes))))
    else:
        print("Enter appropriate data")


elif question == 2:
    print("Enter the name of the country and the year\n")
    attributes = input().split(' ')
    flag = 1
    if len(attributes) == 2:
        for x in rows:
            if x[0] == attributes[1] and x[5].lower() == attributes[0].lower()[:3]:
                count += 1
                flag=0
        if flag:
            print("No data for this year, Please enter the right country or year")
        else:
            print(count)
    else:
        print("Enter appropriate data")

elif question == 3:
    print("Enter the year you wish to know where it held in\n")
    attributes = input().split(' ')
    flag =1
    for x in rows:
        if x[0] == attributes[0]:
            print(x[1])
            flag=0
            break
    if flag:
        print("No data for this year, Please enter the right year")



elif question == 4:
    print("Enter the name of the country\n")
    attributes = input().lower()
    when = []
    lookup_1 = {}
    flag=1
    for x in rows:
        if x[5].lower() == attributes[:3]:
            lookup_1[x[0]] = x[1]
            when.append(x[0])
            flag=0
    if flag==0:
        count = 0
        lookup_2 = {}
        for i in when:
            count = when.count(i)
            lookup_2[i] = count

        when = list(set(when))
        for i in when:
            print(
                f"The country {attributes[:3].upper()} won {lookup_2[i]} prizes in the city {lookup_1[i]} which was held in the year {i} ")
    else:
        print("Enter a valid country name")

elif question == 5:
    flag = 1
    print("Enter the sport's discipline and the year\n")
    attributes = input().split(' ')
    if len(attributes) == 2:
        for x in rows:
            if x[3].lower() == attributes[0].lower() and x[0] == attributes[1] and x[-3] == 'Women':
                print(x[4])
                flag=0
    else:
        print("Enter appropriate data")

    if flag and len(attributes) == 2:
        print(f'No women won any medals for {attributes[0]} in the year {attributes[1]} or the entered data is incorrect')


else:
    print("Please enter a numbers from 1-5")


