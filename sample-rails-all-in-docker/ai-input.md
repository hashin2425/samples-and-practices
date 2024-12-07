# アプリ作成の指示書

## このアプリの目的

このアプリケーションの目的は、一般的な Web アプリとして実装されうる機能についてサンプルコードを作成し、実行可能な状態にすることである。

したがって、コードには日本語でコメントを残し、再利用時に役に立つようにしなければならない。

テーマとして、ショッピングサイトを想定している。

## 技術選定

技術選定として指定するものは以下の通りである。ここで指定されていないものは適切に選定せよ。

- Ruby
- Ruby on Rails
- React
- Tailwind CSS
- docker
- MySQL
- Redis
- Grafana
- Nginx

Rails と React の連携は`react-rails`という Gem を用いること。また、Rails のフロントエンドは Slim テンプレート言語を用いること。

ミドルウェア（MySQL, Redis, Grafana）も Rails アプリもすべて docker-compose によって起動する。ローカル上のコードを docker コンテナーにマウントし、Rails アプリのコードを変更した際にその変更が即座に反映される機能（ホットリロード）が有効になっていなければならない。

## データベース構造

### MySQL

- 商品データベース
  - 商品 ID：文字列・プライマリキー・重複を認めない
  - 商品名：文字列
  - 商品説明文：文字列
  - 在庫数：整数値
  - 価格：整数値
- ユーザーデータベース
  - ユーザー ID：文字列・プライマリキー・重複を認めない
  - パスワード：文字列・ハッシュ化されている
  - （その他ソルトなどが必要であれば格納する）

### Redis

- 商品カートデータベース
  - キー：商品 ID
  - バリュー：ユーザー ID を持つハッシュテーブル（Set 型）のデータ

## 実装する Web ページ

- /
  - これはトップ画面・ホームページに該当するページである。
  - これ以外のページにアクセスするためのリンクが列挙されている。
- /query-items/
  - 商品一覧から絞り込み検索などができるページである。
  - 価格や商品名によって検索・絞り込みが可能である。
  - これはすべてのユーザーが利用可能である。
- /show-item/{item_id}
  - 商品の詳細情報を閲覧できるページである。
  - MySQL から取得される商品の情報が表示される。
  - ユーザーは商品を「カートに入れる」ことができる
  - Redis に保存されている「カートに入れているユーザー数」も表示される
  - すべてのユーザーが閲覧可能であるが、カートに追加することはログイン済みユーザーが使える機能である。
- /login/
  - 作成済みのアカウントにログインするためのページである。
  - ID とパスワードを用いてログインを行うことができる。
- /create-account/
  - アカウントを新規作成するためのページである。
  - ID・パスワード・パスワード再入力を入力フォームとして持ち、バックエンドのみで「ID が既存の ID を重複しないこと」と「パスワードと再入力されたパスワードが一致していること」をバリデーションする。
- /my-account/
  - ユーザーが自身のアカウントについて、ユーザー情報を閲覧・編集できるページである。
  - 編集可能なユーザー情報はパスワードのみである。

## 実装する機能

- ログ取得
  - ログは標準出力に表示され、また、Json ファイルでローカル上に保存される必要がある。
- CSRF 対策や XSS 対策を必要に応じて導入する
- セッション管理は JWT ベースで行う

## ディレクトリ構造

