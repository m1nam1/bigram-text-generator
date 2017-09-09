# coding:utf-8
import random
import commands
import sys

# 一行一記事で分かち書きされたテキストを入力とし、
# bigramを用いてテキストを自動生成するスクリプト
# python bigram.py neko.txt.owakati

#入力ファイル名
INPUT_FILE_NAME = ""
#試行回数
TRY_NUM = 100
RESULT_MIN_LENGTH = 10

def main():
	f = open(INPUT_FILE_NAME)
	lines = f.readlines()
	f.close()

	bigram_list = make_bigram_list(lines)

	for i in range(TRY_NUM):
		word = "BOS"
		text = ""
		while True:
			word = random.choice(filter((lambda x: x[0] == word), bigram_list))[1]
			if word == "EOS":
				break
			text += word

		title_length = len(text.decode("utf-8"))

		if RESULT_MIN_LENGTH <= title_length:
			print text

#bigramリスト生成
def make_bigram_list(lines):
	bigram_list = []
	for line in lines:
		words_list =  ["BOS"] + line.split() + ["EOS"]
		for i,word in enumerate(words_list):
			if words_list[i] != "EOS":
				bigram_list.append([words_list[i],words_list[i+1]])
	return bigram_list

def option_parser():
	global INPUT_FILE_NAME

	usage = '使用方法: python {} INPUT_FILE_NAME'\
		.format(__file__)
	arguments = sys.argv

	#引数やオプションが指定されなかった場合,usageを表示してexitする
	if len(arguments) == 1:
		print usage
		sys.exit()

	arguments.pop(0) # ファイル自身を指す最初の引数を除去

	try:
		INPUT_FILE_NAME = arguments[0]
	except:
		print usage
		sys.exit()

if __name__ == "__main__":
	option_parser()
	main()