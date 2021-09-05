# -*- coding: utf-8 -*-
import pandas as pd
import boto3
import io
import json
import sys

# 引数指定
header_transform_rule = sys.argv[1]
src_bucket_name = sys.argv[2]
src_key_name = sys.argv[3]
dest_bucket_name = sys.argv[4]
dest_key_name = sys.argv[5]

# header_transform_rule.jsonを読み込み
header_transform_rule=open(f'{header_transform_rule}', 'r')
header_transform_rule=json.load(header_transform_rule)

# src読み込み
s3 = boto3.client('s3')
src_object_body = s3.get_object(Bucket=src_bucket_name, Key=src_key_name)['Body'].read().decode('utf-8')

# header変換処理
buffer_in = io.StringIO(src_object_body)
df_in = pd.read_csv(buffer_in)
df_out = df_in.rename(columns=header_transform_rule)
buffer_out = io.StringIO()
df_out.to_csv(buffer_out, index=False)

# dest書き出し
body_out = buffer_out.getvalue()
dest_object_body = s3.put_object(Bucket=dest_bucket_name, Key=dest_key_name, Body=body_out)
print ("successed")