import unittest
from random_points import RandomPoints

class TestRandomPoints(unittest.TestCase):
	"""Тесты для класса "RandomPoints.py"."""

	def setUp(self):
		"""Создает экземпляр случайного блуждения."""

		self.my_points = RandomPoints()

	def test_x_get_step(self):
		"""Проверяет распределние по оси X."""
		self.my_points.x_get_step()
		self.assertIn(self.my_points.x_direction, [1,-1])
		self.assertIn(self.my_points.x_distance, [0, 1, 2, 3 ,4 ,5 ,6 ,7])
		self.assertEqual(self.my_points.x_step, self.my_points.x_direction * self.my_points.x_distance)

	def test_y_get_step(self):
		"""Проверяет распределние по оси X."""
		
		self.my_points.y_get_step()
		self.assertIn(self.my_points.y_direction, [1,-1])
		self.assertIn(self.my_points.y_distance, [0, 1, 2, 3 ,4 ,5 ,6 ,7])
		self.assertEqual(self.my_points.y_step, self.my_points.y_direction * self.my_points.y_distance)

	def test_random_walk(self):
		"""Проверяет количество  случайных точек."""

		self.my_points.random_walk()
		self.assertEqual(len(self.my_points.x_val), self.my_points.nmb_p)
		self.assertEqual(len(self.my_points.y_val), self.my_points.nmb_p)

	def test_return_listX_walk(self):
		""""Возвращает ли метод return_list_walk список значений 'x'?"""

		self.my_points.random_walk()
		self.v1 = self.my_points.return_list_walk('x')
		self.assertEqual(self.v1, self.my_points.x_val)

	def test_return_listY_walk(self):
		"""Возвращает ли метод return_list_walk список значений 'y'?"""

		self.my_points.random_walk()
		self.v2 = self.my_points.return_list_walk('y')
		self.assertEqual(self.v2, self.my_points.y_val)

	def test_return_list_walkNone(self):
		"""Возвращает ли метод return_list_walk список значений 'None'?"""

		self.my_points.random_walk()
		self.v2 = self.my_points.return_list_walk('c')
		self.assertEqual(self.v2, None)








if __name__ == '__main__':
	unittest.main()