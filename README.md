# dockerでデータのバッチ処理をしてみる

## 参照サイト
https://marketingengineercareer.com/docker-datafix

## コマンド実行例
- docker compose up -d --build
- docker-compose run python3 ./header_transform_rule.json　<src対象のバケット名> <src対象のファイルパス> <dest対象のバケット名> <dest対象のファイルパス>