const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: 'production',
  entry: './gpt/static/scss/style.scss',
  output: {
    path: path.resolve(__dirname, 'gpt/static/css'),
    filename: 'bundle.[contenthash].js' // Utilisez un nom de fichier différent pour le fichier JavaScript
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader'
        ]
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'style.css' // Spécifiez le nom de fichier souhaité pour le fichier CSS
    })
  ],
  devtool: 'source-map'
};