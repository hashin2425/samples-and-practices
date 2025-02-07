import redis

# Redisサーバーに接続
r = redis.Redis(host="localhost", port=6379, db=0)


def write_data(key, value):
    """データをRedisに書き込む"""
    r.set(key, value)
    print(f"書き込み成功: {key} = {value}")


def read_data(key):
    """Redisからデータを読み取る"""
    value = r.get(key)
    if value:
        return value.decode("utf-8")
    else:
        return None


def get_all_keys():
    """全てのキーを取得"""
    return [key.decode("utf-8") for key in r.keys("*")]


def delete_data(key):
    """データを削除"""
    if r.delete(key):
        print(f"削除成功: {key}")
    else:
        print(f"キーが見つかりません: {key}")


# 使用例
if __name__ == "__main__":
    # データの書き込み
    write_data("user:1", "Alice")
    write_data("user:2", "Bob")
    write_data("count", "10")

    # データの読み取り
    print("user:1 =", read_data("user:1"))
    print("user:2 =", read_data("user:2"))
    print("count =", read_data("count"))

    # 全てのキーを取得
    print("全てのキー:", get_all_keys())

    # データの削除
    delete_data("user:2")

    # 削除後の全てのキーを確認
    print("削除後の全てのキー:", get_all_keys())

    # 存在しないキーの読み取り
    print("存在しないキー:", read_data("nonexistent"))
