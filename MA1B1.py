# MA1B1.py, for basic running and testing. 
# * DO NOT modify this given test file, except the STUDENT INFO part.
# Main Testing Program

from A1B1 import AList

def main():
    print("=== A1B1, Fixed-Sized ArrayList, by <Student NAME> <Student ID> ===\n")
    myL = AList(6)
    print(f"--- 0. new AL <CHECK> isFullL()?:{myL.isFullL()}, isEmptyL()?:{myL.isEmptyL()}")
    myL.displayL()
    
    print(f"--- 1. insertL <ZYXABC>-W?")
    myL.insertL('Z', 1);  myL.insertL('Y', 2);  myL.insertL('X', 3);
    myL.insertL('C', 4);  myL.insertL('B', 4);  myL.insertL('A', 4);  myL.insertL('W', 3);
    myL.displayL()
    
    myL.removeL(5);  myL.removeL(5);
    print("\n--- 2. appendL: <ZYXA,ZA> - B? ")
    myL.appendL('Z');  myL.appendL('A');  myL.appendL('B');
    myL.displayL()
    print(f"\n ------ 3. <CHECK>  searchLastL('Z'), pos:{myL.searchLastL('Z')}")
    
    print(f"\n--- 3.  removeL(myL.searchLastL('Z')), elt:{myL.removeL(myL.searchLastL('Z'))}")
    myL.displayL()
    print(f"------ <CHECK>  searchLastL('Z'), pos:{myL.searchLastL('Z')}")
    print(f"------ <CHECK>  searchLastL('XYZ'), pos:{myL.searchLastL('XYZ')}")
    
    print("\n=== Program ends ===\n")
    
main()
