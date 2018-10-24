pragma solidity ^0.4 ;

library Strings {
    function concat(string _base, string _value) public constant returns (string){
        bytes memory _basebytes = bytes(_base);
        bytes memory _valuebytes = bytes(_value);
        
        string memory _tmpvalue = new string(_basebytes.length + _valuebytes.length);
        
        bytes memory _newvalue = bytes(_tmpvalue);
        
        uint i;
        uint j;
        
        for(i=0;i<_basebytes.length;i++)
        {
            _newvalue[j++]= _basebytes[i];
        }
        
        for(i=0;i<_valuebytes.length;i++)
        {
            _newvalue[j++]= _valuebytes[i];
        }
        return string(_newvalue);
        
       
    }
     function strpos(string _base, string _value)public constant returns (int)
        {
            bytes memory _basebytes = bytes(_base);
            bytes memory _valuebytes = bytes(_value);
            
            assert(_valuebytes.length == 1);
            
            for (uint i=0; i< _basebytes.length; i++){
                if(_basebytes[i] == _valuebytes[0]){
                    return int(i);
            }
        }
        return -1;
        }
        
        
}


