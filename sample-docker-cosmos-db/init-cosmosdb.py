import time
from azure.cosmos import CosmosClient, PartitionKey

# Cosmos DB Emulatorの接続情報
endpoint = "https://azurecosmosemulator:8081"
key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="

# データベース名とコンテナ名
database_name = "mydb"
container_name = "mycontainer"

# クライアントの初期化
client = CosmosClient(endpoint, key, connection_verify=False)


def wait_for_emulator():
    while True:
        try:
            # データベースのリストを取得してみる
            client.list_databases()
            print("Cosmos DB Emulator is ready.")
            break
        except Exception as e:
            print("Waiting for Cosmos DB Emulator to start...")
            time.sleep(5)


def create_database_and_container():
    # データベースを作成
    database = client.create_database_if_not_exists(id=database_name)
    print(f"Database '{database_name}' created or already exists.")

    # コンテナを作成
    container = database.create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path="/id"), offer_throughput=400)
    print(f"Container '{container_name}' created or already exists.")

    return container


def add_sample_items(container):
    # サンプルアイテムを追加
    items = [{"id": "1", "name": "Item 1", "description": "This is item 1"}, {"id": "2", "name": "Item 2", "description": "This is item 2"}, {"id": "3", "name": "Item 3", "description": "This is item 3"}]

    for item in items:
        container.create_item(body=item)
        print(f"Item {item['id']} added.")


if __name__ == "__main__":
    wait_for_emulator()
    container = create_database_and_container()
    add_sample_items(container)
    print("Initialization completed.")
