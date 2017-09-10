import time
import random
from matplotlib import pyplot as py

def tma(choice_list, no, c):
    #Output array
    output=[]
    mFree=[]
    t0 = time.clock()
    print("Case",c,":", choice_list)

    #Initialize the mathing list for male and female
    for j in range(0,no):
        output.append(0)
        mFree.append(0)


    freeCount = no

    
    #Loop until all mens are matched
    while freeCount>0:
        for k in range(0,no):
            # If already paired exit
            if mFree[k] == 1:
                break


            # Loop through each womens
            for j in range(0,no):
                choice = choice_list[k][j]

                # If female is not previously engaged assign it with the requesting man
                if output[choice-no-1] == 0:
                    output[choice-no-1] = k+1
                    mFree[k] = 1
                    freeCount-=1
                    break
                # If female is already engaged
                else:
                    currentPartner = output[choice-no-1]
                    print("Women {} currently engaged with {}".format(choice, currentPartner))
                    # Find the position of requesting male in womens preference list
                    pos1 = 0
                    # Position of currently engaged partner
                    pos2 = 0
                    #print(choice_list[4].index(k+1))
                    for n in range(no,no*2):
                        if (k+1) == choice_list[n]:
                            pos1 = choice_list[n].index(k+1)
                            output[choice-no-1] = k+1
                            mFree[k] = 1
                            mFree[currentPartner-1] = 0
                            break

                            
                            
                            


                    # Compare the position of both the proposal in women's preference list
                    #print("Pos1 {0} Pos2 {1}".format(pos1,pos2))
                    #if pos1 > pos2:
                        

    g = no+1
    for l in output:
        print("Women {} paired with {}".format(g,l))
        g+=1

    # Return Execution time
    return  time.clock()-t0
                    

                    
                

    

# Driver function
if __name__ == "__main__":
    t0=0
    cases = 4
    choice = 0
    x = []
    y = []

    print("1. TMA")
    print("2. TMA analysis")
    choice = int(input(">"))

    if choice == 1:
        choice_list = []
        for i in range(0, 8):
            if i < 4:
                choice_list.append(random.sample(range(5,9),4))
            else:
                choice_list.append(random.sample(range(1,5), 4))

        time_taken = tma(choice_list, 4, 1)
        print("Execution time: ",time_taken)

    else:
        for n in range(1, 20, 2):
            # cases = cases * 2
            x.append(cases)
            choice_list = []
            for i in range(0, cases * 2):
                if i < (cases):
                    choice_list.append(random.sample(range(cases + 1, (cases * 2) + 1), cases))

                else:
                    choice_list.append(random.sample(range(1, cases + 1), cases))

            t0 += 1
            y.append(tma(choice_list, cases, t0))
            print("=" * 100)
            cases += 2


        py.plot(x, y, 'g')
        py.ylabel('Time (in seconds)')
        py.xlabel('No of pairs')
        py.show()

    
