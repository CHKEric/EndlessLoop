import easygui
#Easygui text:
#easygui.msgbox('1')
import random
#Random Text:
#a = random.randint(0,9) 
#print(a)
import pygame
import time
import sys
# filepath = r""
# pygame.mixer.music.load(filepath)
# pygame.mixer.music.play(start=0.0)


#Preparation Module
def Pre():
	global end,good
	end = 0
	good = 0
	pygame.init()
	pygame.mixer.init()


#start Module:
def Start():
	global bgm
	bgm = r'Sound/bgm.mp3'
	pygame.mixer.music.load(bgm) 
	pygame.mixer.music.play(loops=-1,start=0.0)
	forward = easygui.buttonbox('说在前面：本程序灵感来源于Bilibili-GoldenEggs作品《无尽循环》，该程序仅用于娱乐,有Bug是特性(bushi)[手动狗头]',choices=['好'],title=['Start'])
	if forward == '好':
		start = easygui.buttonbox('确定开始？无尽循环，即将开始！',choices=['开始','我怂了'],title='Q0')
		if start == '我怂了' :
			easygui.buttonbox('怂也得上！',choices=['上'],title='Q0')
			First.Q1()
		elif start == '开始':
			First.Q1()
		else:
			Exit()
	else:
		Exit()


#Exit Module
def Exit():
	Q = easygui.buttonbox('正在重新开始,如关闭默认关闭程序。',choices=['重启','不想玩了，关闭程序'])
	if Q == '重启':
		Start()
	else:
		sys.exit(0)


