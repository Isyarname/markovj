from markova import MarkovChains

mch = MarkovChains("t.txt", sp="буква")
mch.learn()
ls = mch.generateSequence(15, auth="<start>")
txt = ""
for i in ls:
	txt += i
print(txt)