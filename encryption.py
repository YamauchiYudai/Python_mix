before_word = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
after_word = []

k = int(input("k >"))

for i in range(0,26-k):
    after_word.append(before_word[i+k])
for i in range(26-k,26):
    after_word.append(before_word[i-26+k])
a = ("")
b = ("")
for i in range(0,26):
    a += before_word[i]
    b += after_word[i]

print("[exchange table]")
print(a)
print(b)
print()
n = input("please input\n")
x =[]
for i in range(0,len(n)):
    for j in range(0,26):
        if n[i] == before_word[j]:
            x.append(after_word[j])

y =[]
for i in range(0,len(n)):
    for j in range(0,26):
        if x[i] == after_word[j]:
            y.append(before_word[j])

c = ("")
d = ("")
for i in range(0,len(n)):
    c += x[i]
    d += y[i]

print("Before encryption ->",n)
print("after encryption ->",c)
print("after decoding ->",d)
