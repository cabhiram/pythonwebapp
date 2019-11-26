import sys, os, json
sys.path.append('../')

from webapp import app

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000)
