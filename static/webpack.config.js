var path = require("path")
var webpack = require('webpack')

module.exports = {
  context: __dirname,

  entry: {
    // Add as many entry points as you have container-react-components here
    home: './react/modules/Home/index',
    vendors: ['react'],
  },

  output: {
      path: path.resolve('./build/bundles/local/'),
      filename: "[name].js"
  },
  
  node: {
    fs: "empty"
  },

  externals: [
  ], // add all vendor libs

  plugins: [
    new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
  ], // add all common plugins here

  module: {
    loaders: [ 
      { test: /\.json$/, loader: "json-loader"},
      { test: /\.js$/, loader: 'babel-loader'}
    ] // add all common loaders here
  },

  resolve: {
    alias: {
      'react': path.join(__dirname, 'node_modules', 'react')
    },
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx', '.json']
  },
}