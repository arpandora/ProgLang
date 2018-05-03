import pandas as pd

def printKB(knowledge_base):
    print("\n","---------------------------------- KNOWLEDGE BASE ------------------------------------------","\n")

    for x in range(0,len(knowledge_base)):
        childIndent = ""
        continueIndent = ''.join([' ' for k in range(len(knowledge_base["ID"][x]))]) + "  "

        for i in range(0,knowledge_base["ID"][x].count('.')):
            childIndent = childIndent +" -->"

        sentences = [knowledge_base["Question"][x][i:i+140] for i in range(0, len(knowledge_base["Question"][x]), 140)]

        if(childIndent == ""):
            print("\n")

        for j in range(0,len(sentences)):
            if(j == 0):
                print(childIndent,knowledge_base["ID"][x]," ",sentences[j])
            else:
                print(childIndent,continueIndent,sentences[j])

def updateKB(knowledge_base):
    printKB(knowledge_base)
    choices = ["Modify","Add","Delete","Save and Exit"]



    while(True):
        print("\n","---------------------------------- AVAILABLE OPERATIONS ------------------------------------------","\n")
        for x in range(len(choices)):
            print(x+1,") ",choices[x])

        while(True):
            choice = (input("Choose the Option : "))
            if(choice == '1' or choice == '2' or choice == '3' or choice == '4' ):
                break
            else:
                print("Enter Valid Option\n")

        choice = int(choice) - 1

        if(choice == 3):
            break

        elif(choice == 0):
            print("\n")
            modifyChoices = ["Update Question","Update Passage","Update Both"]
            for x in range(len(modifyChoices)):
                print(x+1,") ",modifyChoices[x])
            while(True):
                modifyChoice = (input("Choose the Option : "))
                if(modifyChoice == '1' or modifyChoice == '2' or modifyChoice == '3' ):
                    break
                else:
                    print("Enter Valid Option\n")
            modifyChoice = int(modifyChoice) - 1

            if(modifyChoice == 0):
                while(True):
                    chosenIndex = input("\nEnter the Index : ")
                    try:
                        queryObj = knowledge_base.loc[chosenIndex]
                        break
                    except KeyError:
                        print("Index Not Found - Try Again")

                print("\n","Existing Question : ",queryObj['Question'])
                updatedQuestion = input(" Enter New Question : ")

                knowledge_base.loc[chosenIndex,'Question'] = updatedQuestion

            elif(modifyChoice == 1):
                while(True):
                    chosenIndex = input("\nEnter the Index : ")
                    try:
                        queryObj = knowledge_base.loc[chosenIndex]
                        break
                    except KeyError:
                        print("Index Not Found - Try Again")

                print("\n","Existing Passage : ",queryObj['Passage'])
                updatedPassage = input(" Enter New Question : ")

                knowledge_base.loc[chosenIndex,'Passage'] = updatedPassage

            elif(modifyChoice == 2):
                while(True):
                    chosenIndex = input("\nEnter the Index : ")
                    try:
                        queryObj = knowledge_base.loc[chosenIndex]
                        break
                    except KeyError:
                        print("Index Not Found - Try Again")

                print("\n","Existing Question : ",queryObj['Question'])
                updatedQuestion = input(" Enter New Question : ")
                print("\n","Existing Passage : ",queryObj['Passage'])
                updatedPassage = input(" Enter New Passage : ")

                knowledge_base.loc[chosenIndex,'Passage'] = updatedPassage
                knowledge_base.loc[chosenIndex,'Question'] = updatedQuestion
            print('\n\n',"Modification Successful","\n\n")

        elif(choice == 1):
            while(True):
                chosenIndex = input("\nEnter the Parent Index : ")
                try:
                    childCount = 0
                    queryObj = knowledge_base.loc[chosenIndex]
                    for x in range(len(knowledge_base['ID'])):
                        if(knowledge_base['ID'][x].startswith(chosenIndex) and (knowledge_base["ID"][x].count('.') == 1) and (knowledge_base['ID'][x] != chosenIndex)):
                            childCount = childCount + 1
                            print(knowledge_base['ID'][x])


                    newIndex = chosenIndex+"."+str(childCount+1)
                    if(childCount != 0):
                        prevIndex = chosenIndex+"."+str(childCount)
                    else:
                        prevIndex = chosenIndex

                    print(prevIndex,"--. splitIndex")
                    splitIndex = knowledge_base.index.get_loc(prevIndex) + 1


                    newQuestion = input("Enter Question : ")
                    newPassage = input("Enter Passage : ")

                    newRow = pd.DataFrame({"ID": newIndex, "Question":newQuestion , "Passage":newPassage}, index=[newIndex])
                    knowledge_base = pd.concat([knowledge_base.ix[:splitIndex], newRow, knowledge_base.ix[splitIndex:]])
                    knowledge_base['qID'] = knowledge_base['ID']
                    knowledge_base.set_index("qID", inplace=True)


                    break

                except KeyError:
                    print("Index Not Found - Try Again")
            print('\n\n',"Addition Successful","\n\n")


        elif(choice == 2):
            while(True):
                chosenIndex = input("\nEnter the Index : ")
                try:
                    while(True):
                        queryObj = knowledge_base.loc[chosenIndex]
                        print("\n","Existing Question : ",queryObj['Question'])
                        print(" Existing Passage : ",queryObj['Passage'])
                        proceedChoice = input(" Do You Want To Proceed(Children will also be deleted)? Enter(Y/N) : ")
                        if(proceedChoice == 'Y' or proceedChoice == 'y'):
                            knowledge_base =  knowledge_base[knowledge_base.ID.str.startswith(chosenIndex) == False]
                            print(" Deleted Index ",chosenIndex)
                            break
                        elif(proceedChoice == 'N' or proceedChoice == 'n'):
                            print(" Not Deleted")
                            break
                        else:
                            print(" Enter Y or N Only")
                    break

                except KeyError:
                    print("Index Not Found - Try Again")

            print('\n\n',"Deletion Successful","\n\n")

    return knowledge_base


if __name__ == '__main__':

    knowledge_base_questions = pd.read_csv("test_questions.txt",sep = "_", names = ["ID", "Question"])
    knowledge_base_passage = pd.read_csv("test_passage.txt",sep = "_", names = ["ID", "Passage"])
    knowledge_base = knowledge_base_questions
    knowledge_base['Passage'] = knowledge_base_passage["Passage"]
    knowledge_base = knowledge_base.fillna(0)
    knowledge_base['qID'] = knowledge_base['ID']
    knowledge_base.set_index("qID", inplace=True)

    updatedKB = updateKB(knowledge_base)
    updatedKB_Questions = updatedKB[['ID','Question']]
    updatedKB_Passage = updatedKB[['ID','Passage']]

    updatedKB_Questions.to_csv("updatedKB_Questions.txt",sep="_",header = False , index = False)
    updatedKB_Passage.to_csv("updatedKB_Passage.txt",sep="_",header = False , index = False)
