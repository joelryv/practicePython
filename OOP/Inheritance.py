class Employee:
  raise_amt = 1.04
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@email.com'
    self.pay = pay
    
  def fullname(self):
    return '{} {}'.format(self.first. self.last)
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)
    
# Se define una clase que hereda de Employee:
class Developer(Employee):
  raise_amt = 1.10
  
  # Su método init puede cambiar, para no repetir todo el código se pone esto:
  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang

# Se define otra clase que hereda de Employee
class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    self.employees = employees
  
  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)
  
  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
      
  def print_emps(self):
    for emp in self.employees:
      print('-', emp.fullname())
  
#print(help(Manager))

dev_1 = Developer('Cosme', 'Fulanito', '10000', 'Python')
dev_2 = Developer('Homero J.', 'Simpson', '10000', 'Java')

mgr_1 = Manager('Sr.', 'Burns', '100000', [dev_1])

mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
