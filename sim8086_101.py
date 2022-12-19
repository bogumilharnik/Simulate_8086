# Symulator v.1.02

# f"cokolwiek_text{ax}" - tzw. fstring
# print(f"Pobieramy zawartość rejestru AX: {ax}")

ax = int(input("Podaj liczbę dla rejestru AX: "))
bx = int(input("Podaj liczbę dla rejestru BX: "))
cx = int(input("Podaj liczbę dla rejestru CX: "))
dx = int(input("Podaj liczbę dla rejestru DX: "))

print("wybierz operację: MOV, XCHG lub Q aby wyjść")

wyjscie = str.upper("q")

while wyjscie != False:

    operacja = str.upper(input("Podaj operację: "))
    operacja1 = "MOV"
    operacja2 = "XCHG"
    # wyjscie = "Q"

    if operacja == operacja1:

        print("Podaj numer rejestru z którego przenosisz: AX | BX | CX | DX")
        nr_rejestru_z = str.upper(input())
        print("Podaj numer rejestru do którego przenosisz: AX | BX | CX | DX")
        nr_rejestru_do = str.upper(input())
        if nr_rejestru_z == 'AX' and nr_rejestru_do == 'BX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru AX: " + "ax")
            print(ax)
            print("Wykonujemy operację przeniesienia z rejestru AX do BX")
            rejestr_tmp = ax
            bx = ax
            print("Odczytujemy zawartość rejestru BX: " + "bx")
            print(bx)
            bx = rejestr_tmp
        elif nr_rejestru_z == 'AX' and nr_rejestru_do == 'CX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru AX: " + "ax")
            print(ax)
            print("Wykonujemy operację przeniesienia z rejestru AX do CX")
            rejestr_tmp = ax
            cx = ax
            print("Odczytujemy zawartość rejestru CX: " + "cx")
            print(cx)
            cx = rejestr_tmp
        elif nr_rejestru_z == 'AX' and nr_rejestru_do == 'DX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru AX: " + "ax")
            print(ax)
            print("Wykonujemy operację przeniesienia z rejestru AX do DX")
            rejestr_tmp = ax
            dx = ax
            print("Odczytujemy zawartość rejestru DX: " + "dx")
            print(dx)
            dx = rejestr_tmp
        elif nr_rejestru_z == 'BX' and nr_rejestru_do == 'AX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru BX: " + "bx")
            print(bx)
            print("Wykonujemy operację przeniesienia z rejestru BX do AX")
            rejestr_tmp = ax
            ax = bx
            print("Odczytujemy zawartość rejestru AX: " + "ax")
            print(bx)
            ax = rejestr_tmp
        elif nr_rejestru_z == 'BX' and nr_rejestru_do == 'CX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru BX: " + "bx")
            print(bx)
            print("Wykonujemy operację przeniesienia z rejestru BX do CX")
            rejestr_tmp = bx
            cx = bx
            print("Odczytujemy zawartość rejestru CX: " + "cx")
            print(cx)
            cx = rejestr_tmp
        elif nr_rejestru_z == 'BX' and nr_rejestru_do == 'DX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru BX: " + "bx")
            print(bx)
            print("Wykonujemy operację przeniesienia z rejestru BX do DX")
            rejestr_tmp = bx
            dx = bx
            print("Odczytujemy zawartość rejestru DX: " + "dx")
            print(dx)
            dx = rejestr_tmp
        elif nr_rejestru_z == 'CX' and nr_rejestru_do == 'AX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru CX: " + "cx")
            print(cx)
            print("Wykonujemy operację przeniesienia z rejestru CX do AX")
            rejestr_tmp = ax
            ax = cx
            print("Odczytujemy zawartość rejestru AX: " + "ax")
            print(ax)
            cx = rejestr_tmp
        elif nr_rejestru_z == 'CX' and nr_rejestru_do == 'BX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru CX: " + "cx")
            print(cx)
            print("Wykonujemy operację przeniesienia z rejestru CX do BX")
            rejestr_tmp = bx
            bx = cx
            print("Odczytujemy zawartość rejestru BX: " + "bx")
            print(bx)
            bx = rejestr_tmp
        elif nr_rejestru_z == 'CX' and nr_rejestru_do == 'DX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru CX: " + "cx")
            print(cx)
            print("Wykonujemy operację przeniesienia z rejestru CX do DX")
            rejestr_tmp = cx
            dx = cx
            print("Odczytujemy zawartość rejestru DX: " + "dx")
            print(dx)
            cx = rejestr_tmp
        elif nr_rejestru_z == 'DX' and nr_rejestru_do == 'AX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru DX: " + "dx")
            print(dx)
            print("Wykonujemy operację przeniesienia z rejestru CX do DX")
            rejestr_tmp = dx
            ax = dx
            print("Odczytujemy zawartość rejestru AX: " + "ax")
            print(ax)
            dx = rejestr_tmp
        elif nr_rejestru_z == 'DX' and nr_rejestru_do == 'BX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru DX: " + "bx")
            print(bx)
            print("Wykonujemy operację przeniesienia z rejestru CX do DX")
            rejestr_tmp = dx
            bx = dx
            print("Odczytujemy zawartość rejestru AX: " + "bx")
            print(bx)
            dx = rejestr_tmp
        elif nr_rejestru_z == 'DX' and nr_rejestru_do == 'CX':
            print("Wybrana operacja przeniesienia: " + operacja1)
            print("Pobieramy zawartość rejestru DX: " + "dx")
            print(cx)
            print("Wykonujemy operację przeniesienia z rejestru CX do DX")
            rejestr_tmp = dx
            cx = dx
            print("Odczytujemy zawartość rejestru AX: " + "ax")
            print(ax)
            dx = rejestr_tmp
        else:
            print("Błąd - nie wybrano operacji")

    if operacja == operacja2:
        print("Wybrana operacja zamiana: " + operacja2)

        print("Podaj numer rejestru z którego zamieniasz: AX | BX | CX | DX")
        nr_rejestru_z = str.upper(input())
        print("Podaj numer rejestru do którego zamieniasz: AX | BX | CX | DX")
        nr_rejestru_do = str.upper(input())

        if nr_rejestru_z == 'AX' and nr_rejestru_do == 'BX':

            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru AX: " + "ax")
            print(ax)
            print(bx)
            print("Wykonujemy operację zamiany z rejestru AX do BX")
            ax, bx = bx, ax
            print("Odczytujemy zawartość rejestru BX: " + "bx")
            print(bx)
            print(ax)

        elif nr_rejestru_z == 'AX' and nr_rejestru_do == 'CX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru AX: " + "ax")
            print(ax)
            print(cx)
            print("Wykonujemy operację zamiany z rejestru AX do CX")
            ax, cx = cx, ax
            print("Odczytujemy zawartość rejestru CX: " + "cx")
            print(cx)
            print(ax)

        elif nr_rejestru_z == 'AX' and nr_rejestru_do == 'DX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru AX: " + "ax")
            print(ax)
            print(dx)
            print("Wykonujemy operację zamiany z rejestru AX do DX")
            ax, dx = dx, ax
            print("Odczytujemy zawartość rejestru DX: " + "dx")
            print(dx)
            print(ax)

        elif nr_rejestru_z == 'BX' and nr_rejestru_do == 'AX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru BX: " + "bx")
            print(bx)
            print(ax)
            print("Wykonujemy operację zamiany z rejestru BX do AX")
            bx, ax = ax, bx
            print("Odczytujemy zawartość rejestru AX: " + "ax")
            print(ax)
            print(bx)

        elif nr_rejestru_z == 'BX' and nr_rejestru_do == 'CX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru BX: " + "bx")
            print(bx)
            print(cx)
            print("Wykonujemy operację zamiany z rejestru BX do CX")
            bx, cx = cx, bx
            print("Odczytujemy zawartość rejestru BX: " + "bx")
            print(cx)
            print(bx)

        elif nr_rejestru_z == 'BX' and nr_rejestru_do == 'DX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru BX: " + "bx")
            print(bx)
            print(dx)
            print("Wykonujemy operację zamiany z rejestru AX do CX")
            bx, dx = dx, bx
            print("Odczytujemy zawartość rejestru DX: " + "dx")
            print(dx)
            print(bx)

        elif nr_rejestru_z == 'CX' and nr_rejestru_do == 'AX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru CX: " + "cx")
            print(cx)
            print(ax)
            print("Wykonujemy operację zamiany z rejestru CX do AX")
            cx, ax = ax, cx
            print("Odczytujemy zawartość rejestru AX: " + "ax")
            print(cx)
            print(ax)

        elif nr_rejestru_z == 'CX' and nr_rejestru_do == 'BX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru CX: " + "cx")
            print(cx)
            print(bx)
            print("Wykonujemy operację zamiany z rejestru CX do BX")
            cx, bx = bx, cx
            print("Odczytujemy zawartość rejestru BX: " + "bx")
            print(bx)
            print(cx)

        elif nr_rejestru_z == 'CX' and nr_rejestru_do == 'DX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru CX: " + "cx")
            print(cx)
            print(dx)
            print("Wykonujemy operację zamiany z rejestru CX do DX")
            cx, dx = dx, cx
            print("Odczytujemy zawartość rejestru DX: " + "dx")
            print(dx)
            print(cx)

        elif nr_rejestru_z == 'DX' and nr_rejestru_do == 'AX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru DX: " + "dx")
            print(dx)
            print(ax)
            print("Wykonujemy operację zamiany z rejestru DX do AX")
            dx, ax = ax, dx
            print("Odczytujemy zawartość rejestru DX: " + "ax")
            print(ax)
            print(dx)

        elif nr_rejestru_z == 'DX' and nr_rejestru_do == 'BX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru DX: " + "dx")
            print(dx)
            print(bx)
            print("Wykonujemy operację zamiany z rejestru DX do AX")
            dx, bx = bx, dx
            print("Odczytujemy zawartość rejestru BX: " + "bx")
            print(bx)
            print(dx)

        elif nr_rejestru_z == 'DX' and nr_rejestru_do == 'CX':
            print("Wybrana operacja zamiany: " + operacja1)
            print("Pobieramy zawartość rejestru DX: " + "dx")
            print(dx)
            print(cx)
            print("Wykonujemy operację zamiany z rejestru DX do CX")
            dx, cx = cx, dx
            print("Odczytujemy zawartość rejestru CX: " + "cx")
            print(cx)
            print(dx)

    if operacja == wyjscie:
        break

print("Zakończenie symulatora")
