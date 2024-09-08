#!/bin/sh

BACKUP_DIR="/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/redis_backup_$TIMESTAMP.rdb"

redis-cli SAVE
cp /data/dump.rdb "$BACKUP_FILE"

echo "Backup created: $BACKUP_FILE"

# 3日以上経過したバックアップを削除
find "$BACKUP_DIR" -name "redis_backup_*.rdb" -type f -mtime +3 -delete
