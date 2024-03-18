FROM ubuntu:bionic

RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install python3-pip texlive-latex-base texlive-latex-extra texlive-fonts-recommended xzdec -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -i https://test.pypi.org/simple/ latex-generator-sesorov==1.0.0

RUN apt-get update && apt-get install -y wget
RUN wget -O image.jpg https://thispersondoesnotexist.com

RUN mkdir /output
RUN latex-generator --image image.jpg --output /output
RUN pdflatex -output-directory /output /output/table.tex

WORKDIR /output