# flaskTrain
**1. flask的练习**
+ 两个页面，一个连接Mysql，一个连接redis
+ 导入了bootstrap来装饰页面  
+ 如果本地开发调试，服务连接的字符串，需要改为localhost  
    ```
    redis.StrictRedis(host="localhost", port=6379, db=0) <= start.py  
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/test' <= dbconfig.py
+ 本地调试启动flask
    ```
    gunicorn -c gunicorn.conf.py start:app  
**2. docker-compose的练习**
+ mysql和redis的服务器，在compose中一键发布和启动
+ flask要跑起来的话，需要先启动这两个服务器
    ```
    docker-compose up -d  
**3. dockerfile的练习**
+ flask整体环境的自动打包发布
    ```
    docker build -t 'testflask' .   
    docker run -d --name flaskApp -p 8000:8000 testflask   
    docker network connect fl_mynet flaskApp   
    docker start flaskApp  
