#import xlwings as xw
import csv

class TestExcel:
	def myxlwings(self,file_name):
		app=xw.App(visible=False,add_book=False)
		wb=app.books.open(file_name)

		# sheet1 的a1的格式和内容复制到c1
		sht1 = wb.sheets["Sheet1"]
		range_a1 = sht1.range('A1')
		range_c1 = sht1.range('C1')

		range_a1.value='helloworld1.'
		range_a1.color = (30,100,200)
		print(range_a1.value)

		# 复制A1内容和格式到C1
		range_a1.copy(range_c1)
		print(range_c1.value)


		wb.save()
		wb.close()
		app.quit()

	def mycsv(self,file_name,header,rows):

		with open(file_name,'w',newline='')as f:
		    f_csv = csv.DictWriter(f,header)
		    f_csv.writeheader()
		    f_csv.writerows(rows)

	def test_csv_001(self):
		headers = ["name","age","sex"]
		rows = [
			{"name":"test1","age":"55","sex":"man"},
			{"name":"test2","age":"36","sex":"woman"},
		]

		self.mycsv(file_name="./test.csv",header=headers,rows=rows)

#t1 = TestExcel()
#t1.myxlwings(file_name='./test.xlsx')