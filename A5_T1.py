marks={'Alice':85, 'Misty':97, 'Ash':88, 'Rock':79}
name=input('Enter the student\'s name:')
if name in marks:
    print(name,'marks:', marks[name])
else:
    print(name,'not in list')

