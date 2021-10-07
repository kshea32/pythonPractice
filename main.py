# This entrypoint file to be used in development. Start by reading README.md


from pytest import main

from arithmetic_arranger import arithmetic_arranger

FirstTest = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

Test1 = arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)

Test2 = arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])

Test3 = arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])

Test4 = arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])

Test5 = arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'], True)

Test6 = arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])

Test7 = arithmetic_arranger(['3801 - 2', '123 + 49'])

Test8 = arithmetic_arranger(['1 + 2', '1 - 9380'])

print("First Test: ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True" + "\n" +  FirstTest + "\n" +"Test 1: ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True" + "\n" +  Test1 + "\n" + "Test 2: ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']"+ "\n"  + Test2 + "\n" + "Test 3:['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']"   + "\n"  + Test3 + "\n" + "Test 4:['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']"   + "\n"  + Test4 + "\n" + "Test 5:['3 / 855', '3801 - 2', '45 + 43', '123 + 49']"   + "\n"  + Test5 + "\n" + "Test 6:['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']"   + "\n"  + Test6 + "\n" + "Test 7:['3801 - 2', '123 + 49']"   + "\n"  + Test7 + "\n" + "Test 8:['1 + 2', '1 - 9380']"   + "\n"  + Test8 + "\n")


main()

