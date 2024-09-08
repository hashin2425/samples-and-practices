#!/bin/bash

aws dynamodb create-table \
    --table-name MyTable \
    --attribute-definitions AttributeName=Id,AttributeType=S \
    --key-schema AttributeName=Id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://dynamodb:8000

aws dynamodb put-item \
    --table-name MyTable \
    --item '{"Id": {"S": "1"}, "Name": {"S": "Item 1"}}' \
    --endpoint-url http://dynamodb:8000
