pragma solidity ^0.4.25;

contract calc {
    
    int public val1;
    int public val2;
    int public add_result;
    int public sub_result;
    int public mul_result;
    int public div_result;
    int public mod_result;
    
    function setdata(int v1, int v2) public {
        val1 = v1 ;
        val2 = v2 ;
        //add_result = ares;
        add_result = val1 + val2;
        sub_result = val1 - val2;
        mul_result = val1 * val2;
        div_result = val1 / val2;
        mod_result = val1 % val2;
    }
    
    function getadddata() public returns (int){
        return (add_result);
    }
    
    function getsubdata() public returns(int){
        return (sub_result);
    }
    function getmuldata() public returns(int){
        return (mul_result);
    }
    function getdivdata() public returns(int){
        return (div_result);
    }
    function getmoddata() public returns(int){
        return (mod_result);
    }
    
}