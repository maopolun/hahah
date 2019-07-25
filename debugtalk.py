
import time

def sleep(n_secs):
    time.sleep(n_secs)

def get_timestamp():
    return str(time.strftime('%Y-%m-%d %X'))

def print_documentId():
    # print('documentId是：%s' % id)
    print('哈哈哈哈哈哈哈哈哈哈哈')


def get_base_url(env_type="prod"): # prod：生产环境
    if env_type == "prod":
        return "https://mubu.com"
    else:
        return "https://test.mubu.com"




