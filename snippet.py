# -*- coding: utf-8 -*-

a=u"amīca"
b=u"amīcā"
c=u"āmīca"
l=[a,b,c]
print l
print zip(a,b)
print zip(*l)

uniq=[set(x) for x in zip(*l)]
print uniq

subresult=[]
for u in uniq:
    if(len(u)==1):
        for x in u:
            subresult.append(x)
    else:
        subresult.append('[')
        for x in u:
            subresult.append(x)
        subresult.append(']')

print "".join(subresult)
