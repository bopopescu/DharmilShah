pragma solidity 0.4.25;

contract Transaction {
    event senderlogger(address);
    event valuelogger(uint);
    
    address private owner;
    
    modifier isowner {
        require(owner == msg.sender);
        _;
    }
    
    modifier validvalue {
        assert(msg.value >= 1 ether);
        _;
    }
    
    
    function Transaction()
    {
        owner = msg.sender;
    }

    function() payable isowner validvalue {
        emit senderlogger(msg.sender);
        emit valuelogger(msg.value);
        
        
    }
}