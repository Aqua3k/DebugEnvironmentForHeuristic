####################################
#入力ファイルの場所
inputFilePath = "in"

####################################
#ファイル出力する場所
resultFilePath = "out"

####################################
#log
logFilePath = "log"

####################################
#生成するScore情報を書き込むファイルのパス
scoreFileName = "summary.txt"

####################################
#statistics
makeFigure = True
scoreStr   = "score"
statisticsInfoArray = []

statisticsDirec = "statistics"
csvFileName     = "Statistics.csv"

####################################
#tester commands
myCmd = "python main.py"
command = "cargo run --release --bin tester {myCmd} < {inFile} > {outFile}"
