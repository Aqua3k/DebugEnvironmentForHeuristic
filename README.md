# 概要
たくさんの入力ファイルに対し、プログラムを実行し、結果を記録するデバッグ環境です  
ヒューリスティックコンテスト時の活用を想定しています  

# できること
1 複数のケースに対してプログラムを実行し、その結果を管理します  
2 (適切な前準備をすることで)結果から図を自動で作成します  
　ただし、図の出力にはpandasとmatplotlibをインストールする必要があります  
　(設定で図の出力をしないようにもできます)

# 準備
## main.py内の準備  
main.pyには回答用のスクリプトを書いてください
main()関数以下に書くようにしてください  
また、得点を結果ファイルに反映させたいならmain()の戻り値にスコアを返してください  
プログラム内でスコアを管理していない等の理由で上記が不可能なら、戻り値を返さなくても大丈夫です  

## 入力ファイルの準備  
in以下に任意個の入力用のtxtファイルを入れてください  
入力ファイルの名前は任意で問題ありません  

## 設定ファイル(settings.py)の設定   
### statisticsInfoArray  
結果出力時にwatchしたい変数を指定します  
main.pyの中で使っている変数名list[str]の形式で書いてください  
例としてNとMを見たいときは  
statisticsInfoArray = ["N", "M"]  
と書いてください  
ただし、main.pyの中でグローバルスコープに入っている変数しか指定できず、配列は指定できません   
この機能を使いたくないときは空のリスト[]を指定しておいてください  

### makeFigure
この変数がTrueだと図を作成する処理が走ります  
前述のように、図の出力にはpandasとmatplotlibが必要です  
図を出力したくない場合やpandasとmatplotlibがインストールされていない場合はFalseにしてください

### その他の変数  
パスと出力するファイルの名前です  
パスは絶対パスでも相対パスでも指定できます  
よくわからないなら変更しないでください  

# 出力される結果ファイル  
## 出力結果  
out以下のディレクトリに入力ケースと同じ名前で出力されます  
目視で出力形式が正しいか確認するときや、ビジュアライザなどを使うときに使えます  
 
## csvファイルと図  
statistics以下のディレクトリに結果のCSVファイルが出力されます  
scoreとstatisticsInfoArrayで指定した変数のscatterグラフを作成します  

## HTMLファイル  
DebugLib.pyと同じ階層にresult.htmlというhtmlファイルが作成されます  
各種情報と入力ファイル、出力ファイルへのリンクが載っています  
