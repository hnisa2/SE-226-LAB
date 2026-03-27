users={}
unique_items=set()
num_users = int(input("Enter number of users: "))

for _ in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))
    items = []
    for i in range(1, num_items + 1):
        item = input(f"Item {i}: ")
        items.append(item)
        unique_items.add(item)
    users[username] = items

print("USER DATA:")
for user, items in users.items():
    print(f"{user} -> {items}")

item_count={}
ordered_items=[]

for items in users.values():
    seen=set()
    for item in items:
        if item not in seen:
            seen.add(item)
            if item not in item_count:
                item_count[item] = 1
                ordered_items.append(item)
            else:
                item_count[item] += 1

print("COMMON ITEMS:")
for item in ordered_items:
    if item_count[item]>1:
        print(item)

print("UNIQUE ITEMS:")
for item in ordered_items:
    if item_count[item]==1:
        print(item)

print("MOST POPULAR ITEM:")
if item_count:
    max_count=max(item_count.values())
    for item in ordered_items:
        if item_count[item]==max_count:
            print(item)