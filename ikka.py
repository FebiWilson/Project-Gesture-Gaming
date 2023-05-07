def sort_list(ikka):
    leng = len(ikka)
    for i in range(0,leng):
        for j in range(i+1,leng):
            min = ikka[i][0]
            pos = i
            if min > ikka[j][0]:
                pos = j
            temp = ikka[i]
            ikka[i] = ikka[pos]
            ikka[pos] = temp
def sort_int(ikka):
    leng = len(ikka)
    poplist=[]
    for i in range(0,leng-1):
        if ikka[i][1] > ikka[i+1][0]:
            ikka[i][1] = ikka[i+1][1]
            poplist.append(i+1)
            print(leng)
    for i in poplist:
        ikka.pop(i)
list = [[6,8],[2,4],[1,3],[9,10]]
print(list)
sort_list(list)
print(list)
sort_int(list)
print(list)