#Game Module:
#First cycle:
class First():
	def Q1():
		q1_1 = easygui.buttonbox('一觉起来，你看到今天是20XX年5月31日，外面雨很大，你拿上你新磨得钻石剑，准备出门。你偶然看到南瓜灯，猛然想起了一个带着南瓜面具的杀手，你没多想，直接出门了。',choices=['继续'],title='1-Q1.1')
		if q1_1 == '继续':			
			q1_2 = easygui.buttonbox('一出门，你看见了一个告示牌,上面写：别回头。你决定',choices=['相信告示牌','回头看看？'],title='1-Q1.2')
			if q1_2 == '相信告示牌':
				First.Q2()
			elif q1_2 == '回头看看？':
				Third.Q0_1()
			else:
				Exit()
		else:
			Exit()
	def Q2():
		Q2 = easygui.buttonbox('你向前走，发现一个神秘人，他头上戴着南瓜头套，身上穿着金甲，他丢下一颗红宝石，你发现这是你家里收藏的，你决定',choices=['追！','没意思'],title='1-Q2')
		if Q2 == '追！':
			First.Q3()
		elif Q2 == '没意思':
			Third.Q0_2()
		else:
			Exit()
	def Q3():
		q3 = easygui.buttonbox('你跟着那个神秘人,发现了一个巨大的藤蔓，你紧跟着他,你跟着他上到了一个由云组成的藤蔓，你询问那个神秘人:"你是谁？你到底想干什么？"，因为他头上戴着南瓜头套，话说不清楚，你认为他一定是有阴谋，拿起钻石剑就把他打下了高台，他粉身碎骨。你回头，那有一个平台，上面写着：尘封的真相。你决定',choices=['跳进去看看！','是阴谋，回去了'],title=['1-Q3'])
		if q3 == '跳进去看看！':
			First.Q4()
		elif q3 == '是阴谋，回去了':
			Third.Q0_3()
		else:
			Exit()
	def Q4():
		ran = random.randint(0,9)
		q4 = easygui.buttonbox('你没多犹豫，直接跳了下去。里面是一面墙，上面有几行字。你细细看着，吓了一大跳。你想到了那个神秘人。你回头，看到了那套神秘人的装备——南瓜头套,和一套金甲。旁边的箱子装着一些武器，和一个火箭喷射器。你没有退路，穿上了它。你头一昏，醒来时已经在外面了。你飞到了你家，确实有一个和自己一摸一样的人。你换上金甲，拿出了斧头，一把砍了下去。',choices=['砍他！（%20几率）','直接失败','查看文字'],title=['1-Q4'])
		if q4 == '砍他！（%20几率）':
			if ran <= 1:
				First.KillWin()
			elif ran > 1:
				First.Q5()
		elif q4 == '直接失败':
			First.Q5()
		elif q4 == '查看文字':
			First.curse()
		else:
			Exit()
	def Q5():
		ran = random.randint(0,9)
		q5=easygui.buttonbox('他侥幸躲了过去。你气急败坏，紧紧跟着他。你手上已经转备好了剧毒药水，只要他一犹豫，他将被毒杀。时机到了，你拿起药水，狠狠丢了过去。',choices=['砸他！（%20几率）','直接失败'],title=['1-Q5'])
		if q5 == '砸他！（%20几率）':
			if ran <= 1:
				First.KillWin()
			elif ran > 1:
				First.Q6()
		elif q5 == '直接失败':
			First.Q6()
		else:
			Exit()
	def Q6():
		ran = random.randint(0,9)
		q6 = easygui.buttonbox('真是大慈大悲的观世音菩萨保佑他，又没有打中。你暗暗咒骂，跟踪他，上了那根大藤蔓。你看着他像你一样，打下了那个‘神秘人’，然后看到了那个名为‘尘封的真相’的高台。你心想，快没机会了，说罢，射出了箭。',choices=['射死他！（%20几率）','直接失败'],title=['1-Q6'])
		if q6 == '射死他！（%20几率）':
			if ran <= 1:
				First.KillWin()
			elif ran > 1:
				First.Q7()
		elif q6 == '直接失败':
			First.Q7()
		else:
			Exit()
	def Q7():
		ran = random.randint(0,9)
		q7 = easygui.buttonbox('他跳下去了！你十分焦急，跟着他一跳，没想到，传送门神秘的消失了，你直直坠下，掉入了一地洞。你走过一弯又一弯，看到了另一面墙。那，就是所谓的‘时间表’。你毛骨悚然，恍然大悟，你决定',choices=['当救兵（80%）','直接失败','查看时间表'],title=['1-Q7'])
		if q7 == '当救兵（80%）':
			if ran <= 1:
				Third.heroDie1()
			elif ran >= 2:
			 	First.Q8()
		elif q7 == '直接失败':
			Third.heroDie1()
		elif q7 == '查看时间表':
			First.fir_time()
		else:
			Exit()
	def Q8():
		ran = random.randint(0,9)
		q8 = easygui.buttonbox('他还是跟上来了。你将他引到了一片平地，丢下了你珍藏的红宝石，静候他上门。',choices=['引诱（80%）','直接失败'],title=['1-Q8'])
		if q8 == '引诱（80%）':
			if ran <= 1:
				Third.heroDie02()
			elif ran >= 2:
			 	First.End()
		elif q8 == '直接失败':
			Third.heroDie2()
		else:
			Exit()
	def End():
		global end
		global good
		ran = random.randint(0,9)
		filepath2 = r"Sound/zero2.mp3";
		if end <= 1:
				q9 = easygui.buttonbox('你和他走上了顶端，他和你一样，问了"你是谁？你到底想干什么？"。你迅速地回答他，“我们不要在自相残杀了，我们需要......”话未说完，他拿起剑就把你砍下深崖，你还未反应过来，当场暴毙。',choices=['继续'],title=['died'])
				q9_2 = easygui.buttonbox('【             假结局              】(剧情杀？试试再来一次！）',choices=['重来（80%第一循环，20%第三循环）'],title=['BadEnd0'])
				time.sleep(0)
				end = end + 1
				if q9_2 == '重来（80%第一循环，20%第三循环）':
					if ran <= 2:
						Third.Q1()				
					elif ran >= 3:
						First.Q1()
				else:
					Exit()
		elif end > 1 and ran <= 3:
				q9_3 = easygui.buttonbox('你和他走上了顶端，他和你一样，问了"你是谁？你到底想干什么？"。你决定',choices=['告诉，真相？','趁现在，跳！'],title=['WillWin'])
				if q9_3 == '告诉，真相？':
					easygui.buttonbox('你迅速地回答他，“我们不要在自相残杀了，我们需要......”话未说完，他拿起剑就把你砍下深崖，你还未反应过来，当场暴毙。',choices=['继续'],title=['died'])
					q9_2 = easygui.buttonbox('【             假结局              】（剧情杀？试试再来一次！）',choices=['重来（80%第一循环，20%第三循环）'],title=['BadEnd1'])
					time.sleep(0)
					end = end + 1
					if q9_2 == '重来（80%第一循环，20%第三循环）':
						if ran <= 2:
							Third.Q1()			
						elif ran >= 3:
							First.Q1()
					else:
						Exit()
				elif q9_3 == '趁现在，跳！':
					good = good + 1
					pygame.mixer.music.load(filepath2)
					pygame.mixer.music.play(start=0.0)
					q9_4 = easygui.buttonbox('你奋力一跳，飞速下降，你掉入下方的湖中，湖旁是一次又一次被击杀的“救兵”的头颅。你开始沉入水中，头套让你喘不过气来……恍惚间，你已醒了。你从床上起来，感觉循环好像一个梦。窗外阵阵鸟叫声，你看表，今天是20XX年6月1日，天气晴。你再次来到了那个时间表的位置，藤蔓已然消失，你进了洞，只见那副墙上，赫然写着：第四循环体……【真结局】 【BGM：洛天依-〇】',choices=['第一循环(通关奖励：任意选）','第二循环','第三循环','彩蛋'],title=['GoodEnd1'])
					pygame.mixer.music.stop()
					pygame.mixer.music.load(bgm)
					pygame.mixer.music.play(start=0.0,loops=-1)
					if q9_4 == '第一循环':
						First.Q1()
					elif q9_4 == '第二循环':
						Second.Q1()
					elif q9_4 == '第三循环':
						Third.Q1()
					elif q9_4 == '彩蛋':
						Third.surprise()
					else:
						Exit()


		else:
			q9_5 = easygui.buttonbox('你和他走上了顶端，他和你一样，问了"你是谁？你到底想干什么？"。你迅速地回答他，“我们不要在自相残杀了，我们需要......”话未说完，他拿起剑就把你砍下深崖，你还未反应过来，当场暴毙。',choices=['继续'],title=['died'])
			q9_6 = easygui.buttonbox('【             假结局              】（剧情杀？试试再来一次！）',choices=['重来（80%第一循环，20%第三循环）'],title=['BadEnd2'])
			time.sleep(0)
			end = end + 1
			if q9_5 == "重来（80%第一循环，20%第三循环）":
				if ran <= 2:
					Third.Q1()			
				elif ran >= 3:
					First.Q1()
			else:
				Exit()

	def KillWin():
		kw = easygui.buttonbox('你杀死他后，回到了家，发现时间并没有变，你突然想起了自己不知在哪看过的‘时间表’，你大呼被骗。你发现需要让每个人都活着。',choices=['你决定当救兵'],title=['killWin'])
		if kw == '你决定当救兵':
			Third.Q8()
		else:
			Exit()


	def fir_time():
		time1 = easygui.buttonbox('时间表：',image='Image/time-fir.png',choices=['返回'])
		if time1 == '返回':
			First.Q7()
		elif time1 == 'Image/time-fir.png':
			Second.fir_time()
		else:
			Exit()

	def curse():
		curse = easygui.buttonbox('墙上の字：',image='Image/curse.png',choices=['返回'])
		if curse == '返回':
			First.Q4()
		elif curse == 'Image/curse.png':
			First.curse()
		else:
			Exit()


