import glob


def Read(dataDirect):
    sentences = []
    defOrNotDef = []
    path = dataDirect
    files = glob.glob(path)
    for name in files:
        number_of_lines = len(open(name, encoding="utf8").readlines())
        with open(name, "r", encoding="utf8") as file:
            for i in range(number_of_lines):
                x = file.readline().split()
                if int(x[-1].strip('"')) == 0:
                    del x[-1]
                    temp = " ".join(x)
                    if temp.startswith('"') and temp.endswith('"'):
                        temp = temp[1:-1]
                    sentences.append(temp)
                    defOrNotDef.append(0)
                else:
                    del x[-1]
                    temp = " ".join(x)
                    if temp.startswith('"') and temp.endswith('"'):
                        temp = temp[1:-1]
                    sentences.append(temp)
                    defOrNotDef.append(1)

    return sentences, defOrNotDef
