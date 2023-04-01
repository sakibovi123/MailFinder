arr = [3232, 3232, 3232, 3232, 3232]
new = []
# add 1 to each element of the list
for i in range(len(arr)):
    new.append(arr[i]+i)
print(new)

for j in range(len(new)):
    new.remove(new[j])
print(new)

# print the updated list

