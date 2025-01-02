#WAp to remove the duplicate letters in a string

a= 'cbvashcvSAhaBSbm'
out=' '
for i in a:
    if i not in out:
        out+=i
print(out)