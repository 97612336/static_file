FROM python:latest

WORKDIR /src

COPY ./ /src/

COPY ./.pip /root/
 
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirments.txt

CMD ["python","manage.py","runserver"]
