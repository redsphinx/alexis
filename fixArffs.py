#split on first occurrence of <bla>, first part becomes key, second value
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


#no idea, created to do something with teh 5 features
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


def createBidAndTest():
    test_dic = txt2dic("manyFeatures/test.txt")
    # test_ult = open("manyFeatures/test_ult.txt", "w")
    # bid_ult = open("manyFeatures/test_ult.txt", "w")
    # test_ult.close()
    # bid_ult.close()
    # test_ult = open("manyFeatures/test_ult.txt", "a")
    # bid_ult = open("manyFeatures/bid_ult.txt", "a")
    i = 0
    for key in test_dic.keys():
        i += 1
        print i
        val = test_dic[key]
        cnt = val.split(",")
        print "cnt = "+str(len(cnt))
        if len(cnt) != 245:
            print "we only have "+str(len(cnt)) + " features!"
        val = str(val) + "\n"
        print val
        # test_ult.write(val)
        # test_ult.write("\n")
        # bid_ult.write(key)
        # bid_ult.write("\n")
    # test_ult.close()
    # bid_ult.close()
    pass

createBidAndTest()

# train_dic = txt2dic("fix/bla.txt")
# test_dic = txt2dic("fix/bla_test.txt")
# train_txt = open("fix/train.txt", "a")
# test_txt = open("fix/test.txt", "a")


# fixit(train_txt, train_dic)
# fixit(test_txt, test_dic)
#
# train_txt.close()
# test_txt.close()

