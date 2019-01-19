var Tx = require('ethereumjs-utils')
var Web3 = require('web3')
const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:8545"));
var account = web3.eth.accounts[1]
var msg = '0x5d3bc3d76277df11c764bf4da47361fd1b8cbbb30b12b5e0fbc9033ac1422740';
var signature = web3.eth.sign(account,msg)
const {v,r,s} = Tx.fromRpcSig(signature);
console.log(signature);
console.log("R",r)
console.log("s",s)
console.log("v",v)


//hash for the withdraw function 0xc8f205acb6735e88e050b1e06c3d0d921e52471b =  0x5d3bc3d76277df11c764bf4da47361fd1b8cbbb30b12b5e0fbc9033ac1422740
//R <Buffer 0xe7d5eb8dd51de66b57f726eb8dcfa3fafa692506370d66b06b0386d86fdfd8db>
//s <Buffer 0x322b17888919a3f8ea4c8eed2c96e93608790ee109a2fa658a7c527904b757b7>
//v 28

// order hash of maker account 0x9d3652673614d32e5ee3175d90a592e59202c076 : = 0x7eb3b5cebb7d9acfe56a8cc15b4ebc32045207c17eef97e296fe0f32f547f3d0
//R <Buffer 0x780918678ed3da6d36d49cea0ad3fb6549f21eb0353edff45cc6e5987834bc0e>
//s <Buffer 0x3eb12b4cb57c340c6b02c61a4e2f68e5777edc84bdab33993d22b867d13e1028>
//v 27


//["0x780918678ed3da6d36d49cea0ad3fb6549f21eb0353edff45cc6e5987834bc0e","0x3eb12b4cb57c340c6b02c61a4e2f68e5777edc84bdab33993d22b867d13e1028",
// "0x478a47c3f167e102b2f5d095bab4216138a1b8bb2e0f23420f7c012fa3d3ff2c","0x1362bb1c73350d96df55ac709078a2fac2487fa91904ce38408b7a15819b169a"]


// trade hash of taker account 0x193072c4c771e905b8b036461fac12c037a95078 := 0x3b602cf5b560c21ad91f3ad477e969c5a7626d098e72fdd0b328030be5a46a72
//R <Buffer 0x478a47c3f167e102b2f5d095bab4216138a1b8bb2e0f23420f7c012fa3d3ff2c>
//s <Buffer 0x1362bb1c73350d96df55ac709078a2fac2487fa91904ce38408b7a15819b169a>
//v 28



