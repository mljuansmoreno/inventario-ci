FROM docker:cli AS cli
FROM jenkins/jenkins:lts-jdk21
COPY --from=cli /usr/local/bin/docker /usr/local/bin/docker
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt
