a = input("Alegeti o valoare: ")
try:
    print(int(a))
    print(variabila_nedefinita)

except NameError:
    variabila_nedefinita = None
    print('Name error', e)
except ValueError:
    print("S-a intalnit o eroare")
    a = input("Alegeti o valoare: ")
except Exception as e:
    print(e)
# except NameError:
#     variabila_nedefinita = None
#     print('Name error')

else:
    print("S-a executat cu succes")
finally:
    print("Se executa oricum")
print("A trecut de blocul try-except", variabila_nedefinita)