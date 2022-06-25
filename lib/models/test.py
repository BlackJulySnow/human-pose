s = '<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTAzNTIzMjg1NWRk">'


def findValue(name):
    i1 = s.index(name)
    i2 = s.index(name, i1 + len(name))
    i3 = s.index('"/', i2 + len(name)) + 1
    i4 = s.index('"', i3)
    # print(i2)
    print(s[i3:i4])


findValue("__VIEWSTATE")
