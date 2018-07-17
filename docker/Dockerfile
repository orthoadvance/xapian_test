FROM centos:7
# Set workdir to /tmp
WORKDIR /tmp/
# Set locale
RUN localedef -i fr_FR -f UTF-8 fr_FR.UTF-8
# Activate EPL
RUN yum install -y epel-release
# Fix set locale hack
RUN sed 's/^override_install_langs/#override_install_langs/' -i /etc/yum.conf
RUN yum -y -q install glibc-common
ENV LANG=fr_FR.UTF8
# Set timezone
RUN ln -snf /usr/share/zoneinfo/Europe/Paris /etc/localtime
# Install packages
RUN yum install -y \
    bash \
    htop \
    locate \
    unzip \
    vim \
    wget \
    glibc-common \
    gcc gcc-c++ make openssl-devel cmake unzip \
    libxml2 libxml2-devel libxslt libxslt-devel \
    gettext \
    git \
    glib  glib-devel \
    glib2 glib2-devel \
    libjpeg-devel \
    libffi-devel \
    pygobject3 \
    file-devel \
    kernel-devel \
    python python-devel \
    patch \
    xz \
    zlib-devel \
    --enablerepo=epel ; yum clean all
# Install xapian
ADD PATCHS/ /
ADD http://oligarchy.co.uk/xapian/1.4.2/xapian-core-1.4.2.tar.xz /
RUN cd / && tar Jxf /xapian-core-1.4.2.tar.xz
RUN mv /xapian-core-1.4.2 /xapian-core
RUN cd / && patch -p1 < /glass-cursor-rebuild-fix.patch
RUN cd /xapian-core && ./configure && make && make install
# Install PIP
ADD https://bootstrap.pypa.io/get-pip.py /tmp/
RUN python2 get-pip.py && pip install --upgrade pip
# INSTALL sphinx
RUN pip install sphinx
# Install xapian-bindings python
ADD http://oligarchy.co.uk/xapian/1.4.2/xapian-bindings-1.4.2.tar.xz /tmp/
RUN cd /tmp/ && tar Jxf /tmp/xapian-bindings-1.4.2.tar.xz && cd /tmp/xapian-bindings-1.4.2 && ./configure --with-python && make && make install
# Clone test
RUN ls
RUN cd /tmp/ && git clone https://github.com/staverne/xapian_test
# Test
CMD python /tmp/xapian_test/test_xapian.py glass
