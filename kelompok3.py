# ======================================
# METODE SECANT - PENCARIAN AKAR PERSAMAAN NON-LINEAR
# ======================================

# Import library
import numpy as np

# ================== PANDUAN INPUT ==================
print("="*70)
print("METODE SECANT - PENCARIAN AKAR PERSAMAAN NON-LINEAR")
print("="*70)
print("\nPANDUAN PENULISAN PERSAMAAN f(x):")
print("-" * 70)
print("• Gunakan 'x' sebagai variabel")
print("• Pangkat (polinomial)        : x**2, x**3, dst")
print("• Fungsi trigonometri         : sin(x), cos(x), tan(x)")
print("• Fungsi trigonometri kebalikan : sec(x), csc(x), cot(x)")
print("• Fungsi trigonometri invers  : arcsin(x), arccos(x), arctan(x)")
print("• Fungsi eksponensial         : exp(x)")
print("• Logaritma natural           : log(x)")
print("• Akar kuadrat                : sqrt(x)")
print("-" * 70)
print("\nCONTOH PERSAMAAN:")
print("  • x*exp(-x)+cos(2*x)")
print("  • exp(-x)*2*x-5")
print("  • x**3 - 2*x - 5")
print("  • exp(x) - 3*x")
print("  • sin(x) - 0.5")
print("="*70)

# Input dari user
persamaan = input("Masukkan persamaan f(x): ")
x0 = float(input("Masukkan nilai x0: "))
x1 = float(input("Masukkan nilai x1: "))
e = float(input("Masukkan toleransi error (e): "))
N = int(input("Masukkan jumlah iterasi maksimum (N): "))

# Definisikan fungsi f(x) dari input user
def f(x):
    def sec(x): return 1/np.cos(x)
    def csc(x): return 1/np.sin(x)
    def cot(x): return 1/np.tan(x)
    return eval(persamaan, {"x": x, "np": np,
                            "sin": np.sin, "cos": np.cos, "tan": np.tan,
                            "sec": sec, "csc": csc, "cot": cot,
                            "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
                            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi})

print("\n+-----+---------------+---------------+---------------+---------------+---------------+---------------+")
print(f"|{'i':^5}|{'x0':^15}|{'x1':^15}|{'y0=f(x0)':^15}|{'y1=f(x1)':^15}|{'xi':^15}|{'|f(xi)|':^15}|")
print("+-----+---------------+---------------+---------------+---------------+---------------+---------------+")

for i in range(N + 1):
    y0 = f(x0)
    y1 = f(x1)
    if y1 - y0 == 0:
        print(f"|{i:^5}|{x0:^15.5f}|{x1:^15.5f}|{y0:^15.5E}|{y1:^15.5E}|{'#DIV/0!':^15}|{'#DIV/0!':^15}|")
        break

    xi = x1 - y1 * (x1 - x0) / (y1 - y0)
