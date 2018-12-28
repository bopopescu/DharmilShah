const d = artifacts.require("MyStringStore");

module.exports = function(deployer) {
  deployer.deploy(d);
};