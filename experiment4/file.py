s = 'python'
wf = open('test.txt','w')
wf.write(s)
wf.close()

rf = open('test.txt','r')
r_str = rf.read()
print(r_str)
rf.close()

with open('test.txt','r') as f:
    r_str = f.read()
    print(r_str)