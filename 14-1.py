
inp = ["CP", "C", 
"SF", "S", 
"BH", "F", 
"SS", "N", 
"KB", "N", 
"NO", "N", 
"BP", "F", 
"NK", "P", 
"VP", "H", 
"OF", "O", 
"VH", "O", 
"FV", "F", 
"OP", "V", 
"FP", "B", 
"VB", "B", 
"OK", "S", 
"BS", "B", 
"SK", "P", 
"VV", "H", 
"PC", "S", 
"HV", "K", 
"PS", "N", 
"VS", "O", 
"HF", "B", 
"SV", "C", 
"HP", "O", 
"NF", "V", 
"HB", "F", 
"VO", "B", 
"VN", "N", 
"ON", "H", 
"KV", "K", 
"OV", "F", 
"HO", "H", 
"NB", "K", 
"CB", "F", 
"FF", "H", 
"NH", "F", 
"SN", "N", 
"PO", "O", 
"PH", "C", 
"HH", "P", 
"KF", "N", 
"OH", "N", 
"KS", "O", 
"FH", "H", 
"CC", "F", 
"CK", "N", 
"FC", "F", 
"CF", "H", 
"HN", "B", 
"OC", "F", 
"OB", "K", 
"FO", "P", 
"KP", "N", 
"NC", "P", 
"PN", "O", 
"PV", "B", 
"CO", "C", 
"CS", "P", 
"PP", "V", 
"FN", "B", 
"PK", "C", 
"VK", "S", 
"HS", "P", 
"OS", "N", 
"NP", "K", 
"SB", "F", 
"OO", "F", 
"CV", "V", 
"BB", "O", 
"SH", "O", 
"NV", "N", 
"BN", "C", 
"KN", "H", 
"KC", "C", 
"BK", "O", 
"KO", "S", 
"VC", "N", 
"KK", "P", 
"BO", "V", 
"BC", "V", 
"BV", "H", 
"SC", "N", 
"NN", "C", 
"CH", "H", 
"SO", "P", 
"HC", "F", 
"FS", "P", 
"VF", "S", 
"BF", "S", 
"PF", "O", 
"SP", "H", 
"FK", "N", 
"NS", "C", 
"PB", "S", 
"HK", "C", 
"CN", "B", 
"FB", "O", 
"KH", "O"]

form = [char for char in "SCSCSKKVVBKVFKSCCSOV"]
"""
form = [char for char in "NNCB"]
inp = ["CH", "B",
"HH", "N",
"CB", "H",
"NH", "C",
"HB", "C",
"HC", "B",
"HN", "C",
"NN", "C",
"BH", "H",
"NC", "B",
"NB", "B",
"BN", "B",
"BB", "N",
"BC", "B",
"CC", "N",
"CN", "C"]
"""

newForm = list(form)
ctr = 0
high = 0
low = 0
l = 0
countSet = set()

print(form)
print(newForm)

for x in range(40):
    l = 0
    print(x, len(form))
    while l < len(form)-1:
        if str(form[l])+str(form[l+1]) in inp:
            if l > 0:
                newForm = form[:l+1]
            else:
                newForm = list(form[l])
            newForm.append(inp[inp.index(str(form[l])+str(form[l+1]))+1])
            newForm.append(form[l+1])
            newForm += form[l+2:]
            l += 2
    
        form = list(newForm)
        newForm = []

print(form)
form.sort()
print(form)
low = len(form)
counts = []

ctr = 1
for x in range(len(form)-1):
    countSet.add(form.count(form[x]))
    if form[x] == form[x+1]:
        ctr += 1
    else:
        counts.append(ctr)
        ctr = 1
print(max(countSet)-min(countSet))
print(countSet)
#1333 too low