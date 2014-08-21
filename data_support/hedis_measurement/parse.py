##coding=utf8
'''本脚本用于从data文件夹中得所有文本中提取数据，数据结构是:
{ 文件名1 : 
    { step1 : string1,
      step2 : string2,
      ...
    },
  文件名2 :
    { step1 : string1,
      step2 : string2,
      ...
    },
  ...
}
'''
import jsontree
import os

data = jsontree.jsontree()
 
root = 'data'

for fname in os.listdir(root): ## 比较典型的 关键字作为数据录入的开关的生成器
    name, _ = os.path.splitext(fname)
    
    with open(os.path.join(root, fname), 'rb') as f:
        ctt = list()
        counter = 0
        start_flag = 0
        for line in f.xreadlines():
            line = line.strip()
            
            if 'Step' in line:
                counter += 1
                start_flag = 1
                ctt.append(list())
                continue
            
            if (start_flag == 1) & (counter >= 0):
                ctt[counter-1].append(line)
    
    counter = 1    
    for l in ctt:
        data[name]['step ' + str(counter)] = '\n'.join(l)
        counter += 1

str = jsontree.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

with open('hedis.json', 'wb') as f:
    f.write(str)
