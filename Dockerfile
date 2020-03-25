FROM ubuntu:16.04

ADD . /www
WORKDIR /www/libfastcommon-master
RUN ./make.sh && sudo ./make.sh install
WORKDIR /www/fastdfs-master
RUN ./make.sh && sudo ./make.sh install
COPY /www/storage.conf /etc/fdfs/storage.conf
COPY /www/tracker.conf /etc/fdfs/tracker.conf
RUN sudo service fdfs_trackerd start
RUN sudo service fdfs_storaged start
WORKDIR /www/nginx-1.8.1
RUN sudo ./configure --prefix=/usr/local/nginx/ --add-module=/www/fastdfs-nginx-module-master/src
RUN sudo ./make&&sudo ./make install
COPY /www/mod_fastdfs.conf /etc/fdfs/mod_fastdfs.conf
COPY /www/http.conf  /etc/fdfs
COPY /www/mime.types /etc/fdfs
RUN sudo /usr/local/nginx/sbin/nginx

