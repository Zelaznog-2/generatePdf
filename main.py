import sys
from components.getApi import getApi
from components.generatePdf import generatePdf


def main():
  try:
    api_data = getApi()
    generatePdf(api_data)
  except Exception as e:
    print(f'Error: {e}')
    sys.exit(1)
  finally:
    print('Program completed successfully')
    sys.exit(0)

if __name__ == '__main__':
  sys.exit(main())