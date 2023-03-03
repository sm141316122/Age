drive = input("有沒有開過車?: ")
if drive != "有" and drive != "沒有":
	print("只能輸入 有/沒有")
	raise SystemExit

age = int(input("你的年齡是?: "))
if drive == "有" and age < 18:
	print("沒有駕照不能開車")
elif drive == "有" and age >= 18:
	print("恭喜! 你可以到任何地方")
elif drive == "沒有" and age >= 18:
	print("你已經可以考駕照了 快去考")
else:
	print("18歲才可以考駕照喔")
