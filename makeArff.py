#TODO select how many attributes to use
#TODO put in correct order. get rid of fixArrfs.py
# -- also fo the test data

import time

#makes a unique file for the train file
#tot = string so "test" or "train"
def makeFile(tot):
    pt1 = time.strftime("%d/%m/%Y")
    pt1 = ("_").join(pt1.split("/"))
    pt2 = time.strftime("%H:%M:%S")
    pt2 = ("_").join(pt2.split(":"))
    name = "pipe/" + tot + "_" + pt1 + "_" + pt2 + ".txt"
    open(name, "w")
    with open("txt/blaBU.txt") as f:
        with open(name, "w") as f1:
            for line in f:
                f1.write(line)
    return name

#convert text file to dictionary
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

# p2b = txt2dic("txt/train_photo_to_biz_ids.txt")
# fn = makeFile("train")
# bla = open(fn, "a")
# train = txt2dic("txt/train.txt")
# traincl = txt2dic("txt/train_classified_noacc.txt")



def makeIt():

    pass
# blank = [0,0,0,0,0,0,0,0,0]
# i=0
# for key1 in p2b.keys():
#     i += 1
#     pid = key1
#     bid = p2b[key1]
#     #get the matching bid in train and get them labels
#     labels = str(train[bid])
#     #change format of them labels
#     labels = map(int, labels.split())
#     for x in xrange(0,9):
#         if x in labels:
#             blank[x] = 1
#         else:
#             blank[x] = 0
#     blank = ','.join(map(str, blank))
#     blank = ","+blank
#     labels = blank
#     blank = [0,0,0,0,0,0,0,0,0]
#     #get the matching pid in traincl and paste them labels
#     #check if traincl contains this picture
#     if pid in traincl.keys():
#         line3 = str(pid)+","+str(traincl[pid])
#         line3 = line3.split("\n")[0]
#         line3 = line3+labels+"\n"
#         #write line to bla
#         # bla.write(line3)
#         print(i)
#
# bla.close()
