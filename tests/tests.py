import os
import subprocess
import time
import redis

def test_generator_service():
    print("Testing Generator Service...")
    result = subprocess.run([
        'curl', '-X', 'POST', 'http://generator:5000/generate',
        '-H', 'Content-Type: application/json',
        '-d', '{"model_name": "test_model", "viewer_id": 1}'
    ], stdout=subprocess.PIPE)
    print("Generator Service Response:", result.stdout.decode('utf-8'))

def test_invoker_service():
    print("Testing Invoker Service...")
    result = subprocess.run([
        'curl', 'http://invoker:5000/recommend?user_id=1'
    ], stdout=subprocess.PIPE)
    print("Invoker Service Response:", result.stdout.decode('utf-8'))

def test_redis_cache():
    print("Testing Redis Cache...")
    r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
    cache_result = r.get('1')
    print("Redis Cache Response for user_id=1:", cache_result)

def main():
    time.sleep(15)

    test_generator_service()
    time.sleep(1)
    test_invoker_service()
    time.sleep(1)
    test_redis_cache()

if __name__ == "__main__":
    main()