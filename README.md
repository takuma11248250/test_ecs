# dockerでデータのバッチ処理をしてみる

## 参照サイト
https://marketingengineercareer.com/docker-datafix  
https://marketingengineercareer.com/ecs-datafix

## コマンド実行例
### ローカルdocker環境
- docker compose up -d --build
- docker-compose run python3 ./header_transform_rule.json　<src対象のバケット名> <src対象のファイルパス> <dest対象のバケット名> <dest対象のファイルパス>

### AWS ECS
- aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin <アカウントID>.dkr.ecr.ap-northeast-1.amazonaws.com
- docker compose up -d --build
- docker tag test_ecs/python3:latest <アカウントID>.dkr.ecr.ap-northeast-1.amazonaws.com/test_ecs/python3:latest
- docker push <アカウントID>.dkr.ecr.ap-northeast-1.amazonaws.com/test_ecs/python3:latest
- aws ecs run-task --cluster test-ecs --task-definition test-ecs --overrides '{"containerOverrides": [{"name":"python3","command": ["./header_transform_rule.json", "<バケット名>", "<inputファイルのパス>", "<バケット名>", "<outputファイルのパス>"]}]}' --launch-type FARGATE --network-configuration "awsvpcConfiguration={subnets=[<作成したサブネットID>],securityGroups=[<作成したセキュリティグループID>],assignPublicIp=ENABLED}"