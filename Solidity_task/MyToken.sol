pragma solidity ^0.4;

import "browser/erc20testing.sol";

contract myfirsttoken is erc20 {
   
    string public constant symbol = "MFT";
    string public constant name = "My First Token";
    uint public constant decimals  = 18;
    
    uint private constant __totalsupply = 100000000000000000; 
    mapping (address => uint) private __balanceof;    
    mapping (address => mapping(address => uint)) private __allowances;
    
    constructor() public {
        __balanceof[msg.sender] = __totalsupply; 
    }
    
    function totalSupply() external constant returns (uint _totalsupply){
        _totalsupply = __totalsupply;
    }
    
    function balanceOf(address _owner)public view returns (uint balance){
        return __balanceof[_owner];
    }
    
    function transfer(address _to, uint _value) external  returns(bool success){
        if(_value > 0 && _value <= balanceOf(msg.sender)){
         __balanceof[msg.sender] -= _value;
         __balanceof[_to] += _value;
         return true;
        }
        return false;
    }
    
    function transferFrom(address _from, address _to, uint _value) public returns (bool success){
        if (__allowances[_from][msg.sender] > 0 
            && _value > 0 
            && __allowances[_from][msg.sender] >= _value &&
            __balanceof[_from] >= _value ){
                __balanceof[_from] -= _value;
                __balanceof[_to] += _value;
                __allowances[_from][msg.sender] -= _value;
                return true;
            }
        return false;     
    }
    function allowance(address _owner, address _spender) public view returns (uint remaining)
    {
        return __allowances[_owner][_spender];
        
    }
    function approve(address _spender, uint _value) public returns (bool success)
    {
        
        __allowances[msg.sender][_spender] = _value;
        return true;
    }
}
