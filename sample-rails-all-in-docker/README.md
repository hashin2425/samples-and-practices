# sample-rails-all-in-docker

Webアプリケーションとして使うであろう機能をすべて実装したものを作る

ミドルウェアもdocker-composeで起動できるようにする

## connect to mysql

<https://github.com/hashin2425/samples-and-practices/commit/47ddb04df55541b8ae20c7e307eea657150444b4>

## add Grafana, Nginx

<https://github.com/hashin2425/samples-and-practices/commit/d81e484fdd844efd9c65b9968a9b4a44d85de8e5>

## add homepage

```sh
docker-compose exec app rails g controller web/home index
```
