f = "Hello world"
f = f.split()[::-1]
f.append('!')
f.insert(0, '!')
f = ' '.join(f)
print(f)