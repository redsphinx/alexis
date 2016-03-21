bla_test = open("txt/bla_test_2.txt", "a")
testcl = open("txt/test_classified_noacc.txt", "r")

# blank = [0,0,0,0,0,0,0,0,0]
# blank = ','.join(map(str, blank))
# blank = ","+blank
# print blank

for i, line in enumerate(testcl):
    # line = line.split("\n")[0]
    # line = line+blank+"\n"
    # print line
    # bla_test.write(line)

bla_test.close()