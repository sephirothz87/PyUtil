#coding:utf-8
import logging
import logging.config


config = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': { 
        'standard': {
            # 'format': '[%(asctime)s][%(threadName)s:%(thread)d]'
            #           '[%(name)s:%(levelname)s(%(lineno)d)]\n'
            #           '[%(module)s:%(funcName)s]:%(message)s'
            'format': '[%(asctime)s][%(levelname)s(%(lineno)d)]:%(message)s'
        }
    },
    
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            # 'filename': '/data/kgt/log/debug.log', 
            'filename': './log/debug.log', 
            'maxBytes': 1024*1024*5, 
            'backupCount': 5, 
            'encoding': 'utf8',
        },
    },
    
    'loggers': {
        'default': {
            'handlers': ['console', 'log'],
            'level': 'DEBUG',
            'propagate': True, 
        },
        'product': {
            'handlers': ['console', 'log'],
            'level': 'INFO',
            'propagate': False, 
        },
    }
}

# logging.basicConfig(level = logging.INFO,format = '[%(asctime)s][%(name)s][%(levelname)s]  %(message)s',filename='../log/debug.log',filemode='w')
# logger = logging.getLogger(__name__)
logging.config.dictConfig(config)
logger = logging.getLogger("default")