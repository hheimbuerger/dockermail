FROM ubuntu:15.10

ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen en_GB en_GB.UTF-8 && dpkg-reconfigure locales

# Prerequisites
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && \
    apt-get update && apt-get install -y \
    git-core \
    build-essential \
    pkg-config \
    libev-dev \
    libpcre3-dev \
    wget \
    jq \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Build libsrs2 from source
ENV LIBSRS2_PACKAGE=libsrs2-1.0.18
RUN cd /tmp && \
    wget -q http://www.libsrs2.org/srs/$LIBSRS2_PACKAGE.tar.gz && \
    tar xfz $LIBSRS2_PACKAGE.tar.gz && \
    cd /tmp/$LIBSRS2_PACKAGE && \
    ./configure && \
    make install && \
    ldconfig && \
    rm -R /tmp/$LIBSRS2_PACKAGE*

# Build pfix-srsd from source
RUN cd /tmp && git clone --recursive https://github.com/Fruneau/pfixtools.git && \
    cd /tmp/pfixtools/common && make && \
    cd /tmp/pfixtools/pfix-srsd && make install && \
    ldconfig && \
    rm -R /tmp/pfixtools

# Nice place for your settings
VOLUME ["/mail_settings"]

# Copy boot scripts
COPY boot /
COPY boot.d /boot.d
RUN chmod 755 /boot /boot.d/*

EXPOSE 10001 10002
CMD /boot; /usr/local/sbin/pfix-srsd -f -I mydomain.com /etc/postfix/pfix-srs.secrets
