from jt import load_jt, dump_jt, prt_jt, d2j


walgreens = load_jt('walgreens.txt')

for id, info in walgreens.iteritems():
    if len(info['hours']) != 6:
        print id, info['hours']