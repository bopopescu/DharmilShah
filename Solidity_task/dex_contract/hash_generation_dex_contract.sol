pragma solidity ^0.4.25;
contract order {
    
    address contractaddress = 0xd95faef9eed84fe32284f404d6ca8269fb5a21a4;
    address tokenaddress = 0x93f136820df4c5b7c98244a0b31a865de3570642;
    function orderH(uint256[8] tradeValues, address[4] tradeAddresses) public constant  returns(bytes32,bytes32){
    bytes32 orderHash = keccak256(abi.encodePacked(contractaddress, tradeAddresses[0], tradeValues[0], tradeAddresses[1], tradeValues[1], tradeValues[2], tradeValues[3], tradeAddresses[2]));
    bytes32 tradeHash = keccak256(abi.encodePacked(orderHash, tradeValues[4], tradeAddresses[3], tradeValues[5]));
    return (orderHash,tradeHash);
    }
    
    function ecr(bytes32 msgHash, uint8 v, bytes32 r, bytes32 s) public pure returns(address)
    {
        return ecrecover(keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", msgHash)), v, r, s);
    }
    
    function withdrawhash(uint256 amount, address user, uint256 nonce) public constant returns(bytes32){
        bytes32 hash = keccak256(abi.encodePacked(contractaddress, tokenaddress, amount, user, nonce));
        return(hash);
    }
}