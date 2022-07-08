FROM tiangolo/meinheld-gunicorn-flask:python3.8
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD *.py /code/
ADD mferbase.db /code/
EXPOSE 8888
CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "app:app", "--preload", "--workers", "4", "--access-logfile", "-"]