```md
shopping-app/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── custom.md
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml
│       ├── deploy.yml
│       └── dependency-updates.yml
├── .gitignore
├── .env-sample
├── .rubocop.yml
├── .eslintrc.js
├── .stylelintrc.js
├── docker-compose.yml
├── Makefile
├── README.md
├── docker/
│   ├── app/
│   │   ├── Dockerfile
│   │   └── entrypoint.sh
│   ├── mysql/
│   │   ├── Dockerfile
│   │   ├── my.cnf
│   │   └── init.sql
│   ├── nginx/
│   │   ├── Dockerfile
│   │   └── default.conf
│   ├── redis/
│   │   ├── Dockerfile
│   │   └── redis.conf
│   └── grafana/
│       ├── Dockerfile
│       └── provisioning/
│           ├── dashboards/
│           │   └── dashboard.yml
│           └── datasources/
│               └── datasource.yml
└── src/
    ├── Gemfile
    ├── Gemfile.lock
    ├── Rakefile
    ├── package.json
    ├── yarn.lock
    ├── .browserslistrc
    ├── babel.config.js
    ├── postcss.config.js
    ├── app/
    │   ├── assets/
    │   │   ├── images/
    │   │   └── stylesheets/
    │   │       ├── application.tailwind.css
    │   │       └── components/
    │   ├── controllers/
    │   │   ├── api/
    │   │   │   └── v1/
    │   │   │       ├── auth_controller.rb
    │   │   │       ├── items_controller.rb
    │   │   │       └── cart_controller.rb
    │   │   └── web/
    │   │       ├── home_controller.rb
    │   │       ├── sessions_controller.rb
    │   │       └── users_controller.rb
    │   ├── javascript/
    │   │   ├── components/
    │   │   │   ├── common/
    │   │   │   ├── items/
    │   │   │   ├── cart/
    │   │   │   └── auth/
    │   │   ├── pages/
    │   │   ├── services/
    │   │   │   ├── api/
    │   │   │   └── auth/
    │   │   ├── hooks/
    │   │   ├── contexts/
    │   │   ├── types/
    │   │   └── utils/
    │   ├── models/
    │   │   ├── concerns/
    │   │   │   ├── tokenizable.rb
    │   │   │   └── searchable.rb
    │   │   ├── validators/
    │   │   ├── item.rb
    │   │   └── user.rb
    │   ├── services/
    │   │   ├── cart/
    │   │   │   ├── add_item_service.rb
    │   │   │   └── remove_item_service.rb
    │   │   └── auth/
    │   │       ├── jwt_service.rb
    │   │       └── password_service.rb
    │   ├── views/
    │   │   ├── layouts/
    │   │   │   └── application.html.slim
    │   │   └── pages/
    │   │       ├── home/
    │   │       ├── items/
    │   │       └── users/
    │   └── helpers/
    ├── config/
    │   ├── environments/
    │   │   ├── development.rb
    │   │   ├── production.rb
    │   │   └── test.rb
    │   ├── initializers/
    │   │   ├── cors.rb
    │   │   ├── redis.rb
    │   │   └── session_store.rb
    │   ├── locales/
    │   │   ├── en.yml
    │   │   └── ja.yml
    │   ├── database.yml
    │   ├── routes.rb
    │   ├── application.rb
    │   └── credentials.yml.enc
    ├── db/
    │   ├── migrate/
    │   │   ├── 20240101000000_create_users.rb
    │   │   └── 20240101000001_create_items.rb
    │   ├── schema.rb
    │   └── seeds/
    │       ├── development/
    │       └── production/
    ├── lib/
    │   ├── tasks/
    │   │   └── custom_tasks.rake
    │   └── utils/
    │       └── logger.rb
    ├── log/
    ├── public/
    ├── spec/
    │   ├── factories/
    │   ├── models/
    │   ├── requests/
    │   │   ├── api/
    │   │   └── web/
    │   ├── system/
    │   ├── support/
    │   │   ├── capybara.rb
    │   │   └── factory_bot.rb
    │   └── rails_helper.rb
    ├── storage/
    ├── tmp/
    └── vendor/
```

## プロジェクト作成時のコマンド

```sh
rails new src --database=mysql --skip-action-mailbox --skip-action-text --skip-spring --skip-listen --skip-system-test --javascript=webpack --css=tailwind --template-engine=slim --skip-bundle
```

## その他

- コードの生成や実装時にはベストプラクティスにしたがって作成を行うこと。
- コードの生成時にはディレクトリ構成を必ず示してからコードを生成せよ。
- 必要な環境変数をリストアップし、それを`.env`ファイルや`.env-sample`ファイルなどに記述せよ。
- 必要に応じてテストコードを導入せよ
