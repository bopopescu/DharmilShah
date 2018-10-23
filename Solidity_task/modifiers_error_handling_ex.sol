pragma solidity ^0.4.25;

interface myinterface 
{
    function checkvalue(int amount) returns (bool);
    function loan() returns (bool);
}

contract baseclass is myinterface { // to implement interface is keyword required
    int internal value ;
    address private owner;
    
    modifier ownerfunc {
        require(owner == msg.sender);
        _;
    }
    function testthrow()
    {
        throw;
    }
    constructor(int amount) {
        value = amount;
        owner  = msg.sender; 
    }
    function deposit(int amount) ownerfunc
    {
        value = value + amount;
    }
    function withdraw(int amount) ownerfunc
    {
        if(checkvalue(amount))
        {
            value -= amount;    
        }
        
    }
    function balance()  returns (int)
    {
        return value;
    }
    function  loan() returns(bool)   
    {
        return value > 0;
    }
    function checkvalue(int amount) returns(bool)
    {
        return amount >= value;
    }   
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
}
contract TestThrows
{
    function testassert(){
        assert(1 == 2);
    }
    function testrequire(){
        require (2 == 1);
    }
    function testrevert(){
        revert();  
    }
    function testthrow(){
        throw;
    }
}




