class A:
    pass

class B(A):
    pass


a = A()
b = B()

print(isinstance(a,A))
print(isinstance(b,B))
print(isinstance(b,A))          # True / 모든 자식은 부모타입이다. b는 B타입과 동시에 A타입이다.
print(isinstance(a,B))          # False / 부모는 절대 자식타입이 될 수 없다.