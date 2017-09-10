
def tma(items):
    #print(items)
    n = 4

    mAlloted = [0,0,0,0]
    fAlloted = [0,0,0,0]
    choiceList = []
    choiceList.append([])
    choiceList.append([])
    choiceList.append([])
    choiceList.append([])

    # Run the loop until all men are engaged
    while n > 0:
        for c in range(0,4):
            # If the current men is not engaged
            print("For man {}".format(c + 1))
            if mAlloted[c] != 1:
                # Loop through the current men preference list
                for i in range(0, 4):
                    choice = items[c][i]
                    # print("Man {0}, Women {1}".format(c+1,choice))
                    pp = 0
                    if choice == 5:
                        pp = 0
                    elif choice == 6:
                        pp = 1
                    elif choice == 7:
                        pp = 2
                    elif choice == 8:
                        pp = 3
                    else:
                        pp = 0

                    if fAlloted[pp] != 1:
                        fAlloted[pp] = 1
                        mAlloted[c] = 1
                        choiceList[c].append(choice)
                        choiceList[c].append(c + 1)
                        n -= 1
                        #c += 1
                        print("Alloted Women {0} with {1}".format(choice, c+1))
                        break

                    elif fAlloted[pp] == 1:
                        # Check for the position of proposing male in females preference list
                        # print(choice)
                        pos1 = items[choice - 1].index(c + 1)
                        print(pos1)
                        pos_person = 0
                        pos_temp = 0;
                        # Find the index for already engaged man in the list
                        for j in range(0, 4):
                            if choice in choiceList[j]:
                                pos_temp = j
                                pos_person = choiceList[j][1]

                        pos2 = items[choice - 1].index(pos_person)
                        print(pos2)
                        if pos1 > pos2:
                            choiceList[pos_temp][1] = c + 1
                            mAlloted[c] = 0
                            n -= 1
                            #c += 1
                            break


    print(choiceList)











if __name__ == "__main__":
    preference_list = []
    preference_list.append([])
    preference_list.append([])
    preference_list.append([])
    preference_list.append([])
    preference_list.append([])
    preference_list.append([])
    preference_list.append([])
    preference_list.append([])

    # Mens Preference
    preference_list[0].append(6)
    preference_list[0].append(8)
    preference_list[0].append(5)
    preference_list[0].append(7)

    preference_list[1].append(5)
    preference_list[1].append(8)
    preference_list[1].append(7)
    preference_list[1].append(6)

    preference_list[2].append(5)
    preference_list[2].append(7)
    preference_list[2].append(6)
    preference_list[2].append(8)

    preference_list[3].append(8)
    preference_list[3].append(6)
    preference_list[3].append(5)
    preference_list[3].append(7)

    # Womens preference
    preference_list[4].append(1)
    preference_list[4].append(4)
    preference_list[4].append(2)
    preference_list[4].append(3)

    preference_list[5].append(4)
    preference_list[5].append(1)
    preference_list[5].append(2)
    preference_list[5].append(3)

    preference_list[6].append(1)
    preference_list[6].append(2)
    preference_list[6].append(3)
    preference_list[6].append(4)

    preference_list[7].append(4)
    preference_list[7].append(3)
    preference_list[7].append(2)
    preference_list[7].append(1)

    tma(preference_list)

