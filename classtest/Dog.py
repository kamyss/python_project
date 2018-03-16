class Shop():
	'''一个餐馆的对象操作'''	
	def __init__(self,shop_type,shop_name):
		self.shop_type=shop_type
		self.shop_name=shop_name
	def get_title_shop_type(self):
		shop_name=self.shop_name
		return shop_name.title()
#shop=Shop('canyincate','xiaochihaha')
class Sshop(Shop):
	def __init__(self,shop_type,shop_name):
		super().__init__(shop_type,shop_name)
	def get_title_shop_type(self):
		shop_name='666666'
		return shop_name.title()
#实例化子类
sshop=Sshop('xiaocanyindian','xiaochihaha2');
print(sshop.get_title_shop_type())
		