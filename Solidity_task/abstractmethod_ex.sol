pragma solidity ^0.4.25;

contract baseclass {
    int internal value ;
    constructor(int amount) {
        value = amount;
    }
    function deposit(int amount) 
    {
        value = value + amount;
    }
    function withdraw(int amount)
    {
        value -= amount;
    }
    function balance()  returns (int)
    {
        return value;
    }
    function loan() returns (bool); // abstract method  declared
}

contract deriveclass is baseclass(4000) {
    // is keyword used to use functionality of the baseclass
    
    string internal name;
    int internal age;
    
    function setname(string Name)  {
        name = Name;
    }
    function getname()  returns (string)
    {
        return name ;
    }
    function setage(int Age) {
        age = Age;
    }
    function getage()  returns (int)
    {
        return age ;
    }
    function  loan() returns(bool)   //  abstract method defination
    {
        return true;
    }
    
}
