# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    set = []
    for i in range(ord('a'),ord('z')+1):
        set.append(chr(i))
    position = (ord(letter)+n - ord('a')) % 26
    return set[position]

def rotate(word,n):
    rotated = ""
    for letters in word:
        if letters == " ":
            rotated = rotated + letters
        else:
            rotated = rotated + str(shift_n_letters(letters,n))
    return rotated




print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???