#Second cycle:
class Second():
	def Q1():
		q1_1 = easygui.buttonbox('一觉起来，你看到今天是20XX年5月31日，外面雨很大，你拿上你新磨得钻石剑，准备出门。你偶然看到南瓜灯，猛然想起了一个带着南瓜面具的杀手，你没多想，直接出门了。',choices=['继续'],title='2-Q1.1')
		if q1_1 == '继续':			
			q1_2 = easygui.buttonbox('',choices=['向前走就对了','回头看看？'],title='2-Q1.2')
			if q1_2 == '向前走就对了':
				Second.Q2()
			elif q1_2 == '回头看看？':
				Third.Q0_1()
			else:
				Exit()
		else:
			Exit()

	def Q2():
		Q2 = easygui.buttonbox('你远眺，好大的藤蔓啊！',choices=['冲','没意思'],title='2-Q2')
		if Q2 == '冲':
			Second.Q3()
		elif Q2 == '没意思':
			Second.died()
		else:
			Exit()
	def Q3():
		q3 = easygui.buttonbox('你走上了那个藤蔓，到了一个平台。那有一个高台，上面写着：尘封的真相。你决定',choices=['跳进去看看！','是阴谋，回去了'],title=['2-Q3'])
		ran2 = random.randint(0,100)
		if q3 == '跳进去看看！' and good < 1:
			if ran2 <= 1:
				Third.surprise()
			else:
				Third.Q4()
		elif q3 == '跳进去看看！' and good >= 1:
			if ran2 <= 30:
				Third.wSurpr()
			else:
				Third.Q4()
		elif q3 == '是阴谋，回去了':
			Second.died()
		else:
			Exit()
	def Q5():
		q5=easygui.buttonbox('他侥幸躲了过去。你气急败坏，紧紧跟着他。你手上已经转备好了剧毒药水，只要他一犹豫，他将被毒杀。时机到了，你拿起药水，狠狠丢了过去。',choices=['砸他！（%20几率）','直接失败'],title=['2-Q5'])
		ran = random.randint(0,9)
		if q5 == '砸他！（%20几率）':
			if ran <= 1:
				First.KillWin()
			elif ran > 1:
				Second.Q6()
		elif q5 == '直接失败':
			Second.Q6()
		else:
			Exit()
	def Q6():
		q6 = easygui.buttonbox('真是大慈大悲的观世音菩萨保佑他，又没有打中。你暗暗咒骂，跟踪他，上了那根大藤蔓。你看着他像你一样，打下了那个‘神秘人’，然后看到了那个名为‘尘封的真相’的高台。你心想，快没机会了，说罢，射出了箭。',choices=['射死他！（%20几率）','直接失败'],title=['3-Q6'])
		ran = random.randint(0,9)
		if q6 == '射死他！（%20几率）':
			if ran <= 1:
				First.KillWin()
			elif ran > 1:
				Second.Q7()
		elif q6 == '直接失败':
			Second.Q7()
		else:
			Exit()
	def Q7():
		q7 = easygui.buttonbox('他跳下去了！你十分焦急，跟着他一跳，没想到，传送门神秘的消失了，你直直坠下，掉入了一地洞。你走过一弯又一弯，看到了另一面墙。那，就是所谓的‘时间表’。你毛骨悚然，恍然大悟，你决定',choices=['当救兵','直接失败','查看时间表'],title=['3-Q7'])
		ran = random.randint(0,9)
		if q7 == '当救兵':
			Third.Q8()
		elif q7 == '直接失败':
			Third.heroDie1()
		elif q7 == '查看时间表':
			Second.sec_time()
		else:
			Exit()
	
	def sec_time():
		time1 = easygui.buttonbox('时间表：',image='Image/time-thi.png',choices=['返回'])
		if time1 == '返回':
			Second.Q7()
		elif time1 == 'Image/time-thi.png':
			Second.sec_time()
		else:
			Exit()
	def died():
		d = easygui.buttonbox('你刚想返回，一个人拿着武器直接杀来。',choices = ['重生'],title='died-2')
		if d == '重生':
			Second.Q1()
		else:
			Exit()

