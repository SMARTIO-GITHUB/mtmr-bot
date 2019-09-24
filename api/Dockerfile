FROM golang:1.11

RUN apt-get update -qq && \
    apt-get install -y default-mysql-client vim

ENV GOPATH /go
ENV PATH $PATH:$GOPATH/bin

RUN mkdir -p /go/src/api
COPY . /go/src/api
WORKDIR /go/src/api

RUN go get -u  github.com/beego/bee
RUN go get -u github.com/astaxie/beego
RUN go get gopkg.in/mgo.v2

CMD bee run -downdoc=true -gendoc=true
