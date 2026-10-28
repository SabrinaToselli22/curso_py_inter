from tarea.cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):

  def extraer(self, monto):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    if monto > self.saldo:
      raise ValueError("Fondos insuficientes en la Cuenta Ahorro.")
    self.saldo -= monto

  def aplicar_interes(self):
    interes = self.saldo * 0.001
    self.saldo += interes

    from .cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):

  def extraer(self, monto):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    if monto > self.saldo:
      raise ValueError("Fondos insuficientes en la Cuenta Ahorro.")
    self.saldo -= monto

  def aplicar_interes(self):
    interes = self.saldo * 0.001
    self.saldo += interes