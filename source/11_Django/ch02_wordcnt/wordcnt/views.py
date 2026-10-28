from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def wordinput(request):
  return render(request, "wordcnt/wordinput.html") #templates/wordcnt/wordinput.html


def about(request):
    return render(request, "wordcnt/about.html")   #templates/wordcnt/about.html


def result(request):
    # print('전달받은 파라미터(fulltxt) ',request.GET)   #GET 방식으로 받은 내용 딕셔너리 타입
    # print('전달받은 파라미터(fulltxt):', request.POST)   #POST방식으로 받은 내용 딕셔너리 타입
    fulltxt = request.POST.get('fulltxt').strip()
    strlength=len(fulltxt)   #글자수
    words = fulltxt.split(" ") #단어들(space단위로 분리) ['홍길동','안녕', '홍길동']
    wordcnt = len(words)
    words_dic = dict()  # 빈 딕셔너리 
    for word in words:
      if word in words_dic: #word가 words_dic의 키로 존재하는지 여부
        words_dic[word] += 1
      else:
        words_dic[word] = 1
    # print(words_dic)
    # print(words_dic.items())
    context = {
        'fulltxt':fulltxt,
        'strlength':strlength,
        'wordcnt':wordcnt,
        'dict': words_dic.items()  #[('홍길동', 2), ('박길동', 1)]
    }
    return render(request,
                  "wordcnt/result.html",
                  context)


