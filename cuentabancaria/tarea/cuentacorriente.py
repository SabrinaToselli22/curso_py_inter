from tarea.cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

  def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
    super().__init__(titular, cbu, saldo_inicial)
    self.limite_descubierto = limite_descubierto

  def extraer(self, monto):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    if monto > (self.saldo + self.limite_descubierto):
      raise ValueError("La extracción supera el límite de descubierto.")
    self.saldo -= monto

    from .cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

  def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
    super().__init__(titular, cbu, saldo_inicial)
    self.limite_descubierto = limite_descubierto

  def extraer(self, monto):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    if monto > (self.saldo + self.limite_descubierto):
      raise ValueError("La extracción supera el límite de descubierto.")
    self._ssaldo -= monto