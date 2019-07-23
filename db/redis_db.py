# coding:utf-8
import json
import redis
from config.conf import get_redis_args

redis_args = get_redis_args()
parameter_db = redis_args.get('parameter', 1)
children_db = redis_args.get('children', 2)

host = redis_args.get('host', '127.0.0.1')
port = redis_args.get('port', 6379)

parameter_con = redis.Redis(host=host, port=port,db=parameter_db)
children_con = redis.Redis(host=host, port=port, db=children_db)

class Parameters(object):


    @classmethod
    def store_parameter(self, sign, parameter):
        pickled_parameter = json.dumps(
            {'parameter': parameter, 'sign': sign})
        parameter_con.hset('md5url', sign['md5url'], pickled_parameter)
        self.push_in_queue(sign['md5url'])

    @classmethod
    def push_in_queue(self, md5url):
        for i in range(parameter_con.llen('md5url_queue')):
            temp = parameter_con.lindex('md5url_queue', i).decode('utf-8')
            if temp:
                if temp == md5url:
                    return
        parameter_con.rpush('md5url_queue', md5url)

    @classmethod
    def fetch_parameter(self):
        for i in range(parameter_con.llen('md5url_queue')):
            md5url = parameter_con.lpop('md5url_queue').decode('utf-8')
            parameter = parameter_con.hget('md5url', md5url).decode('utf-8')
            if parameter:
                parameter = json.loads(parameter)
                return md5url, parameter
        return None
