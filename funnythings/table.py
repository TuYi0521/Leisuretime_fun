from prettytable import PrettyTable
v = ["Name", "court", "time"]
x = PrettyTable(v)
x.add_row(["SongL", 32, "北京"])
x.add_row(["Wang Haoyang", 45, "天津"])
x.add_row(["TuYi", 28, "河北"])
# print(x)
print(x.get_string(sortby="court"))
# print(x.get_string(sortby="court", reversesort=True))

print('\n'.join([' '.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

