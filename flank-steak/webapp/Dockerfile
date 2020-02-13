#creates base layer
FROM python:3

#Starts working dir


#Copy Files
#COPY /csvdemo.csv ./csvdemo.csv
COPY . .

# Install Requirements
RUN apt-get install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

#Debian 10
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list


RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# optional: for unixODBC development headers
RUN apt-get install unixodbc-dev
# optional: kerberos library for debian-slim distributions
RUN apt-get install libgssapi-krb5-2
RUN pip install -r requirements.txt

EXPOSE 8050

CMD python ./reportbuilder.py
