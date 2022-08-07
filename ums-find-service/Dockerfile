FROM python:3.8-slim-buster

WORKDIR /ums
ADD ums /ums
RUN pip3 install -r requirements.txt

EXPOSE 7070
ENTRYPOINT ["python"]
CMD ["/ums/app.py"]