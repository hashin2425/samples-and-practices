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

### Edit package.json

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
bundle add 'react-rails' --strict
rails generate react:install

rails g react:component HelloWorld greeting:string
rails g react:component my_subdirectory/HelloWorld greeting:string
```

## init typescript

```sh
npm install typescript @babel/preset-typescript
npm install fork-ts-checker-webpack-plugin
```

### Add `tsconfig.json` file

```json
{
    "compilerOptions": {
        "declaration": false,
        "emitDecoratorMetadata": true,
        "experimentalDecorators": true,
        "lib": [
            "es6",
            "dom"
        ],
        "module": "es6",
        "moduleResolution": "node",
        "sourceMap": true,
        "target": "es5",
        "jsx": "react",
        "noEmit": true
    },
    "exclude": [
        "**/*.spec.ts",
        "node_modules",
        "vendor",
        "public"
    ],
    "compileOnSave": false
}
```

### Edit `config/application.rb`

```rb
module TestApp
  class Application < Rails::Application
    # add this line
    config.react.server_renderer_extensions = ["jsx", "js", "tsx", "ts"]
  end
end

```

### Edit `config/shakapacker.yml`

```yml
default: &default
  # add this
  extensions:
    - .js
    - .jsx
    - .ts
    - .tsx
    - .css
    - .scss
    - .sass
    - .less

```

### Edit `config/webpack/webpack.config.js`

```js
const { generateWebpackConfig, merge } = require('shakapacker')
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');

const webpackConfig = generateWebpackConfig()

module.exports = merge(
  webpackConfig, {
    plugins: [new ForkTsCheckerWebpackPlugin()]
  }
);
```

## Add page

```sh
rails generate controller Welcome index
```

### Add `route.rb`

```rb
get "/" => "welcome#index"
```

### Edit `app/view/welcome/index.html.erb`

```html
# add this
<%= react_component("HelloWorld", { greeting: "Hello from react-rails.", info: { name: "react-rails" } }, { class: "hello-world" }) %>
```

you can change js to tsx: app\javascript\components\HelloWorld.tsx
