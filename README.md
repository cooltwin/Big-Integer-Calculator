# Big-Integer-Calculator
This project enables addition, subtraction, multiplication and computing power of large integers eg :- 124678964 ^ 2563943. 

INPUT AND OUTPUT 

The project uses the concept of infix to postfix conversion of an input string. It pushes any variable that it encounters while parsing the string and pops the variable whenever it encounters a operand +,-,*,^,?,= .

In case if it encounters an “=”, it checks if the token next to “=” is a no or variabe. If it’s a no, pop the variable from the stack and convert the no to a string and assign it to the variable ( by putting it in a dictionary of variable to list mapping named as varToListDict in the code). On the other hand if it’s a variable push it to the stack.

Now when it encounters a +,-,*,^ it pops the first operand from the stack and finds its corresponding list and since the second operand is not yet pushed to the stack so it takes it directly from the input string and finds the corresponding list of it. Now it has got both so it performs the desired operation by calling the respective functions.

If it encounters a "?" , means it should loop back from certain line no mentioned in the input command (kind of looping command). For the same reasons it reads the lineno from the input string ( input statement). Inorder to loop back I have maintained a list of input statements prior to the processing of the input statements and inserted them to this list. Now that we have the input statement list we can loop the lineno in a recursive manner going line by line.

If it encounters a command of type “var” it means that it should print the variable. So as I have explained earlier whenever the algorithm encounters a variable it pushes it to a variable stack(named varStack in the code). At the end of the processing function I am checking if the stack still has any variable if so then print the list corresponding to this variable ( Because in the other cases I
have poped out the variables while computing them. So no other variables except the assignment ones will be in the stack).

-----------------------------------------------------------------------------------------------------------------------------
HOW THE SYSTEM WORKS

Add operation – Addition is simply adding each element of both the list in reverse order and take care of carry and keep adding the previous stage carry to next stage. Also at the end append the carry to the resultant list.

Subtract - Subtraction implementation in tricky when borrows are taken. Whenever a borrow is taken update the next element from whom we have lended. Meanwhile also check if the lending element is not zero because if we lend from such an element then it goes to -1 which is wrong . So I have put a check for eligible lenders ( i.e checking if the lender is non zero). Also if the borrowing elemnt is the last element of the list ( i.e msb of n1, since the list here stores the number n1 in reverse order) then the result is going to be negative so return 0 instead. I have also made a prior check for negative results by comparing the length of the two lists representing the number. If length of list1(n1) is lesser than length of list2(n2) means n1<n2 and n1-n2<0 so return 0 instead.

Multiply – Its implementation involves multiplying each element of list2 to all elements of list1 and subsequently adding the output of each multiplication stage. This is done by multiplying one level and then calling add() to add the level with the previous levels.

Power – It’s a repeated multiplication to itself. So I am calling multiplication inside in this function as n2 times( if its n1^n2). The challenge here is n2 is too large how do we run the loop n2 times without converting n2 from string to an integer or from list to an integer. So Here is what I did – multiply each element of list2 with its position value suppose the no is 78925, so list2 represents it as 5->2->9->8->7 , so the loop runs 5*1 + 2*10+9*100+8*1000+7*10000 = 78925. It’s like when we encounters the first element of list2 (i.e 5) run loop 5*1 times next when it encounters the second element 2 it runs the loop 2*10 times and next time 9*100 times and so on ….
