def getComponents(tablelines):
    labels = [line.split()[-1] for line in tablelines[1:-1]]
    values = [line.split()[:-4] for line in tablelines[1:-1]]
    return labels,values

_latexTableTemplate = "\\begin{table}[t]\n"\
"\centering\n" \
"\setlength{\\tabcolsep}{0.2em}\n" \
"\\begin{tabular}{|| @N_CLASSES ||}\n" \
" \hline\n" \
" Label & @CLASSES \\\ [0.5ex]\n" \
 "\hline\hline\n" \
"@TABLELINES \\\ [1ex]\n"\
"\hline\n"\
"\end{tabular}\n"\
"\caption{@CAPTION}\n"\
"\end{table}\n"\



def makeMainTable(labels,values):
    maintblines = []
    for index, label in enumerate(labels):
        maintblines.append(label + " & " + " & ".join(values[index]))
    return " \\\ \n".join(maintblines)

if __name__ == '__main__':
    tablelines = []
    line = "a"
    while line != "":
        line = input()
        tablelines.append(line)
    labels, values = getComponents(tablelines)
    Nclasses_STR = ((len(labels)+1) * "c ")[:-1]
    classes_STR = " & ".join(labels)
    maintb = makeMainTable(labels, values)
    table = _latexTableTemplate.replace("@N_CLASSES",Nclasses_STR).replace("@CLASSES",classes_STR).replace("@TABLELINES",maintb)
    print(table)



