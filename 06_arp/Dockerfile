FROM ubuntu

ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y iptables tcpdump dsniff iproute2 python3 python3-pip tmux dnsutils
RUN pip3 install --upgrade --break-system-packages scapy mitmproxy==7.0.4 werkzeug==2.0

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
