FROM python

RUN pip3 install psutil
RUN pip3 install pyTest


COPY ./*.py ./home

WORKDIR /home

ENTRYPOINT python3 -m pytest -v
