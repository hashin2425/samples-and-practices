#!/bin/bash
set -e

# Railsサーバー起動前の準備
rm -f tmp/pids/server.pid
bundle install
yarn install
bundle exec rails db:create db:migrate

# Railsサーバーの起動
bundle exec rails server -p 3000 -b '0.0.0.0'