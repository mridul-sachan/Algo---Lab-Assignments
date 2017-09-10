import copy


inputpreferslist = {
    'input1':['output2','output1'],
    'input2':['output1','output2'],
    
 }
outputpreferslist = {
    'output1':['input2','input1'],
    'output2':['input2','input1'],
    
 }
 

input = sorted(inputpreferslist.keys())
output = sorted(outputpreferslist.keys())
 
 
def matchmaker():
    global input
    print "input:",input
    inputsfree = input[:]
    print "inputsfree:",inputsfree
    switch  = {}
    inputprefers = copy.deepcopy(inputpreferslist)
    print "inputprefers",inputprefers
    outputprefers = copy.deepcopy(outputpreferslist)
    print "outputprefers",outputprefers
    while inputsfree:
        input = inputsfree.pop(0)
        print "input:",input
        inputslist = inputprefers[input]
        print "inputslist:",inputslist
        output = inputslist.pop(0)
        print "output:",output
        Newinput= switch.get(output)
        print "Newinput:",Newinput
        if not Newinput:
            # output free
            switch[output] = input
            print (switch)
        else:
            
            outputslist = outputprefers[output]
            print "satish"
            if outputslist.index(Newinput) > outputslist.index(input):
                
                switch[output] = input
                print("  %s switched %s for %s" % (output, Newinput, input))
                if inputprefers[Newinput]:
                    
                    inputsfree.append(Newinput)
            else:
                # output is already switched to old Newinput
                if inputslist:
                    # Look again
                    inputsfree.append(input)
    return switch
 
 
print('\nSwitching:')
switch = matchmaker()
 
print('\nPair:')
print('  ' + ',\n  '.join('%s is switch to %s' % pairs
                          for pairs in sorted(switch.items())))
print('Always a Pair Stable!')
