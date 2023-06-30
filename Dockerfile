#FROM python:latest
FROM python:3.10

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple \
#    && pip install flask_sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple \
#    && pip install redis -i https://pypi.tuna.tsinghua.edu.cn/simple \
#    && pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple \
#    && pip install Bootstrap-Flask -i https://pypi.tuna.tsinghua.edu.cn/simple \
#    && pip install cryptography  -i https://pypi.tuna.tsinghua.edu.cn/simple  \
#    && pip install gunicorn -i https://pypi.tuna.tsinghua.edu.cn/simple   \
#    && pip install greenlet -i https://pypi.tuna.tsinghua.edu.cn/simple   \
#    && pip install eventlet -i https://pypi.tuna.tsinghua.edu.cn/simple   \
#    && pip install gevent  -i https://pypi.tuna.tsinghua.edu.cn/simple   

EXPOSE 8000
CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]
