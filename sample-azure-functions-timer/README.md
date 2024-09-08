# azure-functions-timer-sample

公開用：Azure Functions で Timer トリガーベースの関数を作成するサンプルリポジトリ

## 内容

この関数アプリは、1 分ごとにロギングする機能を持っています。

```py
│  .funcignore # Azure Functionsで無視するファイルやディレクトリを指定
│  .gitignore # gitで無視するファイルやディレクトリを指定
│  host.json # Azure Functionsのグローバル設定を定義
│  LICENSE # プロジェクトのライセンス情報
│  local.settings.json # ローカル開発時の設定を定義
│  README.md # プロジェクトの説明書き（README）
│  requirements.txt # Pythonプロジェクトの依存関係をリストアップ
│
├─.github # GitHub固有の設定ファイルを格納するディレクトリ
│  └─workflows # GitHub Actionsのワークフローを定義
│          main-azure-functions-app.yml # 主要なAzure FunctionsアプリのCI/CD設定
│
├─.vscode # Visual Studio Code固有の設定ファイルを格納するディレクトリ
│      extensions.json # 推奨するVS Code拡張機能
│      launch.json # デバッグ設定
│      settings.json # VS Codeの設定
│      tasks.json # タスクランナー設定
│
└─example # "example" という名前のAzure Functions関数を格納するディレクトリ
        function.json # 関数のバインディングと設定を定義
        __init__.py # 関数の本体（Pythonコード）
```
