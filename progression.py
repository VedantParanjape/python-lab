series = input("enter a list of numbers: ").split(" ")
series = [int(i) for i in series]

isap = True
isgp = True
d = 'nil'
r = 'nil'

for i in range(len(series)-2):
    if series[i+1] - series[i] == series[i+2] - series[i+1]:
        d = series[i+1] - series[i]
        continue
    else:
        isap = False
        break

for i in range(len(series)-2):
    if series[i+1]/series[i] == series[i+2]/series[i+1]:
        r = series[i+1] / series[i]
        continue
    else:
        isgp = False
        break

print("Series is a ap: {}, d: {}".format(isap,d))
print("Series is a gp: {}, r: {}".format(isgp,r))