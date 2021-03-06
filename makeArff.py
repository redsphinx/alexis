import time

# makes a unique pair train and text file
def makeFile():
    pt1 = time.strftime("%d/%m/%Y")
    pt1 = ("_").join(pt1.split("/"))
    pt2 = time.strftime("%H:%M:%S")
    pt2 = ("_").join(pt2.split(":"))
    traname = "pipe/" + "train" + "_" + pt1 + "_" + pt2 + ".txt"
    tesname = "pipe/" + "test" + "_" + pt1 + "_" + pt2 + ".txt"
    # open(traname, "w")
    open(tesname, "w")
    # traf = open(traname, "a")
    tesf = open(tesname, "a")
    with open("txt/blaBU.txt") as f:
        for line in f:
            # traf.write(line)
            tesf.write(line)
        # with open(name, "w") as f1:
        #     for line in f:
        #         f1.write(line)
    return (traname,tesname)
    pass


# convert text file to dictionary
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
    pass


def makeTraArff(p2b, traincl, trabla, train, attNum):
    blank = [0,0,0,0,0,0,0,0,0]
    i=0
    for key1 in p2b.keys():
        i += 1
        pid = key1
        bid = p2b[key1]
        #get the matching bid in train and get them labels
        labels = str(train[bid])
        #change format of them labels
        labels = map(int, labels.split())
        for x in xrange(0,9):
            if x in labels:
                blank[x] = 1
            else:
                blank[x] = 0
        blank = ','.join(map(str, blank))
        blank = blank + ","
        # blank = ","+blank
        labels = blank
        blank = [0,0,0,0,0,0,0,0,0]
        #get the matching pid in traincl and paste them labels
        #check if traincl contains this picture
        if pid in traincl.keys():
            #check for the num of attributes
            line3 = traincl[pid]
            line3 = line3.split("\n")[0].split(",")

            # line3 = str(pid)+","+str(traincl[pid])
            # line3 = line3.split("\n")[0]
            line3 = line3[:attNum]
            l3 = ""
            for item in line3[:-1]:
                l3 += item + ","
            l3 += line3[-1]

            # print l3
            # line3 = line3+labels+"\n"
            line3 = labels+l3+"\n"
            # print line3
            #write line to bla
            # trabla.write(line3)
            print(str(i)+": "+line3)
    pass


def makeTesArff(tesbla, testcl, attNum):
    blank = [0,0,0,0,0,0,0,0,0]
    blank = ','.join(map(str, blank))
    blank = blank + ","

    for i, line in enumerate(testcl):
        #check for the num of attributes
        line = line.split("\n")[0].split(",")
        line = line[1:attNum+1]
        l3 = ""
        for item in line[:-1]:
            l3 += item + ","
        l3 += line[-1]

        line = blank+l3+"\n"

        tesbla.write(line)
    tesbla.close()
    testcl.close()
    print "makeTesArff done"
    pass

# --- main
p2b = txt2dic("txt/train_photo_to_biz_ids.txt")
(trafn, tesfn) = makeFile()
trabla = open(trafn, "a")
tesbla = open(tesfn, "a")
train = txt2dic("txt/train.txt")
traincl = txt2dic("txt/train_classified_noacc.txt")
testcl = open("txt/test_classified_noacc.txt", "r")

attNum = 2
if attNum >0 and attNum < 6:
    # makeTraArff(p2b, traincl, trabla, train, attNum)
    makeTesArff(tesbla, testcl, attNum)

trabla.close()
tesbla.close()
testcl.close()