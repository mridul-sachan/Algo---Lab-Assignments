QUESTION 2:
SOLUTION:



import copy

input_preferslist = {
    'input1':['output2','output1','output4','output3'],
    'input2':['output1','output4','output2','output3'],
    'input3':['output3','output2','output4','output1'],
    'input4':['output3','output2','output1','output4'],

    
 }
output_preferslist = {
    'output1':['input2','input1','input4','input3'],
    'output2':['input1','input4','input3','input2'],   
    'output3':['input1','input2','input4','input3'],
    'output4':['input4','input1','input2','input3'],
    
 }
 

input = sorted(input_preferslist.keys())
output = sorted(output_preferslist.keys())
 
 
def switch_connection():
    global input
    inputprefers = copy.deepcopy(input_preferslist)
    outputprefers = copy.deepcopy(output_preferslist)
    print('Input preferences :',inputprefers,'\n')
    print('Output preferences :',outputprefers,'\n')
    print('\nSwitching_connection:')
    inputsfree = input[:]
    switch  = {}
   
    while inputsfree:
        input = inputsfree.pop(0)
        inputslist = inputprefers[input]
        output = inputslist.pop(0)
        Newinput= switch.get(output)
        if not Newinput:
         
            switch[output] = input
            print (switch)
        else:
            
            outputslist = outputprefers[output]
            if outputslist.index(Newinput) > outputslist.index(input):
                
                switch[output] = input
                print("  %s switched %s for %s" % (output, Newinput, input))
                if inputprefers[Newinput]:
                    
                    inputsfree.append(Newinput)
            else:
               
                if inputslist:
                   
                    inputsfree.append(input)
    return switch
 
 

switch = switch_connection()
 
print('\nPair:')
print('  ' + ',\n  '.join('%s is switch to %s' % pairs
                          for pairs in sorted(switch.items())))
print('Always a Stable Pair!')
