import time
import datetime

age = 10
name = 'taro'

if age < 20:
    print('20歳未満')
    print('2行目')
else:
    print('20歳以上')
    print('2行目')

print(type(30/3))
print("5times" * 5)
print(f"My name is {name}.\nage is {age}")

names_array = ['Tanaka', 'Yamada', 'Nakayama']  # array
names_array.append('Makino')
names_array.pop(2)
print(len(names_array))

'''
  tuple
  値の変更ができない。error: names_tuple[0] = 'Anonymous')
'''
names_tuple = ('Tanaka', 'Yamada', 'Nakayama')
print(type(names_tuple))

'''
  set
  順番と重複(重複が許されない)の概念を持たない。
'''
names_set = {'Tanaka', 'Yamada', 'Nakayama'}
print(type(names_set))

nums_set = {2, 5, 2, 7, 3, 5, 5}  # {2, 3, 5, 7} 必ずしも昇順ではない
nums_set.add(8)
nums_set.remove(2)
print(nums_set)

'''
  dictionary(連想配列)
  重複したキーは登録できない。重複して記載しすると、値が上書きされる。

  以下の連想配列の要素は同じ
  {1: "soccer", 2: "baseball", 3: "basketball"}
  {1: "soccer", 2: "tennis", 2: "baseball", 3: "basketball"}

'''
sports = {1: "soccer", 2: "baseball", 3: "basketball"}
sports[2] = "tennis"
sports[4] = "baseball"
sports.pop(1)
print(sports)

'''
  dict型のfor文
'''
for sport in sports.items():
    print(sport)

for keys in sports.keys():
    print(keys)

for values in sports.values():
    print(values)

for key, value in sports.items():
    print(f"key: {key}, value: {value}")

'''
  配列のindexを取り出す
'''
for index, value in enumerate(names_array):
    print(f"index: {index}, value: {value}")

'''
  関数とアノテーション

  以下のように戻り値と戻り値のアノテーションが一致しない場合、
  暗黙の型変換は起こらず、戻り値の型は引数の型となる。
  def func(num: int) -> str:
      return num


  print(type(func(num)))  # int
'''
num = 0


def func(num: int) -> str:
    return str(num)


print(type(func(num)))

'''
    クラス
    継承: クラスを引き継ぐ
      ・乗り物クラス(スーパークラスまたは親クラス)
      ->継承
        ・車クラス (サブクラスまたは子クラス)
        ・バイククラス (サブクラスまたは子クラス)

    オーバーライド: スーパークラスのメソッドをサブクラスで上書きする
      ・乗り物クラス
        - メソッド(走る、ブレーキ)
      ->継承
        ・車クラス
        - 「走る」メソッド
          + 走る時にガソリンを使う(オーバーライドで処理の一部を変更)

    ※オーバーライドでは新たに引数を追加できない。
    メソッドの戻り値は同じ型とする

    publicクラス: 全て公開
    protectedクラス: クラス内部とサブクラスのみアクセス可能
    privateクラス: クラス内部からのみアクセス可能

    属性
'''


class Product:
    def __init__(self):  # コンストラクタ
        self.name = ""  # 属性の定義

    def set_name(self, name):
        self.name = name


shampoo = Product()
shampoo.set_name("シャンプー")
print(shampoo.name)


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


user = User("Hiro", 33, "man")
print(user.name)
print(user.age)
print(user.gender)

'''
  timeモジュール
'''
# 現在時刻をUNIXタイムスタンプで取得
print(time.time())

# 現在時刻を日時のフォーマットで取得
print(time.strftime("%Y年%m月%d日%H時%M分%S秒", time.localtime()))

'''
  datetimeモジュール
'''
now = datetime.datetime.now()
date = datetime.datetime.strptime("2015-03-19", "%Y-%m-%d")
date_time = \
    datetime.datetime.strptime("2015-03-19 12:15:30", "%Y-%m-%d %H:%M:%S")
print(date_time.strftime("%Y年%m月%d日%H時%M分%S秒"))
print(date_time.year)
print(date_time.second)

interval = now - date_time
print(interval.days)

td_1y = datetime.timedelta(days=365)
td_3d = datetime.timedelta(days=3)

add = now + td_1y
sub = now - td_3d

print(add.strftime("今から1年後は%Y年%m月%d日%H時%M分%S秒"))
print(sub.strftime("今から3日前は%Y年%m月%d日%H時%M分%S秒"))
