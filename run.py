import codecs
newfilename = "c:/learn-chinese/3000.txt"
oldfilename = "c:/learn-chinese/know/already-write.txt"
outfilename = "c:/learn-chinese/generate/xiezi.txt"


def isDuplicated(char) :
  with codecs.open(oldfilename, 'r', encoding='utf8') as f:
      cc = f.read(1)
      while cc:
          if cc == char:
              return True
          cc = f.read(1)
  return False



with codecs.open(newfilename, 'r', encoding='utf8') as f:
    with codecs.open(outfilename, 'a', encoding='utf8') as t:
        char = f.read(1)
        count = 0;
        while char:
            if char==" ":
                continue
            #check if it is duplicated
            if not isDuplicated(char):

                t.write(char)
                count = count + 1
                if count == 3:
                    t.write('\n')
                    count = 0;
            char = f.read(1)
