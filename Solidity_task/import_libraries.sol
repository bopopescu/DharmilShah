pragma solidity ^0.4.25 ;

library demo {
    function inc(int self) public returns (int){
        return self+1;
    }
    function dec(int self) public returns (int){
        return self-1;
    }
    function inc_byvalue(int self, int value) public returns(int)
    {
        return self+value;
    }
    function dec_byvalue(int self, int value) public returns(int)
    {
        return self-value;
    }
}