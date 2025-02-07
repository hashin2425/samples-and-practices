# 環境構築の方法

## 実行環境を用意する

LinuxマシンかWSL環境で開発する。

```sh
sudo apt-get update
sudo apt-get upgrade
```

## Rubyのインストール

Rubyのバージョン管理システムとして、rbenvを利用する。
Rubyのバージョンは<https://www.ruby-lang.org/ja/downloads/>に最新の安定版バージョンが示されている。

```sh
# dependency
sudo apt update
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev

# rbenv
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc

# ruby-build
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build

# ここで再起動をさせる
exit

rbenv install 3.4.1
rbenv rehash
rbenv global 3.4.1
ruby -v
```

## Railsのインストール

<https://rubygems.org/gems/rails>

```sh
gem install rails -v 8.0.1
rails -v
```

## Nodeのインストール

Node.jsのインストールには、バージョン管理システムであるNVMを利用する。
インストール方法は<https://github.com/nvm-sh/nvm#install--update-script>に記載されている。

```sh
# NVM
sudo apt update && sudo apt install curl build-essential
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# 再起動させる
exit

# NodeJS
nvm install --lts
nvm use --lts
nvm current
node -v
```

## NPMのインストール

```sh
```

## Docekr-composeのインストール

```sh
```

## Gemのインストール

```sh
```
