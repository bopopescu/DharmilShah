pragma solidity ^0.4.25 ;
 
contract Test {
    string public name ;
    int public age ;
    
    function setdata(string Name, int Age) public{
        name = Name;
        age = Age;
    }
    function getdata() public returns(string, int){
        return(name, age);
    }
    
}