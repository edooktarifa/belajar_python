

from bank.rekening import Rekening
from bank import laporan

rekening = Rekening(pemilik="Sari", saldo=1000000)
saldo_baru = rekening.setor(jumlah=250000)

print(f"{rekening.pemilik}: saldo awal {laporan.format_saldo(rekening.saldo)}")
print(f"{rekening.pemilik}: saldo setelah setor {laporan.format_saldo(saldo_baru)}")