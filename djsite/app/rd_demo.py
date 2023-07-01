import redis

red = redis.Redis(host="127.0.0.1",port=6379)
# 时限10秒
red.set('name', 9999, ex=10)
value = red.get('name')
print(value)

# red.set("name", "小白")
# red.save()

# r = red.get("name")
# print(r)

# red.hset("xiao", "bai", "新")
# red.hset("xiao", "age", 18)
# red.save()

# r = red.hmget("xiao", "bai", "age")
# print(r)

# r = red.hgetall("xiao")
# print(r)


# red.lpush("stu", "新木优子", "刘亦菲", "杨幂")
# red.save()

# r = red.lrange("stu", 0, -1)
# print(r)

# red.sadd("teachers", "古力娜扎", "迪丽热巴", "蜡笔小新")
# red.save()

# r = red.smembers("teachers")
# print(r)

# red.zadd("ren", {"刘亦菲": 10, "杨幂": 15, "杨颖": 5})
# red.save()

# r = red.zrange("ren", 0, -1)
# print(r)

# r = red.zrange("ren", 0, -1, withscores=True)
# print(r)
