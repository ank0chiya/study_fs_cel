# celeryconfig.py

# celeryを動かすための設定ファイル。
BROKER_URL = 'redis://localhost/0'

# CELERYD_CONCURRENCY=1なので、１こずつキューを捌いていく
# ここはCPU数に合わせていくのがよい
CELERYD_CONCURRENCY = 1
CELERY_RESULT_BACKEND = 'redis'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = "redis"
CELERYD_LOG_FILE = "./celeryd.log"

# CELERYD_LOG_LEVELをINFOにしておくと、
# タスクの標準出力もログ(celeryd.log)に書かれる
CELERYD_LOG_LEVEL = "INFO"

# ワーカーはtasks.pyを読み込み、
# 非同期処理させる関数を
# 含むスクリプト全てを指定
CELERY_IMPORTS = ("tasks", )