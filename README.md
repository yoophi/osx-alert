OSX-Alert
==========

OSX의 Apple Script를 이용하여 커맨드라인에서 alert 를 띄울 수 있게 하는 간단한 유틸리티입니다.
(OSX 에서만 동작합니다.)

### 설치 

shell 에서 사용할 수 있는 `alert` 스크립트가 함께 설치됩니다.


```bash
$ pip install git+https://github.com/yoophi/osx-alert.git@master
```

### 실행

```bash
$ alert Some text to alert --title Title
```

긴 작업을 실행한 후 결과를 화면에 띄울 의도로 만들었습니다.

```bash
$ sleep 360 && alert 6분 지났습니다.
$ ls -lR > /tmp/files.txt && alert files.txt 에 항목을 저장했습니다. --title 'OK'
```

`subprocess` 를 이용하기 때문에 코드 내에서 다음과 같이 사용할 수 있습니다.

```python
from alert import alert


while True:
    ret = do_some_long_func()
    alert("result: %s" % ret, "Result")
```
