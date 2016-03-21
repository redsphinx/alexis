def txt2dic(fname):
    fn = open(fname, "r")
    dic = {}
    for i, line in enumerate(fn):
        (one, two, three) = line.partition(",")
        (key, val) = (one, three)
        if '\r\n' in val:
            val = val.split('\r\n')[0]
        else:
            val = val.split('\n')[0]
        dic[key] = val
    fn.close()
    return dic


def fixit(txt, dic):
    n = 5
    i = 0
    for key in dic.keys():
        i += 1
        nl = dic[key]
        groups = nl.split(",")
        nl = ','.join(groups[:n]), ','.join(groups[n:])
        nl = str(nl[1])+","+str(nl[0])+"\n"
        txt.write(nl)
        print i
    pass

train_dic = txt2dic("fix/bla.txt")
test_dic = txt2dic("fix/bla_test.txt")
train_txt = open("fix/train.txt", "a")
test_txt = open("fix/test.txt", "a")


fixit(train_txt, train_dic)
fixit(test_txt, test_dic)

train_txt.close()
test_txt.close()