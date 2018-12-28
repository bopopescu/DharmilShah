module.exports = {
  networks: {
    development: {          //here development refers to the network name 
      host: "localhost",    // 
      port: 8545,
      network_id: "*" // Match any network id
    }
  }
};

/* 
module.exports = {
networks:{               // if we want to use network rinkeby then remove development parameter and in the console type truffle migrate --network rinkeby 
  live:{                 // live is used to deploy contract on any port rather then default rpc port
    host: "localhost",
    port: 9545,
    network_id: 1,
    gas: 10000, gasPrice: 10,
    from: from account address
  }
}
}
*/