#Third cycle:
class Third():
	def Q0_1():
		q0 = easygui.buttonbox('“啊~~~”一个杀手拿着斧子朝你冲来。',choices=['重生[你，木得选择]'],title='3-Died-1')
		if q0 == '重生[你，木得选择]':
			Third.Q1()
		else:
			Exit()
	def Q0_2():
		q0 = easygui.buttonbox('“啊！！！怎么回事啊！！！”一个杀手拿着毒药水向你丢来。',choices=['重生[你，木得选择]'],title='3-Died-2')
		if q0 == '重生[你，木得选择]':
			Third.Q1()
		else:
			Exit()
	def Q0_3():
		q0 = easygui.buttonbox('“这是什么？箭！啊~~~”一个杀手朝着你射箭。',choices=['重生[你，木得选择]'],title='3-Died-3')
		if q0 == '重生[你，木得选择]':
			Third.Q1()
		else:
			Exit()
	def heroDie1():
		q0 = easygui.buttonbox('你在那个你曾经看到告示牌的地方放下了告示牌，上面还是写：别回头！你静候他被引诱来，一阵急促的脚步声，你暗想不妙，那小子没信！杀手的斧子朝你袭来。',choices=['重生[你，木得选择]'],title='HeroDied-1')
		if q0 == '重生[你，木得选择]':
			Third.Q1()
		else:
			Exit()
	def heroDie02():
		q0 = easygui.buttonbox('你静候他被引诱来，一阵急促的脚步声和药瓶打碎的声音，你暗想不妙，那小子没信！杀手的药水朝你袭来。',choices=['重生[你，木得选择]'],title='HeroDied-2')
		if q0 == '重生[你，木得选择]':
			Second.Q1()
		else:
			Exit()
	def Q1():
		q1 = easygui.buttonbox('一觉起来，你看到今天是20XX年5月31日，外面雨很大，你拿上你新磨得钻石剑，准备出门。你偶然看到南瓜灯，猛然想起了一个带着南瓜面具的杀手，你没多想，直接出门了。',choices=['继续'],title='3-Q1')
		if q1 == '继续':
			Third.Q2()
		else:
			Exit()
	def Q2():
		q2=easygui.buttonbox('一出门，你看见了一个告示牌，上面写：“别回头，直接走”,你决定',choices=['相信告示牌','再回头看一眼(再？)'],title=('3-Q2'))
		if q2 == '相信告示牌':
			Third.Q3_1()
		elif q2 == '再回头看一眼(再？)':
			Third.Q3_2()
		else:
			Exit()
	def Q3_1():
		q3_1 = easygui.buttonbox('你向前走，看到了一个神秘人，他丢下了一个东西：你珍藏的宝石。你越发的奇怪，紧跟他上前。你跟着他，上了一根巨大的藤蔓。那根藤蔓的尽头是一个大平台，他站在边缘，你乘机拿出了你的剑，问他："你是谁？你到底想干什么？"他焦急的回答：“！@#￥……#%￥&&*%*……￥……￥#%”，你不明所以,拿出大剑就把他打了下去。你回头一看，那里有一个传送门，你走了上去，上面写着：尘封的真相。你决定',choices=['跳！'],title=['3-Q3'])
		ran2 = random.randint(0,100)
		if q3_1 == '跳！' and good < 1:
			if ran2 <= 1:
				Third.surprise()
			else:
				Third.Q4()
		elif q3_1 == '跳！' and good >= 1:
			if ran2 <= 30:
				Third.wSurpr()
			else:
				Third.Q4()
		else:
			Exit()
	def Q3_2():
		q3_2 = easygui.buttonbox('你回头，雨很大，淅淅沥沥。你环视一圈，转过头去，向前走。',choices=['继续'],title=['3-Q3_2'])
		if q3_2 == '继续':
			Third.Q3_1()
		else:
			Exit()	

	def surprise():
		surpr=easygui.buttonbox('‘大人，这是我再次策划的好戏。’你到了一个未知的地方,看见两个人在讲话。‘A，B，和C三个人在这个地图里，相杀相救，被假的诅咒和"真"的时间表所误导，无限循环永无止境，有1,2,3循环……’‘这保险吗？你亲爱的演员又出来了。’‘欧，大人，这个传送门可能有一点故障，我很快就修好。（你被传送回初始循环）【恭喜触发彩蛋结局   ‘对欧皇体质的大神膜拜，触发难度为1%！[秘密：即便是真结局直通车，也是1%]’】',choices=['继续'],title=['彩蛋'])
		if surpr == '继续':
			First.Q1()
		else:
			Exit()

	def wSurpr():
		ws = easygui.buttonbox('‘大人，这是我再次策划的好戏。’你到了一个未知的地方,看见两个人在讲话。‘A，B，和C三个人在这个地图里，相杀相救，被假的诅咒和"真"的时间表所误导，无限循环永无止境，有1,2,3循环……’‘这保险吗？你亲爱的演员又出来了。’‘欧，大人，这个传送门可能有一点故障，我很快就修好。（你被传送回初始循环）【恭喜触发彩蛋结局‘真结局奖励，达成难度为30%，真结局直通车概率为99%’】',choices=['继续'],title=['彩蛋'])
		if ws == '继续':
			First.Q1()
		else:
			Exit()

	def Q4():
		q4 = easygui.buttonbox('你没多犹豫，直接跳了下去。里面是一面墙，上面有几行字。你细细看着，吓了一大跳。你想到了那个神秘人。你回头，看到了那套神秘人的装备——南瓜头套,和一套金甲。旁边的箱子装着一些武器，和一个火箭喷射器。你没有退路，穿上了它。你头一昏，醒来时已经在外面了。你飞到了你家，确实有一个和自己一摸一样的人。你换上金甲，拿出了斧头，一把砍了下去。',choices=['砍他！（%20几率）','直接失败','查看文字'],title=['3-Q4'])
		ran = random.randint(0,9)
		if q4 == '砍他！（%20几率）':
			if ran <= 1:
				First.KillWin()
			elif ran > 1:
				Second.Q5()
		elif q4 == '直接失败':
			Second.Q5()
		elif q4 == '查看文字':
			Third.curse()
		else:
			Exit()
	def Q8():
		q8 = easygui.buttonbox('你在原来的地方放下了那个告示牌，上面写‘别回头’。他还是跟上来了。你将他引到了一片平地，丢下了你珍藏的红宝石，静候他上门。',choices=['引诱','直接失败'],title=['3-Q8'])
		ran = random.randint(0,9)
		if q8 == '引诱':
			Third.End()
		elif q8 == '直接失败':
			Second.Q1()
		else:
			Exit()
	def End():
		filepath2 = r"Sound/zero2.mp3";
		# 加载音乐
		global end
		global good
		ran = random.randint(0,9)
		if end <= 1:
				q9 = easygui.buttonbox('你和他走上了顶端，他和你一样，问了"你是谁？你到底想干什么？"。你迅速地回答他，“我们不要在自相残杀了，我们需要......”话未说完，他拿起剑就把你砍下深崖，你还未反应过来，当场暴毙。',choices=['继续'],title=['died'])
				q9_2 = easygui.buttonbox('【             假结局              】（剧情杀？试试再来一次！）',choices=['重来（40%第一循环，60%第三循环）'],title=['BadEnd3'])
				end += 1
				time.sleep(0)
				if q9_2 == "重来（40%第一循环，60%第三循环）":
					if ran <= 6:
						Third.Q1()				
					elif ran >= 4:
						First.Q1()
				else:
					Exit()
		elif end > 1 and ran <= 3:
			q9_3 = easygui.buttonbox('你和他走上了顶端，他和你一样，问了"你是谁？你到底想干什么？"。你决定',choices=['告诉，真相？','趁现在，跳！'],title=['WillWin'])
			if q9_3 == '告诉，真相？':
				easygui.buttonbox('你迅速地回答他，“我们不要在自相残杀了，我们需要......”话未说完，他拿起剑就把你砍下深崖，你还未反应过来，当场暴毙。',choices=['继续'],title=['died'])
				q9_2 = easygui.buttonbox('【             假结局              】（剧情杀？试试再来一次！）',choices=['重来（40%第一循环，60%第三循环）'],title=['BadEnd4'])
				end += 1
				if q9_2 == "重来（40%第一循环，60%第三循环）":
					if ran <= 5:
						Third.Q1()			
					elif ran >= 6:
						first.Q1()
				else:
					Exit()
			elif q9_3 == '趁现在，跳！':
				good = good + 1
				pygame.mixer.music.load(filepath2)
				pygame.mixer.music.play(start=0.0)
				q9_4 = easygui.buttonbox('你奋力一跳，飞速下降，你掉入下方的湖中，湖旁是一次又一次被击杀的“救兵”的头颅。你开始沉入水中，头套让你喘不过气来……恍惚间，你已醒了。你从床上起来，感觉循环好像一个梦。窗外阵阵鸟叫声，你看表，今天是20XX年6月1日，天气晴。你再次来到了那个时间表的位置，藤蔓已然消失，你进了洞，只见那副墙上，赫然写着：第四循环体……【真结局】 【BGM：洛天依-〇】',choices=['第一循环(通关奖励：任意选）','第二循环','第三循环','彩蛋'],title=['GoodEnd2'])
				pygame.mixer.music.stop()
				pygame.mixer.music.load(bgm)
				pygame.mixer.music.play(start=0.0,loops=-1)
				if q9_4 == '第一循环(通关奖励：任意选）':
					First.Q1()
				elif q9_4 == '第二循环':
					Second.Q1()
				elif q9_4 == '第三循环':
					Third.Q1()
				elif q9_4 == '彩蛋':
					ran3 = random.randint(1,100)
					if ran3 == 100:
						Third.surprise()
					elif ran3 <= 99:
						Third.wSurpr()
					else:
						Exit()
				else:
					Exit()

			else:
				Exit()

		else:
			q9_5 = easygui.buttonbox('你和他走上了顶端，他和你一样，问了"你是谁？你到底想干什么？"。你迅速地回答他，“我们不要在自相残杀了，我们需要......”话未说完，他拿起剑就把你砍下深崖，你还未反应过来，当场暴毙。',choices=['继续'],title=['died'])
			q9_6 = easygui.buttonbox('【             假结局              】',choices=['重来（40%第一循环，60%第三循环）'],title=['BadEnd5'])
			time.sleep(0)
			end = end + 1
			if q9_6 == "重来（40%第一循环，60%第三循环）":
				if ran <= 5:
					Third.Q1()			
				elif ran >= 6:
					First.Q1()
			else:
				Exit()
			
	def curse():
		curse = easygui.buttonbox('墙上の字：',image='Image/curse.png',choices=['返回'])
		if curse == '返回':
			Third.Q4()
		elif curse == 'Image/curse.png':
			Third.curse()
		else:
			Exit()


#Run program：
Pre()
Start()




###思路###
#1，假结局【1，3】后有几率直接到达第三循环（80%第一循环，20%第三循环）X
#2，假结局【2】后有几率直接到达第三循环（40%第一循环，60%第三循环）X
#3，成为第二循环萌新：在第三循环作为救兵被杀死
#4，成为第二循环杀手：在第三循环作为萌新杀死救兵