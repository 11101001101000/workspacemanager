import os as exec
end = 0
os = 0
hd = 0
a = 0
while end == 0:
    if os == 0 or hd == 0:
        os = input ('which os are you on, win or linux?  ')
        hd = input ('workspace dir path:  ')
        print ('Welcome to WorkspaceManager.')
    print('''1) view workspace structure
2) create new workspace
3) delete existing workspace
4) change os
5) change workspace path''')
    a = input()
    if a == '1':
        if os == 'win':
            exec.system ('dir ' + hd)
    if a == '4':
        os = 0
    if a == '5':
        hd = 0