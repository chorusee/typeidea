from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'typeidea',
        'PASSWORD': '123@typeidea_db1',
        'HOST': '127.0.0.1',
        'PORT': 3306,

    }
}

REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD': ''
            'CLIENT_GLASS': 'django_redis.client.DefaultClient',
            'PARSE_GLASS': 'redis.connection.HiredisParse',
        },
        'CONNECTION_POOL_GLASS': 'redis.connection.BlockingConnectionPool',
    }
}
