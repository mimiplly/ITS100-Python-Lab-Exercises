#10 times
like = 0
sad = 0
heart = 0
for i in range(1,11):

    feel = input("Feeling Like ('L'), Sad ('S'), and Heart('H')?")
    if feel in "LSH":
        if feel == "L":
            like += 1
        elif feel == "S":
            sad += 1
        elif feel == "H":
            heart += 1
    else:
        print("Invalid input, accepts only (L/S/H).")
print("================")
total = like + sad + heart
print("Total Like: %d" % total)
print("================")
likes = (like / total) * 100
sads = (sad / total) * 100
hearts = (heart / total) * 100
print("Like: %d (%.2f)." %(like,likes))
print("Sad: %d (%.2f)." %(sad,sads))
print("Heart: %d (%.2f)." %(heart,hearts))
print("================")