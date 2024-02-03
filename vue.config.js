const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  devServer: {
    port: 8406,
  },
  transpileDependencies: true,
});
