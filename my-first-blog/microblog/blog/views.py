from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm

'''
  render関数は通常、templatesフォルダの中のhtmlファイルを読み込む
  {"posts": posts}は、postsという変数をテンプレートに渡す
'''


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {"posts": posts})


'''
  slug=slug
  右側のslugが引数のslugに該当
  getメソッドは、指定されたフィルターに一致するオブジェクトを返す
  クエストされたURLから直接取得した値であることから、
  データベースの状態と一致しない場合、リダイレクト先が意図したポストにならない可能性がある

  redirect関数の引数、post.slugとの違い
  post.slugは、Postモデルのslug属性を指し、特定のポストを識別するために使用される。
  基本的には両者共に同じ値であることが期待されるが、
  データベース内のslug(post.slug)が変更された場合など必ずしも両者が一致するわけでないため、
  redirect関数には後者のデータベースのslug情報に基づいたpost.slugを指定する必要がある。

  POSTメソッドが複数あり処理を分岐したい場合、
  if request.method == "POST" and 'comment' in request.POST:
  とすることで、POSTリクエストの中にcommentというキーがあるかチェックし、
  それに対応した処理を行うことができる

  form.save()
  フォームから送信されたデータを使って新しいモデルインスタンスを作成し、
  データベースに保存するメソッド

  commit=False
  データベースに即座に保存せず、モデルインスタンスを返す。
  これにより、モデルインスタンスの属性を変更したり、関連オブジェクトを設定したりできる

  テンプレートにpostとformがrender関数によって渡される流れ。
  1. post_detailにリクエストが送信される

  2. request.methodがPOSTかつform.is_valid()がTrueの場合、
     redirect関数によって再びリクエストが発生し、post_detail関数が呼び出される。

  3. post_detail関数内のrender関数が実行され、postとformがテンプレートに渡される
'''


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)  # 指定されたslugに一致するPostオブジェクトを取得

    if request.method == "POST":
        form = CommentForm(request.POST)  # CommentFormのインスタンス化

        if form.is_valid():
            comment = form.save(commit=False)  # Commentモデルのインスタンスを作成
            comment.post = post  # commentがどのポストに関連づけられているかを設定
            comment.save()  # コメントをデータベースに保存

            # commentを投稿後にpost_detailにリダイレクト
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()

    # comment投稿後にpost_detailにリダイレクトされ、その時のリクエストに対してrender関数が実行される
    return render(request, "blog/post_detail.html", {"post": post, "form": form})
