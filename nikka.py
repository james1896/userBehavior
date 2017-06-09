# -*- coding: utf-8 -*-

from app import app


print "run  调用了两次需要修改"



if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", debug=True, port=8001)
