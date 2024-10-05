# project init commands

<https://github.com/reactjs/react-rails/blob/master/docs/get-started.md>

## version checks

```sh
ruby -v
# ruby 3.3.4 (2024-07-09 revision be1089c8ec) [x64-mingw-ucrt]
rails -v
# Rails 7.2.1
node -v
# v20.12.0
```

## init rails

```sh
rails new test-app --skip-javascript
```

## install react

```sh
cd test-app

bundle add shakapacker --strict
bundle install # 管理者権限が必要
rails shakapacker:install

npm install react react-dom @babel/preset-react prop-types css-loader style-loader mini-css-extract-plugin css-minimizer-webpack-plugin
```

Edit package.json

```diff
"babel": {
  "presets": [
-   "./node_modules/shakapacker/package/babel/preset.js"
+   "./node_modules/shakapacker/package/babel/preset.js",
+   "@babel/preset-react"
  ]
},
```

```sh
rails g react:component HelloWorld greeting:string
rails g react:component my_subdirectory/HelloWorld greeting:string
```

## init typescript

```sh
npm install typescript @babel/preset-typescript
npm install fork-ts-checker-webpack-plugin
```
