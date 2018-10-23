pragma solidity ^0.4.25;

interface data
{
    function stuname(string name) public constant returns(string);
}
contract baseclass is data
{
   
    function stuname(string name) public constant returns(string)
    {
        return name;
    }
}
contract deriveclass is baseclass 
{
    string public clg;
    function getclg(string Clg) public
    {
        clg =Clg;    
    }
    function setclg() public constant returns(string)
    {
        return clg;
    }
   
}
