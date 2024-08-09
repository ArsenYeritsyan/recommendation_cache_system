from flask import Flask, request, jsonify
import redis
import requests
import json
import threading

app = Flask(__name__)
cache = {}
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    if user_id in cache:
        return jsonify(cache[user_id])

    cached_result = redis_client.get(user_id)
    if cached_result:
        return jsonify(json.loads(cached_result))

    result = runcascade()
    cache[user_id] = result
    redis_client.setex(user_id, 10, json.dumps(result))
    return jsonify(result)

def runcascade():
    models = ['model1', 'model2', 'model3', 'model4', 'model5']
    results = []

    def fetch(model):
        response = requests.post('http://generator:5000/generate', json={"model_name": model, "viewer_id": 1})
        results.append(response.json())

    threads = [threading.Thread(target=fetch, args=(model,)) for model in models]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)