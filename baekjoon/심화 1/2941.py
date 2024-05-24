# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=

word = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in alpha:
    if char in word:
        word = word.replace(char, "a")

print(len(word))