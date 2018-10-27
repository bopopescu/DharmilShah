pragma solidity 0.4;


interface erc20 {
    
    function totalSupply() external view returns (uint _totalsupply); 
    function balanceOf(address owner)external view returns (uint balance);
    function transfer(address _to, uint _value)external  returns (bool success);
    function allowance(address _owner, address _spender) external view returns (uint remaining);
    function transferFrom(address _from, address _to, uint _value) external view returns (bool success);
    function approve(address _spender, uint _value) external view returns (bool success);
    // event Approval(address indexed _owner, address indexed _spender, uint _value);
    // event Transfer(address indexed _from, address indexed _to, uint _value);
}