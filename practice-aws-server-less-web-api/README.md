# aws-server-less-web-api-practice

AWS 環境におけるサーバーレス Web API 構築の練習

クライアントから任意の文字列を送るとデータベースに格納され、また、その文字列をクライアントは取得することができる。

## 役割

```txt
Amazon DynamoDB (NoSQL)
｜
AWS Lambda (Python) **本リポジトリの扱う要素**
｜
Amazon API Gateway
｜
ユーザー
```

```mermaid
flowchart
    A[Amazon DynamoDB]-->|データの保存・取得|B[AWS Lambda - Python]
    B-->|API処理|C[Amazon API Gateway]
    C-->|RESTful API|D[ユーザー]
```
