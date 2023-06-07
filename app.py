from flask import Flask

FAI=Flask(__name__)


@FAI.route('/Happy/<name>/')
def Happy(name):
    return  f'hello...Good Evening {name}!...'

if __name__=='__main__':
    FAI.run(debug=True,host='192.168.182.244',port=5001)
    