FROM python
WORKDIR /src
COPY server.py .
RUN pip install flask
EXPOSE 4000
CMD python server.py

