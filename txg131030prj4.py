# Author: Twinkle Gupta
# File Description : This project develops a program that implements arithmetic with large integers, of arbitrary size.
#                    Negative numbers are not handled.
# Date : Sept 23,2014

import re

class ListOperations:
# Dictionary (kind of hashmap)to map the variables given in input with their corresponding list
    varToListDict = {}
# Maintaining a list of input cmds so as to loop back when cmd is of type var?lineno
    inputCmdsList = []
    base = 10  # fixed all opeartions to base 10

# Function Description : This function parses the input cmd one by one. Its like the infix to postfix conversion
#                        algorithm, whenever it encounters a variable it pushes it to the stack(which is a list by
#                        implementation named varStack) and whenever it encounters a symbol it either pops the var
#                        and finds its mapping list using varToListDict which is a dictionary of variables and their
#                        corresponding lists or performs someother operation as listed
# Parameter : inputstr: string containing the user given statement ( Note it's just a single statement)
# Pre-condition : None
# Post-condition : None
    def ProcessInputCmd(self, inputstr):
        varStack = [] #stack to maintain the order of variables in a given input cmd
        resultantList = []
        i = 2
        flag = 0 #To inform that var = 0 and stop the loop now, in cases where cmd is of type var?lineno
        #breaking the input cmd into tokens eg- var=var1+var2 then token is a list containing= [var,=,var1,+,var2]
        done = 'false'
        while done != 'true' and i<len(inputstr):
            token = inputstr[i]
            pattern1 = re.compile('[a-z]')
            if pattern1.match(token):
                varStack.append(token) # if the token is an alphabet i.e variable, then push it into the stack

            elif token == '=':
            #if after "=" there is a number means cmd is of type var1 = no otherwise its of type var = var1 op var2
                token = inputstr[4] # get the token next to "="
                pattern2 = re.compile('[0-9]')
                if pattern2.match(token): # check if its a no
                    tempList = self.StrToNum(inputstr[4:]) #convert the no to a list
                    self.varToListDict[varStack.pop()] =  tempList #map the list to the variable var
                    done = 'true'
            #if its not a no then do nothing

            elif token == '?':
            # Cmd is of type var?lineno , so check the value of var
                tempList = self.varToListDict[varStack.pop()]
                varVal = self.NumToStr(tempList)
                if int(varVal) == 0:
                    flag = 1
                else: # var != 0 so iterate through the line no given
                    lineno = int(inputstr[4:]) # fetching the lineno
                    while flag != 1:
                        inputstr = self.inputCmdsList[lineno -1]
                        flag = self.ProcessInputCmd(inputstr) #iterating through that line no
                        lineno += 1
                done = 'true'

            elif token == '+' or token == '-' or token == '^' or token == '*':
                list1 = self.varToListDict[varStack.pop()] # get list corresponding to first operand
                list2 = self.varToListDict[inputstr[6]] # get list corresponding to second operand
                if token == '+':
                    resultantList = self.Add(list1, list2)
                elif token == '-':
                    resultantList = self.Subtract(list1, list2)
                elif token == '*':
                    resultantList = self.Multiply(list1, list2)
                elif token == '^':
                    resultantList = self.Power(list1, list2)
                # var in cmd var=var1+var2 is fetched from stack and assigned the resultant list
                self.varToListDict[varStack.pop()] = resultantList
                done = 'true'
            else:
                print "Error!!! Incorrect Cmd" #if the char is not any of above type then print error message
                done = 'true'
            i += 1
        #if stack still has elements means the cmd is of type "var" i.e we need to print value of var
        if varStack:
            #printing the var value by first fetching its corresponding list and then converting the list to a string
            item = varStack.pop()
            for var, list in self.varToListDict.iteritems():
                if var == item:
                    print self.NumToStr(list) #this prints the variable value
        return flag


# Function Description : Converts a given number in string format to a list of integers
# Parameter : str : string containing the number
# Pre-condition : None
# Post-condition : None
    def StrToNum(self, str):
        i = len(str) - 1
        list = []
        while i>=0:
            list.append(int(str[i])) #copying the string elements in reverse order to a list
            i -= 1
        return list

# Function Description : Converts a given list of integers to a number in string format.
# Parameter : list : list of integers which is to be converted into a string
# Pre-condition : None
# Post-condition : None
    def NumToStr(self, list):
        newstr =""
        for element in list:
            # copying the numbers in the list to a string. Note: list contains the number in reverse order
            newstr += str(element)
        newstr = newstr[::-1] #reversing the string. Now the string contains the correct order of the number.
        return newstr

