#smaple_pac/ab/__init__.py
#sample_pac.ab 패키지를 import 할 때 자동적으로 메모리에 로드되는 파일
# ab페키키지 셋팅
#ab밑에 a.py(공통적으로 많이 쓰는 함수들)와 b.py(가끔가다 쓰는 함수)
#from sample_pac.ad import *이렇게 쓸 수 있도록 세팅
__all__=['a','b']

print("sample_pac안에 ab패키지를 로드 됨")
