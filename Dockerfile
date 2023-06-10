FROM oraclelinux:9
RUN yum install -y python3-pip git; \
    pip install --upgrade pip; \
    yum clean all;
  
RUN git clone https://github.com/breeze-technology/salt-middleware.git /app

RUN pip install -r /app/requirements.txt

ENV SALT_API_USER_PASSWORD ${SALT_API_USER_PASSWORD}
ENV SALT_RETURNER_PASSWORD ${SALT_RETURNER_PASSWORD}

CMD sh -c "cd /app ; gunicorn -w 4 main:app"