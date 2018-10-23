pragma solidity ^0.4.25;

import "browser/imports_libraries.sol";

contract testlibraries {

    using demo for *;     //using keyword is used to use library of imports_libraries file
    
    function testincrement(int base) returns (int)
    {
        return base.inc();
    }
    function testdecrement(int base) returns (int)
    {
        return base.dec();
    }
    function testincrementbyvalue(int base, int valu2) returns (int)
    {
        return base.inc_byvalue(valu2);
    }
    function testdecrementbyvalue(int base, int valu2) returns (int)
    {
        return base.dec_byvalue(valu2);
    }
}


