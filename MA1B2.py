# MA1B2.py, for basic running and testing. 
# * DO NOT modify this given test file, except the STUDENT INFO part.
# Main Testing Program

from A1B2 import DLList

def main():
    print("=== === A1B2, DLList program, by <Student NAME> <Student ID>===")

    myL = DLList()   
    myL.appendDL(11); myL.appendDL(22); myL.appendDL(33)
    myL.appendDL(55); myL.appendDL(77); myL.appendDL(99)
    print("\n--- 1. List with Insert items <11,22,33,55,77,99>---")
    myL.displayBwDL()
    myL.displayDL()   
    print(f" ------ <CHECK>  getNextFwDL(55), elt:{myL.getNextFwDL(55)}")
    print(f" ------ <CHECK>  getPrevBwDL(55), elt:{myL.getPrevBwDL(55)}")

    print(f"\n ------2. <CHECK>  removePrevBwDLBw(55), elt:{myL.removePrevBwDL(55)}")
    myL.displayDL()
    myL.displayBwDL()
    
    print("\n=== Program ends ===\n")

main()
