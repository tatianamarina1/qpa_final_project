FROM python:3 
RUN pip install sqlalchemy matplotlib
COPY script.py data_io.py db_data_types.py fill_db.py /
COPY data/ /data
CMD [ "python", "./script.py" ]