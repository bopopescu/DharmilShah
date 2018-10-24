pragma solidity ^0.4.0 ;

contract datatype {
    
    bool demobool = false;
    uint demouint = 255;
    int demoint = 128;
    
    string demostring;
    uint[] mystringarr;
    
    byte demobyte;
    
    enum demo {ADD, REMOVE,UPDATE}
    
    demo dd = demo.ADD;
    
    address public demoadddress ;
    
    function addressfunctionality() public {
        demoadddress = msg.sender;
        demoadddress.balance;
    }
    
    function get() public constant returns(address){
        return demoadddress;
    }
    int[] demoarr = [10,20,30];   // dynamic array size
    
    function arrfunctionality() public
    {
        demoarr.push(40);
        demoarr.length;
        demoarr[1];
    }
    
    int[10] demo_fixedarr;    // fixed array size
    
    struct demoaccount
    {
        uint balance ; 
        uint dailylist;
    }
    
    demoaccount dac;
    
    function structfunctionality() public{
        dac.balance = 10;
    }
    
    mapping (address => demoaccount) _account; 
    function() payable public {
        _account[msg.sender].balance += msg.value;
    }
    
    function getbalance() public returns (uint){
        return _account[msg.sender].balance;
         
    }
    
    
}
