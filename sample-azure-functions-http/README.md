# azure-functions-http-sample

公開用：Azure Functions で HTTP トリガーベースの関数を作成するサンプルリポジトリ

## 内容

ルート URL にアクセスしたときに、メッセージを返す関数アプリが含まれています。

```py
│  .funcignore                - Azure Functionsのデプロイ時に無視するファイルやディレクトリを指定
│  .gitignore                 - Gitバージョン管理から除外するファイルやディレクトリを指定
│  function_app.py            - Azure Functionsアプリケーションのメインコード
│  host.json                  - Azure Functionsのホスト設定を記述
│  LICENSE                    - プロジェクトのライセンス情報
│  local.settings.json        - ローカル開発用の設定ファイル
│  README.md                  - プロジェクトの説明や使い方を記載
│  requirements.txt           - プロジェクトに必要なPythonパッケージを記載
|
├─.github                     - GitHub関連の設定やワークフローファイルを格納
│  └─workflows
│          azure-functions-app-python.yml - GitHub Actionsのワークフロー設定、Azure Functionsへの自動デプロイなどを定義
|
├─.vscode                     - Visual Studio Codeの設定ファイルを格納
│      extensions.json        - 推奨するVS Code拡張機能を指定
│      launch.json            - デバッグ設定
│      settings.json          - VS Codeのプロジェクト固有の設定
│      tasks.json             - VS Codeのタスクランナー設定
|
└─src                         - ソースコードを格納するディレクトリ
        __init__.py            - Pythonパッケージの初期化ファイル
```
