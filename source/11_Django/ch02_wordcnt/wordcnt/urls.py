# wordcnt 패키wl(__init__/py)안의 urls모듈(*.py)
# wordcnt/                 (name=wordcnt:wordinput)  단어 문자 입력받는 화면으로 감
# wordcnt/about            (name=wordcnt:about)      도움말
# wordcnt/result           (name=wordcnt:result)     입력받은 단어들의 결과 출력

from django.urls import path, include
from . import views    #  . 의 의미 : 현재 폴더    . = wordcnt

app_name = "wordcnt"
urlpatterns = [
      path("",views.wordinput, name="wordinput"),
      path("about/",views.about, name="about"),
      path("result/",views.result, name="result"),
]



    # path("admin/", admin.site.urls),
    # path("", views.index, name="index"),
    # path("test/", views.test, name="test"),
    # path("showId/<int:id>/", views.showIntId, name="showIntId"),
    # path("showId/<str:id>/", views.showStrId, name="showStrId"),
    # # path("wordcnt/"),   # 매번 path 지정하기에는 번거로움
    # # path("wordcnt/reault/"),
    # # path("wordcnt/about/"),
    # path("wordcnt/", include("wordcnt.urls")), 

