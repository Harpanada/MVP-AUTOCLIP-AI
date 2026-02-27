
a=["a","b","c","d","e","f","g","h"]
cur=[]
# current_start = a[0].start

# print(current_start)
for i , seg in a:
    print("i=",i)

    print("seg=",seg)

    cur.append(seg)
    print("cur=",cur)
    cur=[]

    # current_words += len(seg.text.split())
    if i == len(a) - 1:
        break

    next_seg = a[i+1]
    print("next_seg=",next_seg)