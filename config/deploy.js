/* jshint node: true */

module.exports = function(deployTarget) {
  var ENV = {
    build: {
    },
    s3: {
      bucket: 'imtapps-ember-test',
      region: 'us-east-1',
      accessKeyId: 'fake',
      secretAccessKey: 'fake',
    }
  };

  return ENV;
};
