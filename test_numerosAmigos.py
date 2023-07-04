import pytest
from numerosAmigos import numeros_amigos

def test_prueba1():
    assert numeros_amigos(1,2) == "1 y 2 no son amigos"
    
def test_prueba2():
    assert numeros_amigos(4,2) == "4 y 2 no son amigos"

def test_prueba3():
    assert numeros_amigos(220,284) == "220 y 284 son amigos"

def test_prueba4():
    assert numeros_amigos(1184,1210) == "1184 y 1210 son amigos"

def test_prueba5():
    assert numeros_amigos(50,100) == "50 y 100 no son amigos"

def test_prueba6():
    assert numeros_amigos(10,11) == "10 y 11 son amigos"

def test_prueba7():
    assert numeros_amigos(3,14) == "3 y 14 son amigos"

def test_prueba8():
    assert numeros_amigos(177,288) == "177 y 288 son amigos"

def test_prueba9():
    assert numeros_amigos(2620,2924) == "2620 y 2924 no son amigos"

def test_prueba10():
    assert numeros_amigos(1,0) == "1 y 0 son amigos"

if __name__ == '__main__':
    test_prueba1()
    test_prueba2()
    test_prueba3()
    test_prueba4()
    test_prueba5()
    test_prueba6()
    test_prueba7()
    test_prueba8()
    test_prueba9()
    test_prueba10()