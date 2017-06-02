import os, time, re, random

dir_equip = "C:\Users\devin\Desktop\Books\Pathfinder\PFLootTable\Master_Equipment_file.txt"
dir_item = "C:\Users\devin\Desktop\Books\Pathfinder\PFLootTable\Master_Item_file.txt"
dir_master = "C:\Users\devin\Desktop\Books\Pathfinder\PFLootTable\MasterList.txt"
items = []
equip = []

pp = 'pp'
gp = 'gp'
sp = 'sp'
cp = 'cp'

exp_cost = 0
picked_items = []
item_ammount = 0

def intro():
    print('Items given?')
    item_ammount = input()
    print('(1) Equipment,\n(2) Items,\n(3) Both?')
    fileType = input()
    print('Exp?')
    exp = input()
    if int(fileType) == 1:
        dir_item = dir_equip
        print('Using equip list;')
    if int(fileType) == 2:
        print('Using item list;')
    if int(fileType) == 3:
        dir_item = dir_master
        print('Using master list;')
    findGP()
    pickItems(exp, item_ammount)
    intro()

def pickItems(exp, item_ammount):
    print(item_ammount)
    while (item_ammount > 0):
        item = random.choice(items)
        exp_cost = int(item[1])
        if exp >= 0:
            #print(item[1])
            #print(exp)
            if int(item[1]) <= int(exp):
                picked_items.append(item)
                exp = int(exp) - int(exp_cost)
                item_ammount = item_ammount - 1
                print(item)
            if int(item[1]) == int(exp):
                picked_items.append(item)
                exp = int(exp) - int(exp_cost)
                item_ammount = 0
                print(item)
                
    
    money = str(exp)
    print('Gold left: ' + money)
    print('---------------------------------------')

def runThrough():
    for i in items:
        print(i)

def findGP():
    with open(dir_item) as file:
        for line in file:
            line = line.strip()
            x = line.find(gp)
            if x > 0:
                new = line.split(gp, 1)[0]
                new = new.replace(',', '')
                new = new.replace('+', '')
                gp_val = re.findall(r'\b\d+\b\s', new)[0]
                cut = re.findall(r'\b\d+\b\s', new)[-1]
                item_val = new.split(cut, 1)[0]
                items.append([item_val, gp_val])

intro()
exit = input()
