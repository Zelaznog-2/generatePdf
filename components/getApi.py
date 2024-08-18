import requests

def getApi():
  """
  Fetches data from the API endpoint https://jsonplaceholder.typicode.com/users and returns the JSON response.
  """
  result = None
  try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    result = response.json()
  except requests.exceptions as e:
    print(f'Error fetching data: {e}')
  finally:
    print('API request completed')
    return result