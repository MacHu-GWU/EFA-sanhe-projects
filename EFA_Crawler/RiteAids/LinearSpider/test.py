def gen():
    for i in xrange(4):
        yield i
        
        
for j in gen():
    print j
    
print j + 2