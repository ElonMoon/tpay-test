# tpay Test
[![codecov](https://codecov.io/gh/ElonMoon/tpay-test/branch/master/graph/badge.svg)](https://codecov.io/gh/ElonMoon/tpay-test)
### Python, Django Version
- python 3.8.5
- django 2.2

### 프로젝트 실행 방법
1. `git clone https://github.com/ElonMoon/tpay-test.git .`
2. `docker build -t tpay -f Dockerfile .`
3. `docker run --rm -it -p 8000:80 --name tpay tpay`
4. URI `http://localhost:8000`

### 프로젝트 API 문서
`http://localhost:8000/doc/`

### 프로젝트 테스트 방법
1. `docker exec -it tpay /bin/bash`
2. `pytest`