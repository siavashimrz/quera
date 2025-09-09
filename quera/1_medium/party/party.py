n_guests = int(input())
guests = dict({})
for i in range(n_guests):
    name = input()
    guests.update({name: 0})

for i in range(n_guests):
    name = input()
    money_people_pair = input()
    money, people = money_people_pair.split(' ')
    money, people = int(money), int(people)
    if people != 0:
        residue = money % people
        share = money // people
    else:
        residue = money
        share = 0
    guests[name] -= money
    guests[name] += residue

    for j in range(people):
        person = input()
        guests[person] += share
    # print(money,"***",people)

# print(guests)
# print("----",guests.keys())
# print("----",guests.values())

for name in guests.keys():
    print(f"{name} {guests[name]}")

