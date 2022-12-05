name=[]
name.append("joe")
name.append("Sally")
name.append("Jim")
name.append("June")
name.append("Betty")
name.append("Bill")
name.append("Zak")
name.append("Anne")
name.append("Kate")
print(name)

for i in range(len(name)):
    print('{} .{}'.format(i+1, name[i]))
