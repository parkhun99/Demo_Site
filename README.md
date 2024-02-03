# Matrix demo site Front server

# 1. 환경
- Ubuntu 20.04.6 LTS
- Vue 3.2.13
- tailwind css 3.2.7

# 2. 실행
- npm install
- npm install -g @vue/cli
- npm run serve

# 3. 파일 구조
## 1) 디렉토리
- node_modules : 프로젝트의 의존성 패키지들이 설치되는 디렉토리
- public : 프로젝트 빌드 및 배포 디렉터리
- src : Vue.js 애플리케이션의 소스 코드가 위치하는 주요 디렉터리

## 2) 루트 경로 파일
- .babelrc : Babel 설정 파일
- .editorconfig : 코드 에디터의 설정 통일하기 위한 파일
- .eslintrc : 프로젝트 내의 JavaScript 코드에 대한 규칙 및 스타일을 정의 파일
- babel.config : JavaScript 코드를 환경에 맞게 변환 파일
- postcss.config.js : PostCSS(후처리기)의 설정 파일
- tailwind.config.js : Tailwind CSS 프레임워크의 설정 파일
- README.md

## 3) public 디렉토리 파일
- _redirects
- .htaccess
- index.html : 웹 페이지의 기본 구조를 정의
- Matrix_P1.png
- web.config

## 4) src 디렉토리 파일
- assets : 이미지, 스타일, Sass 파일 등 프로젝트에서 사용되는 정적 에셋을 저장
- logo : 프로젝트에 사용되는 로고 이미지 파일 저장
- components : 프로젝트에서 사용되는 여러 Vue 컴포넌트 파일 저장
- router : 특정 경로와 해당 경로에 매핑되는 Vue 컴포넌트 파일 저장
- store : 애플리케이션의 상태, 변이, 액션 관리와 관련된 로직 파일 저장
- App.vue : Vue.js 애플리케이션의 최상위 컴포넌트, 애플리케이션의 레이아웃 및 라우팅을 함
- main.js : Vue 애플리케이션 생성, 전반적인 설정 및 초기화를 담당함

## 5) components 디렉토리 파일
- AppAccordion.vue : Vue.js를 사용하여 토글 버튼이 있는 아코디언 스타일의 UI 요소를 생성하는 데 사용
- Header.vue : Vue.js를 사용하여 웹 애플리케이션의 헤더를 구성
- ImgPage.vue : 페이지 상단에 현재 위치 표시, 이미지와 관련된 페이지, 모델 설명, 데모, 샘플 이미지 등을 제공
- ImgResult.vue : 파일 선택, 드랍 영역, 업로드된 이미지, 결과 이미지, 결과 텍스트 등의 상태를 관리
- MainPage.vue : 모델 카테고리 및 썸네일 표시, 반응형으로 레이아웃을 조절, 클릭 시 모델 데모 페이지로 이동 기능 제공
- MenuAccordion.vue : 카테고리 및 서브 카테고리를 펼치고 닫을 수 있는 아코디언 스타일의 UI를 제공
- ModelDemo.vue : 화면 폭에 따라 이미지 업로드 및 서브 메뉴의 가시성을 동적 제어 기능 제공
- SampleImg.vue : 샘플 이미지 표시, 상호 작용 동작을 처리, 이미지의 URL을 부모 컴포넌트로 전달하는 기능 제공
- Sidebar.vue : 사이드바 구성, 메뉴 아이템 및 카테고리를 동적으로 표시
- SubMenu.vue : 다양한 버튼, 플 이미지가 있는 하위 메뉴 제공

# 4. 주의사항
## 1) 유지보수 용이성:
- 프론트 엔드 코드를 동적으로 개발하여 변경이나 추가 사항이 발생했을 때 기존 코드를 쉽게 수정할 수 있도록 구현

## 2) 최소한의 수정:
- 최소한의 수정으로 원하는 동작을 얻도록 함
- 코드 일부를 수정하여 전체 시스템을 빠르게 업데이트하거나 새로운 요구 사항을 빠르게 추가
  
## 3) config_category.py 모델 정보 동적 적용:
- config_category.py의 모델 정보를 동적으로 적용하고자 함
- 모델 변경이 발생하더라도 프론트 엔드 코드의 수정 없이 즉시 적용