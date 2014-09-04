import pickle
def search(name):
    data = pickle.load(open('uses_data.p', 'rb'))
    res = list()
    for line, drugname in data.iteritems():
        if name in line:
            res.append( '%s\n\t%s\n' % (drugname, line) )
    return '\n'.join(res)

print search('congestive heart failure')