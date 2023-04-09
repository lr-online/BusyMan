# 使用 Python 3.9 作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器中的 /app 目录下
COPY . /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' > /etc/timezone

# 安装项目依赖
RUN pip install --upgrade pip -i https://pypi.doubanio.com/simple
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.doubanio.com/simple


# 暴露项目端口
EXPOSE 80

# 启动项目
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
