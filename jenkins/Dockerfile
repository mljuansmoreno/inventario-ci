FROM docker:cli AS cli
FROM jenkins/jenkins:lts-jdk21
COPY --from=cli /usr/local/bin/docker /usr/local/bin/docker
