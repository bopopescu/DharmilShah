pragma solidity ^0.4;

import "browser/strings.sol";


contract teststrings {

    using Strings for string;
    function testconcat(string _base)public constant returns(string)
    {
        return _base.concat("_suffix");
    }
    
    function stringpos(string _base)public constant returns (int){
        return _base.strpos("t");
    }
    
}