import functools
import requests

def add_correlation_id(fields):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'data' in kwargs:
                kwargs['data'].update(fields)
            elif 'json' in kwargs:
                kwargs['json'].update(fields)
            return func(*args, **kwargs)
        return wrapper
    return decorator

class AddCorrelationIdMeta(type):
    def __new__(cls, name, bases, dct):
        correlation_id = dct.get('correlation_id', {})
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and attr_name.startswith('http_'):
                dct[attr_name] = add_correlation_id(correlation_id)(attr_value)
        return super().__new__(cls, name, bases, dct)

class HttpClient(metaclass=AddCorrelationIdMeta):
    correlation_id = {'correlation_id': 'abc123', 'source': 'api'}

    def http_post(self, url, **kwargs):
        response = requests.post(url, **kwargs)
        return response.json()

    def http_get(self, url, **kwargs):
        response = requests.get(url, **kwargs)
        return response.json()

if __name__ == "__main__":
    client = HttpClient()
    url = "https://httpbin.org/post"
    payload = {'message': 'Hello, World!'}
    response = client.http_post(url, json=payload)
    print(response)
