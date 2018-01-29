passingBool = False
with open("testing.txt", "rt") as fin:
    with open("testingout.txt", "wt") as fout:
        for line in fin:
            #print("line[:15]:",line[:15])
            if line[:15] == ' \t<ReportImage>':
                passingBool = True
                #print("inside if")
            elif passingBool == True and line[:15] == ' \t<ImageType>PD':
                passingBool = False
                fout.write(' 	<ReportImage>REPLACEME</ReportImage>\n')
                fout.write(line)
                #print("inside elif")
            elif passingBool == False:
                fout.write(line)
