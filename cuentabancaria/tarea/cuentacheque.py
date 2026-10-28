from tarea.cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

  def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
    super().__init__(titular, cbu, saldo_inicial)
    self.costo_emision = costo_emision

  def extraer(self, monto):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    total_a_descontar = monto + self.costo_emision
    if total_a_descontar > self.saldo:
      raise ValueError(
          "Saldo insuficiente para cubrir el monto y la comisión del cheque."
      )
    self.saldo -= total_a_descontar

    from .cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

  def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
    super().__init__(titular, cbu, saldo_inicial)
    self.costo_emision = costo_emision

  def extraer(self, monto):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    total_a_descontar = monto + self.costo_emision
    if total_a_descontar > self.saldo:
      raise ValueError(
          "Saldo insuficiente para cubrir el monto y la comisión del cheque."
      )
    self._saldo -= total_a_descontars