import math
#business_id,labels
#2 003sg,1 2 3
#write to file submission/submission.txt
#from submission/output-test.txt get the labels
#from txt/test_classified_noacc.txt get the pid
# --> matching rows
#from txt/test_photo_to_biz.txt get the bid

def txt2dic(fname):
    fn = open(fname, "r")
    dic = {}
    # a = 0
    # b = 1
    for i, line in enumerate(fn):
        (one, two, three) = line.partition(",")
        (key, val) = (one, three)
        if '\r\n' in val:
            val = val.split('\r\n')[0]
        else:
            val = val.split('\n')[0]
        dic[key] = val
    #     a += 1
    #     b = i
    # print a
    # print b
    fn.close()
    return dic

def op2ar(fname):
    fn = open(fname, "r")
    ar = []
    for line in fn:
        line = line.split("\n")[0]
        # groups = line.split(",")
        # line = " ".join(groups)
        ar.append(line)
    return ar

#photo id to bid
p2b = txt2dic("txt/test_photo_to_biz.txt")
# the output, our labels
op = op2ar("submission/output-test.txt")
#key is the pid
test = op2ar("txt/test_classified_noacc.txt")

#return dic with unique bids as keys
def revDic(fn):
    # fn = "txt/erdi"
    f = open(fn, "r")
    nd = {}
    for line in f:
        (key, val) = line.split(",")
        val = val.split("\n")[0]
        nd[val] = key
    f.close()
    return nd

xf = revDic("txt/erdi")
print "length xf: " + str(len(xf.keys()))


#return a dictionary with key = bid and val = labels in binary vector form
def makeBidVecLab(p2bDic, opAr, testAr, ubDic):
    i = 0
    bidVecLab = {}
    # p2bDic = p2b
    # testAr = test
    # opAr = op
    # ubDic = xf

    for key in ubDic.keys():
        bid = key
        if bid not in bidVecLab.keys():
                bidVecLab[bid] = [0,0,0,0,0,0,0,0,0]
        tmp = opAr[i]
        tmp = tmp.split(',')
        if '' not in tmp:
            for x in tmp:
                bidVecLab[bid][int(x)] += 1
        i += 1

    # for thing in testAr:
    #     pid = thing.split(",")[0]
    #     bid = p2bDic[pid]
    #     #if the key doesn't exist, make it
    #     if bid not in bidVecLab.keys():
    #         bidVecLab[bid] = [0,0,0,0,0,0,0,0,0]
    #     tmp = opAr[i]
    #     tmp = tmp.split(',')
    #     if '' not in tmp:
    #         for x in tmp:
    #             bidVecLab[bid][int(x)] += 1
    #     i += 1
    print "length bidVecLab: " +str(len(bidVecLab))
    return bidVecLab

testXfingers = makeBidVecLab(p2b, op, test, xf)


# return only labels that appear more than a % of the time
def getFinalLabels(dic, perc):
    if perc <= 1 and perc >= 0:
        # dic = testXfingers
        for key in dic.keys():
            labels = []
            threshold = math.ceil(perc*max(dic[key]))
            for x in xrange(0, len(dic[key])):
                if dic[key][x] >= threshold and dic[key][x] > 0:
                    labels.append(x)
            dic[key] = labels
    return dic

epic = getFinalLabels(testXfingers, 0.9)


def makeSubForm(dic):
    i = 0
    # dic = epic
    sub = open("submission/sub3.txt", "a")
    for key in dic.keys():
        i += 1
        tmp = dic[key]
        # print tmp
        entry = ""
        if tmp:
            for x in tmp[:-1]:
                entry = entry + str(x) + " "
            bla2 = tmp[-1]
            entry = entry + str(tmp[-1])
        entry = key + "," + entry + "\n"
        sub.write(entry)
        # print i
    print "length sub: " + str(i)
    sub.close()
    pass

makeSubForm(epic)


