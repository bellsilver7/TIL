# nest.js 공식문서 학습

```
Nest(NestJS)는 효율적이고 확장 가능한 Node.js 서버 측 애플리케이션을 구축하기 위한 프레임워크입니다. 프로그레시브 자바스크립트를 사용하고, TypeScript로 구축되고 완벽하게 지원하며(아직도 개발자는 순수한 JavaScript로 코딩할 수 있음), OOP(Object Oriented Programming), FP(Functional Programming) 및 FRP(Functional Reactive Programming)의 요소를 결합합니다.

Nest는 Express(기본값)와 같은 강력한 HTTP 서버 프레임워크를 사용하며 선택적으로 Fastify를 사용하도록 구성할 수 있습니다!

Nest는 이러한 일반적인 Node.js 프레임워크(Express/Fastify)보다 추상화 수준을 제공하지만, API를 개발자에게 직접 노출합니다. 이를 통해 개발자는 기본 플랫폼에서 사용할 수 있는 수많은 타사 모듈을 자유롭게 사용할 수 있습니다.
```

node.js 덕분에 javascript는 프론트와 백엔드 애플리케이션 모두에서 큰 영향을 미치고 있지만 아키텍처의 주요 문제까지 해결해주지는 못했다. 하지만 nest.js는 고도로 테스트 가능하고 확장 가능하며 느슨하게 결합되고 유지관리할 수 있는 아키텍처를 제공한다고 한다. 이는 Angular에서 영감을 받았다고 말한다.

nest.js에 대해 간단히 알아봤고 설치를 시작했다.

2가지 방법을 제공하고 있었으며 한가지는 Nest CLI를 사용하는 방법과 하나는 Github 저장소에서 클론하는 방법이다. 나는 CLI를 설치해 시도했다.

```bash
$ npm i -g @nestjs/cli
$ nest new project-name
```
> TypeScript의 엄격한 모드가 활성화된 새 프로젝트를 만들려면, nest new 명령에 --strict 플래그를 함께 입력합니다.