# Function Description : This function adds two list of integers and returns the added value as a list of integers
# Parameter : list1 : list of integers representing the first operand in addition operation
#             list2 : list of integers representing the second operand in addition operation
# Pre-condition : None
# Post-condition : None
    def Add(self, list1, list2):
        resultantList = []
        carry = 0
        sum = 0
        i = 0
        len1 = len(list1)
        len2 = len(list2)
        if len1 > len2:
            count = len(list1)
        else:
            count = len(list2)
        while i<count: # run the addition algorithm until it reaches to the end of both of the lists
            if i<len1: # if list1 has elements take it else put it '0' so that it doesn't contribute to the sum
                element1 = list1[i]
            else:
                element1 = 0
            if i<len2: # if list2 has elements take it else put it '0' so that it doesn't contribute to the sum
                element2 = list2[i]
            else:
                element2 = 0
            sum = element1+element2+carry # add the numbers and the previous addition's carry over
            carry = sum/self.base
            sum = sum%self.base
            resultantList.append(sum)# store the added value to the resultant list
            i += 1
        if carry > 0:
            resultantList.append(carry)
        return resultantList

# Function Description : This function subtracts n2 (represented by list2) from n1 ( represented  by list1)
# Parameter : list1 : list of integers representing the first operand in subtraction operation
#             list2 : list of integers representing the second operand in subtraction operation
# Pre-condition : None
# Post-condition : None
    def Subtract(self, list1, list2):
        borrow = 0
        diff = 0
        count = 0
        # as list1 is going to be altered while taking borrow so instead keep the original and alter the copy of it
        list1Copy = []
        resultantList = []
        newList = []
        newList.append(0)
        for element in list1:
            list1Copy.append(element)
        len1 = len(list1Copy)
        len2 = len(list2)
        if len1 < len2:
        # list1 has lesser no of digits than list2 i.e n1<n2, so result will be neg, so return 0 as the resultant list.
            return newList
        while count<len1:
            element1 = list1Copy[count]
            if count<len2: # if list2 has elements take it else put it '0' so that it doesn't contribute to diff
                element2 = list2[count]
            else:
                element2=0
            # if element1 < element2 then take a borrow, its going to be neg
            # second case is if element1 >=element2 then no issue perform normal subtraction (borrow remains to be 0)
            if element1 < element2:
                i = 1
                if count+i >= len1: # if they are no eligible lenders and the list has hit the last msb
                    return newList # then exit by returning 0 as the  resultant list
                while list1Copy[count+i] == 0: #find the next eligible lender to take the borrow
                    i += 1
                list1Copy[count+1] -= 1 #found an eligible lender, now lending '10' from it
                borrow =1
            diff = (element1+borrow*self.base)-element2 # add the borrow and then sub element2 from element1
            resultantList.append(diff) # store the added value to the resultant list
            borrow = 0
            count += 1
        temp = resultantList.pop()
        # if last element in resultant list is 0 i.e after subtraction the msb has become 0 so discard the msb
        # but if its single digit like resultant list is = 0 then keep it or if msb is nonzero then also keep the msb.
        if temp !=0 or len(resultantList) == 0:
            resultantList.append(temp)
        return resultantList

# Function Description : Computes the product of two numbers represented by list1 and list2. It calculates the product
#                        row by row by shifting the entry of each row accordingly and adds the entry of two rows
#                        simulataneously.
# Parameter :list1 : list of integers representing the first operand in multiplication operation
#            list2 : list of integers representing the second operand in multiplication operation
# Pre-condition : None
# Post-condition : None
    def Multiply(self, list1, list2):
        tempList = []
        resultantList = []
        carry = 0
        count = 0
        for element2 in list2:
            count +=1# counting the no of rows in the prod operation so as to add that many zeroes in the next row
            for element1 in list1:
                prod = element1*element2 + carry #computing the product
                carry = prod/self.base
                prod = prod%self.base
                tempList.append(prod)
            if carry > 0:
                tempList.append(carry)
                carry = 0
            resultantList = self.Add(resultantList, tempList) #adds prod of a row with the previous rows
            del tempList[:] #emptying the list so that it can store the next row of the products
            temp = count
            while temp >0: #shifting the next row by adding zeroes to the list
                tempList.append(0)
                temp -= 1
        return resultantList

# Function Description : Computes n1 ^ n2 where n1 is represented by list1 and n2 by list2
# Parameter :list1 : list of integers representing the first operand in power operation
#            list2 : list of integers representing the second operand in power operation
# Pre-condition : None
# Post-condition : None
    def Power(self, list1, list2):
        count = 0
        resultantList = list1

        for element in list2:
            #for every element in list2 compute its position in the number n2 , suppose that list2 represents n2 = 789
            # then this loop generates first 9 then in next for loop it produces 8*10 and then 7*10*10 in the last for
            # loop iteration
            while count>0:
                element = element*self.base
                count -=1
            # overall the multiplication is performed on list1 for 9+80+700 = 789 times
            while element >1:
                resultantList = self.Multiply(list1, resultantList)
                element -= 1 # counting the no of times multiplication is done
            count += 1 # count to keep track of the element's position in number n2
        return resultantList

# Function Description : This function is like main() in Java programming. It takes the input from the user and calls
#                        the processing function to process the input commands one by one.
# Parameter : None
# Pre-condition : None
# Post-condition : None
    def StartOperation(self):
        while 'true' :
            str = raw_input()
            if str == "":
                break
            self.inputCmdsList.append(str)
            self.ProcessInputCmd(str) #parsing the input command

obj = ListOperations()
obj.StartOperation()