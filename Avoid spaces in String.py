test_str = 'rakesh is best'
print("The original string is :" + str(test_str))
res = sum(not chr.isspace() for chr in test_str)
print("The characters frequency avoiding spaces : " + str(res))
