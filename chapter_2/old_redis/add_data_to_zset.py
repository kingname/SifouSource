import redis

client = redis.Redis()

client.zincrby('python', 'chapter', 2)
