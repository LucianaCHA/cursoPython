# Por que usar my py test? para dar mas seguridad a nuestro codigo vsliando que los tipos de datos sean los correctos

# Para usarlo debemos instalarlo con pip install pytest

# unittest es una libreria de python que nos permite hacer pruebas unitarias


from unittest import TestCase
from prueba import suma

class PruebaTest(TestCase):
    def test_sin_argumentos(self):
        with self.assertRaises(TypeError):
            suma()
    def suma_argumentos_erroneos(self):
        with self.assertRaises(TypeError):
            suma(1,2,3)
            suma(None, None)
            suma(1, "2")
            suma([], {})

    def test_suma_correcta(self):
        self.assertEqual(suma(1,20), 21)
        self.assertEqual(suma(1,2), 3)
        self.assertEqual(suma(12,34), 46)
        self.assertEqual(suma(-15,5), -10)

# assert espera que la condicion sea verdadera, si no lo es, lanza un error

# notequal valida que dos cosas no sean iguales 
# self.assertEqual('hola', 'hola') test ok
# self.assertNotEqual('hola', 'hola') test falla

#assertTrue y assertFalse 

#self.asserTrue('hola') esto es true porque recibe algo
# self.asserFalse('hola') esto no es true porque recibe algo


# self.assertIs(firts, second , msg=None)
# self.assertIsNot(firts, second , msg=None) # valida si el first y second obj son el mismo objeto

class tst(TestCase):
    def test_in(self):
        self.assertIn('a', 'hola')
        self.assertIsInstance('hola', str) # isinstance valida si el primer argumento es una instancia del segundo argumento


#setUp y tearDown

# setUp se ejecuta antes de cada test (como beforeEach en jest)
# tearDown se ejecuta despues de cada test (como afterEach en jest)


class tst2(TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')
    def test_1(self):
        print('test_1')
    def test_2(self):
        print('test_2')
       
       
from unittest.mock import patch
import  json


class tst3(TestCase):
    @patch('prueba.suma')# patch es un decorador que nos permite mockear una funcion, recibe como parametro el nombre de la funcion a mockear
    def test_suma(self, mock_suma):
        mock_suma.return_value = 3
        self.assertEqual(suma(1,2), 3)
from prueba import obtener_juegos

class TestMock(TestCase):
    @patch('requests.get')
    def test_obtener_juegos(self, mock_get):
        with open('data.json', 'r') as file:
            data = json.load(file)

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = data

        self.assertEqual(obtener_juegos(), data)

# mockear error de api
from prueba import ejecutar_funcion

class TestMock2(TestCase):
    @patch('prueba.una_funcion')
    def test(self, mock_una_funcion):
        mock_una_funcion.side_effect = Exception('error')
        with self.assertRaises(Exception):
            ejecutar_funcion()

