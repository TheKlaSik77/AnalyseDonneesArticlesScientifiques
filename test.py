from collections import OrderedDict

d = {2014: {"bonjour" : 2,"aurevoir" : 1,"hello" : 8,"ahh" : 4},
          2012: {"step" : 5,"eho" : 4,"ahez" : 2,"msdfkls" : 14},
          2022: {"sefsee" : 1,"fgdgg" : 6,"erzad" : 3,"qdndc" : 2},
          1989: {"sdfvcxx" : 4,"lfdkos" : 2,"azddsf" : 9,"dsfzza" : 5}
         }

d_sort = OrderedDict(sorted(d.items()))

print(f"{d_sort}\n\n")

for cle in d_sort:
    value_sort = dict(sorted(d_sort[cle].items(), key=lambda item: item[1], reverse=True))
    d_sort[cle] = value_sort

print(d_sort)

for cle in enumerate(d_sort):
    print(cle)
