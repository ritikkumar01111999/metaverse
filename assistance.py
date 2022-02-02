#######importing the inbuilt module#########


import first_code as fc
import sum
import mul
import divide
import substract

def creden():    
    question=input('enter your question here:-').lower()
    question_for_test=question.split()  
    #print(question_for_test)
    return question_for_test
    
def check_start(credential):
        for i in credential:
            if "sum" in i:
                print("########### you are ready to jump feel free #############")
                fc.sum()
                sum.activate_drill()
            if "add" in i:
                print("########### you are ready to jump feel free #############")
                fc.sum()
                sum.activate_drill()
            if "sub" in i:
                print("########### you are ready to jump feel free #############")
                fc.sub()
                substract.activate_drill()
            if "substract" in i:
                print("########### you are ready to jump feel free #############")
                fc.sub()
                substract.activate_drill()
            if "mul" in i:
                print("########### you are ready to jump feel free #############")
                fc.mul()
                mul.activate_drill()
            if "multiply" in i:
                print("########### you are ready to jump feel free #############")
                fc.mul()
                mul.activate_drill()
            if "div" in i:
                print("########### you are ready to jump feel free #############")
                fc.divi()
                divide.activate_drill()
            if "divide" in i:
                print("########### you are ready to jump feel free #############")
                fc.divi()
                divide.activate_drill()
            
        
#################  activating functions   ##############
if __name__=="__main__":
    credential=creden()
    check_start_function=check_start(credential)
    
    