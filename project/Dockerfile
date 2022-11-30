FROM python:3
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY script.py data_io.py db_data_types.py fill_db.py /
COPY data/ /data
CMD [ "python", "./script.py" ]