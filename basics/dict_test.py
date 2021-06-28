class TestDict:
	def test_dict_merge(self):
		"""
		测试字典合并
		"""
		dict1 = {"user":"test1"}
		dict2 = {"pwd":"123456"}

		dict3 = dict(dict1,**dict2)
		assert dict3["user"] == dict1["user"]
		assert dict3["pwd"] == dict2["pwd"]