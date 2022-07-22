# RabbitMQ

참조: [RabbitMQ](https://www.rabbitmq.com/)

With tens of thousands of users, RabbitMQ is one of the most popular open source <u>_[message brokers](#메세지-브로커message-broker)_</u>. From T-Mobile to Runtastic, RabbitMQ is used worldwide at small startups and large enterprises.

RabbitMQ is lightweight and easy to deploy on premises and in the cloud. It supports multiple messaging protocols. RabbitMQ can be deployed in distributed and federated configurations to meet high-scale, high-availability requirements.

RabbitMQ runs on many operating systems and cloud environments, and provides a wide range of developer tools for most popular languages.

<br>
<br>

## 특징

### - 비동기 메시징(Asynchronous Messaging)

여러 메시징 프로토콜(multiple messaging protocols), 메시지 대기열(message queuing), 배달 승인(delivery acknowledgement), 대기열에 대한 유연한 라우팅(flexible routing to queues), 여러 교환 유형(multiple exchange type)을 지원합니다.

### - 개발자 경험(Developer Experience)

Kubernetes, BOSH, Chef, Docker 및 Puppet으로 배포합니다. Java, .NET, PHP, Python, JavaScript, Ruby, Go 등과 같은 선호하는 프로그래밍 언어로 언어 간 메시징을 개발하십시오.

### - 분산 배포(Distributed Deployment)

고가용성(availability) 및 처리량(throughput)을 위해 클러스터로 배포합니다. 여러 가용 영역(availability zones) 및 지역(regions)에 걸쳐 연합합니다.

### - 엔터프라이즈와 클라우드 지원(Enterprise & Cloud Ready)

플러그형 인증(Pluggable authentication), 권한 부여(authorisation), TLS(전송 계층 보안) 및 LDAP(경량 디렉터리 액세스 프로토콜)를 지원합니다. 가볍고 퍼블릭 및 프라이빗 클라우드에 배포하기 쉽습니다.

### - 도구 및 플러그인(Tools & Plugins)

지속적인 통합(continuous integration), 운영 메트릭(operational metrics) 및 다른 엔터프라이즈 시스템과의 통합을 지원하는 다양한 도구 및 플러그인. RabbitMQ 기능 확장을 위한 유연한 플러그인 접근 방식.

### - 관리 및 모니터링(Management & Monitoring)

RabbitMQ 관리 및 모니터링을 위한 HTTP-API, command line 도구 및 UI.

<br>
<br>

## 다운로드 및 설치

[Change Log](https://www.rabbitmq.com/changelog.html)

[Release Series](https://www.rabbitmq.com/versions.html)

```yaml
# 최신 RabbitMQ 3.10
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

### 설치 가이드

- Linux, BSD, UNIX: [Debian](https://www.rabbitmq.com/install-debian.html), [Ubuntu](https://www.rabbitmq.com/install-debian.html) | [RHEL, CentOS, Fedora](https://www.rabbitmq.com/install-rpm.html) | [Generic binary build](https://www.rabbitmq.com/install-generic-unix.html) | [Solaris](https://www.rabbitmq.com/install-solaris.html)
- Windows: [Chocolatey or Installer](https://www.rabbitmq.com/install-windows.html) (recommended) | [Binary build](https://www.rabbitmq.com/install-windows-manual.html)
- MacOS: [Homebrew](https://www.rabbitmq.com/install-homebrew.html) | [Generic binary build](https://www.rabbitmq.com/install-generic-unix.html)
- [Erlang/OTP for RabbitMQ](https://www.rabbitmq.com/which-erlang.html)

<br>
<br>

## 튜토리얼

RabbitMQ는 메시지 브로커로 메시지를 수락하고 전달합니다. 우편물을 우편함에 넣으면 배달부가 받는 사람에게 배달할 것을 우리는 알고 있습니다. 여기서 우리는 RabbitMQ를 우체국이라고 생각해볼 수 있습니다. 우체국과의 차이점은 종이를 다루지 않고 이진 데이터(binary blobs of data ‒ messages)를 수락하고 저장 및 전달하는 것입니다.

### 주요 용어

- producing : 보내는 것 이상을 의미하지 않습니다. 메시지를 보내는 프로그램은 생산자 입니다.

- queue : RabbitMQ 내부에 있는 우편함의 이름입니다. 메시지는 RabbitMQ와 애플리케이션을 통해 흐르지만 queue 내부에만 저장할 수 있습니다. 큐 는 호스트 의 메모리 및 디스크 제한에 의해서만 바인딩되며 본질적으로 큰 메시지 버퍼입니다. 많은 생산자 가 하나의 대기열로 메시지를 보낼 수 있고 많은 소비자 가 하나의 대기열 에서 데이터 수신을 시도할 수 있습니다. 이것이 우리가 큐를 표현하는 방법입니다:

- Consuming : 받는 것과 비슷한 의미를 가지고 있습니다. consumer는 대부분 메시지 수신을 기다리는 프로그램입니다.

1. **"Hello World!"** : 어떤 일을 하는 가장 단순한 것 [[이동](./RabbitMQ/rabbitmq-tutorial-hello-world.md)]

   ![image](https://www.rabbitmq.com/img/tutorials/python-one.png)

2. **Work queues** : 작업자 간의 작업 분배 (the competing consumers pattern) [[이동](./RabbitMQ/rabbitmq-tutorial-work-queues.md)]

   ![image](https://www.rabbitmq.com/img/tutorials/python-two.png)

3. **Publish/Subscribe** : 한 번에 많은 소비자에게 메시지 보내기 [[이동](./RabbitMQ/rabbitmq-tutorial-publish-subscribe.md)]

   ![image](https://www.rabbitmq.com/img/tutorials/python-three.png)

4. **routing** : 메시지를 선택적으로 수신 [[이동](./RabbitMQ/rabbitmq-tutorial-routing.md)]

   ![image](https://www.rabbitmq.com/img/tutorials/python-four.png)

5. **Topics** : 패턴 기반 메시지 수신 (topics) [[이동](./RabbitMQ/rabbitmq-tutorial-topics.md)]

   ![image](https://www.rabbitmq.com/img/tutorials/python-five.png)

6. **RPC** : 요청/응답 패턴 [[이동](./RabbitMQ/rabbitmq-tutorial-rpc.md)]

   ![image](https://www.rabbitmq.com/img/tutorials/python-six.png)

7. **Publisher Confirms** : Reliable publishing with publisher confirms [[이동](./RabbitMQ/rabbitmq-tutorial-publisher-confirms.md)]

<br>
<br>

## 용어설명

### 메세지 브로커(message broker)

```text
인터페이스 엔진(interface engine)은 송신자의 메시지 프로토콜 형식으로부터의 메시지를 수신자의 메시지 프로토콜 형식으로 변환하는 중간 컴퓨터 프로그램 모듈이다. 메시지 브로커들은 응용 소프트웨어가 이전에 정의해둔 메시지를 교환할 수 있는 전기통신의 요소 또는 컴퓨터 네트워크이다. 메시지 브로커들은 메시지 지향 미들웨어(MOM)의 빌딩 블록이지만 일반적으로 MOM과 원격 프로시저 호출(RPC) 등의 전통적인 미들웨어를 대체하지는 않는다.
```

[참조] [위키백과](https://ko.wikipedia.org/wiki/%EB%A9%94%EC%8B%9C%EC%A7%80_%EB%B8%8C%EB%A1%9C%EC%BB%A4)
