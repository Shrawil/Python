items = input("Enter items for list seperated by comma : ")
ls = items.split(',')
itemsList = list()
for item in ls:
    item = item.strip()
    try: 
        itemsList.append(int(item))
    except ValueError:
        try:
            itemsList.append(float(item))
        except ValueError:
            if item == 'True':
                itemsList.append(True)
            elif item == 'False':
                itemsList.append(False)
            elif item in (None, ''):
                itemsList.append(None)
            else:
                itemsList.append(str(item))
print(itemsList)