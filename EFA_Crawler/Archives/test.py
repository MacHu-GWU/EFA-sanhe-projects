from tools._ref_data import lastnamelist

data = {lastname: {str(i) : -1 for i in range(1900, 2021)} for lastname in lastnamelist}

print data