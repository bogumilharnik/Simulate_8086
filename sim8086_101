# Symulator v.1.01

# f"cokolwiek_text{ax}" - tzw. fstring
# print(f"Pobieramy zawartość rejestru AX: {ax}")

ax = int(input("Podaj liczbę dla rejestru AX: "))
bx = int(input("Podaj liczbę dla rejestru BX: "))
cx = int(input("Podaj liczbę dla rejestru CX: "))
dx = int(input("Podaj liczbę dla rejestru DX: "))

print("wybierz operację: MOV, XCHG lub Q aby wyjść")

operacja = str(input("Podaj operację: "))
operacja1 = "MOV"
operacja2 = "XCHG"
operacja3 = "Q"


while operacja != operacja3:

    if operacja == operacja1:
            print("Podaj numer rejestru z którego przenosisz: AX | BX | CX | DX")
            nr_rejestru_z = str(input())
            print("Podaj numer rejestru do którego przenosisz: AX | BX | CX | DX")
            nr_rejestru_do = str(input())
            if nr_rejestru_z == 'AX'and nr_rejestru_do == 'BX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru AX: " + "ax")
                print(ax)
                print("Wykonujemy operację przeniesienia z rejstru AX do BX")
                rejestr_tmp = ax
                bx = ax
                print("Odczytujemy zawartość rejestru BX: " + "bx")
                print(bx)
                bx = rejestr_tmp
            elif nr_rejestru_z == 'AX'and nr_rejestru_do == 'CX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru AX: " + "ax")
                print(ax)
                print("Wykonujemy operację przeniesienia z rejstru AX do CX")
                rejestr_tmp = ax
                cx = ax
                print("Odczytujemy zawartość rejestru CX: " + "cx")
                print(cx)
                cx = rejestr_tmp
            elif nr_rejestru_z == 'AX'and nr_rejestru_do == 'DX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru AX: " + "ax")
                print(ax)
                print("Wykonujemy operację przeniesienia z rejstru AX do DX")
                rejestr_tmp = ax
                dx = ax
                print("Odczytujemy zawartość rejestru DX: " + "dx")
                print(dx)
                dx = rejestr_tmp
            elif nr_rejestru_z == 'BX'and nr_rejestru_do == 'AX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru BX: " + "bx")
                print(bx)
                print("Wykonujemy operację przeniesienia z rejstru BX do AX")
                rejestr_tmp = ax
                ax = bx
                print("Odczytujemy zawartość rejestru AX: " + "ax")
                print(bx)
                ax = rejestr_tmp
            elif nr_rejestru_z == 'BX'and nr_rejestru_do == 'CX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru BX: " + "bx")
                print(bx)
                print("Wykonujemy operację przeniesienia z rejstru BX do CX")
                rejestr_tmp = bx
                cx = bx
                print("Odczytujemy zawartość rejestru CX: " + "cx")
                print(cx)
                cx = rejestr_tmp
            elif nr_rejestru_z == 'BX'and nr_rejestru_do == 'DX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru BX: " + "bx")
                print(bx)
                print("Wykonujemy operację przeniesienia z rejstru BX do DX")
                rejestr_tmp = bx
                dx = bx
                print("Odczytujemy zawartość rejestru DX: " + "dx")
                print(dx)
                dx = rejestr_tmp
            elif nr_rejestru_z == 'CX'and nr_rejestru_do == 'AX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru CX: " + "cx")
                print(cx)
                print("Wykonujemy operację przeniesienia z rejstru CX do AX")
                rejestr_tmp = ax
                ax = cx
                print("Odczytujemy zawartość rejestru AX: " + "ax")
                print(ax)
                cx = rejestr_tmp
            elif nr_rejestru_z == 'CX'and nr_rejestru_do == 'BX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru CX: " + "cx")
                print(cx)
                print("Wykonujemy operację przeniesienia z rejstru CX do BX")
                rejestr_tmp = bx
                bx = cx
                print("Odczytujemy zawartość rejestru BX: " + "bx")
                print(bx)
                bx = rejestr_tmp
            elif nr_rejestru_z == 'CX'and nr_rejestru_do == 'DX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru CX: " + "cx")
                print(cx)
                print("Wykonujemy operację przeniesienia z rejstru CX do DX")
                rejestr_tmp = cx
                dx = cx
                print("Odczytujemy zawartość rejestru DX: " + "dx")
                print(dx)
                cx = rejestr_tmp
            elif nr_rejestru_z == 'DX'and nr_rejestru_do == 'AX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru DX: " + "dx")
                print(dx)
                print("Wykonujemy operację przeniesienia z rejstru CX do DX")
                rejestr_tmp = dx
                ax = dx
                print("Odczytujemy zawartość rejestru AX: " + "ax")
                print(ax)
                dx = rejestr_tmp
            elif nr_rejestru_z == 'DX'and nr_rejestru_do == 'BX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru DX: " + "bx")
                print(bx)
                print("Wykonujemy operację przeniesienia z rejstru CX do DX")
                rejestr_tmp = dx
                bx = dx
                print("Odczytujemy zawartość rejestru AX: " + "bx")
                print(bx)
                dx = rejestr_tmp
            elif nr_rejestru_z == 'DX'and nr_rejestru_do == 'CX':
                print("Wybrana operacja przeniesienia: " + operacja1)
                print("Pobieramy zawartość rejestru DX: " + "dx")
                print(cx)
                print("Wykonujemy operację przeniesienia z rejstru CX do DX")
                rejestr_tmp = dx
                cx = dx
                print("Odczytujemy zawartość rejestru AX: " + "ax")
                print(ax)
                dx = rejestr_tmp
            else:
                print("Błąd - nie wybrano operacji")
