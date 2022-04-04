from random import choice
import numpy as np

class RandomPoints3D():
	"""Класс для генерирования случайных блужданий в трех измерениях."""

	def __init__(self, amount_points = 5000):
		"""Иницифлизирует количество  случаайных точек."""
		
		self.amp = amount_points
		self.x = [0]
		self.y = [0]
		self.z = [0]
		self.arr_z_y_x = []

	def x_get_step(self):
		"""Распределение по оси X."""
		self.x_dir = choice([-1, 1])
		self.x_dis = choice([i for i in range(0,8)])
		self.x_step = self.x_dir * self.x_dis
		return self.x_step

	def y_get_step(self):
		"""Распределение по оси X."""
		self.y_dir = choice([-1, 1])
		self.y_dis = choice([i for i in range(0,8)])
		self.y_step = self.y_dir * self.y_dis
		return self.y_step

	def z_get_step(self):
		"""Распределение по оси X."""
		self.z_dir = choice([-1, 1])
		self.z_dis = choice([i for i in range(0,8)])
		self.z_step = self.z_dir * self.z_dis
		return self.z_step

	def array_create(self):
		"""Создает матрицу ходов z_y_x."""
		self.arr_z_y_x = np.array([self.z, self.y, self.x])

	def random_walk(self):
		"""Генерация случайных точек."""
		while len(self.x) < self.amp:
			x1step = self.x_get_step()
			y1step = self.y_get_step()
			z1step = self.z_get_step()
			if x1step == 0 and y1step == 0 and z1step == 0:
				continue
			x_val = x1step + self.x[-1]
			y_val = y1step + self.y[-1]
			z_val = z1step + self.z[-1]
			self.x.append(x_val)
			self.y.append(y_val)
			self.z.append(z_val)
		self.array_create()

	def show_walk(self):
		"""Отображение  списков ходов."""
		print('X=',self.x)
		print('Y=',self.y)
		print('Z=',self.z)

	def data_array(self):
		"""Выводит и возвращает матрицу ходов."""

		print(self.arr_x_y_z)
		return self.arr_x_y_z

	def list_value(self, value = 'arr'):
		"""Вовзращает ходы по осям."""
		if value.lower() == 'x':
			return self.x
		elif value.lower() == 'y':
			return self.y
		elif value.lower() == 'z':
			return self.z
		elif value.lower() == 'arr':
			return self.data_array()

	def write_data(self):
		"""Записывает  атрибуты в файл."""
		
		file = 'data.txt'
		with open(file,'w', encoding='utf-8') as f:
			str_x, str_y, str_z = '', '', ''
			
			i = 0 
			while i < len(self.x):
				str_x += ' '+ str(self.x[i])
				str_y += ' '+str(self.y[i])
				str_z += ' '+ str(self.z[i])
				i +=1
			f.write('Значения X: \n')
			f.write(str_x)
			f.write('\nЗначения Y: \n')
			f.write(str_y)
			f.write('\nЗначения Z: \n')
			f.write(str_z)


