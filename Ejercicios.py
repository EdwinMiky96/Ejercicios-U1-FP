def sipuedovotarenelecciones():
  print ("Como saber si puedes votar por tu edad")
  mensaje=""
  edadP=int(input("ingrese la edad que tiene:"))
  if edadP>=18:
    mensaje="Usted tiene la edad necesaria para votar"
  else:
    mensaje="Usted no cumple con la edad minima para votar"
  print(mensaje)

def pagoSemanaBase40horas():
  print ("Pago semanal del trabajador")
  sueldoPagarSem=0.0
  #Datos de entrada
  horasTra=int(input("Ingrese horas trabajadas a la semana:"))
  horasPago=int(input("Ingrese el pago por hora:")) 
  #Proceso 
  if horasTra>40:
    sueldoPagarSem=40*horasPago+(horasTra-40)*2*horasPago
  else:
    sueldoPagarSem=horasTra*horasPago
  #Datos de salida
  print("El sueldo a pagar al trabajador es:", sueldoPagarSem)

def regalodel14defebrero():
  presupuesto = int (input ('Ingresa el valor de presupuesto: '))
  if presupuesto<=10:
    print ('Tarjeta')
  if presupuesto>=11 and presupuesto<=100:
    print ('Chocolates')
  if presupuesto>=101 and presupuesto<=250:
    print ('Flores')
  if presupuesto>=251:
    print ('Anillo')
  print ()

def cobroporelusodelEstacionamineto():
  horas = int (input ('Ingresa el valor de horas: '))
  cobro=0
  if horas<=2:
      cobro=horas*5
  if horas>2 and horas<=5:
      cobro=2*5+(horas-2)*4
  if horas>5 and horas<=10:
      cobro=2*5+3*4+(horas-5)*3
  if horas>10:
      cobro=2*5+3*4+3*5+(horas-10)*2
  print ('Valor de cobro: ' + repr (cobro))
  print ()

def costoydescuentodeunArticulo():
  precio = float (input ('Ingresa el valor de precio: '))
  descuento=0
  if precio>=200:
      descuento=precio*0.15
  if precio>100 and precio<200:
      descuento=precio*0.12
  if precio<100:
      descuento=precio*0.1
  costo=precio-descuento
  print ('Valor de costo: ' + repr (costo))
  print ('Valor de descuento: ' + repr (descuento))
  print ()

def asignaciondeBecas():
  edad = float (input ('Ingresa el valor de edad: '))
  promedio = float (input ('Ingresa el valor de promedio: '))
  beca=0
  if edad>18 and promedio>=9:
      beca=2000
  if edad>18 and promedio>=7.5 and promedio<9:
      beca=1000
  if edad>18 and promedio>=6 and promedio<7.5:
      beca=500
  if edad<=18 and promedio>=9:
      beca=3000
  if edad<=18 and promedio>=8 and promedio<9:
      beca=2000
  if edad>18 and promedio>=6 and promedio<8:
      beca=100
  if promedio<6:
      print ('Se env\u00EDa carta de invitaci\u00F3n a estudiar m\u00E1s')
  print ('Valor de beca: ' + repr (beca))
  print ()

def bonomensualporAntiguedad():
  antiguedad = float (input ('Ingresa el valor de antiguedad: '))
  sueldo = float (input ('Ingresa el valor de sueldo: '))
  bono_por_antiguedad=0
  if antiguedad>2 and antiguedad<5:
      bono_por_antiguedad=sueldo*0.2
  if antiguedad>=5:
      bono_por_antiguedad=sueldo*0.3
  bono_por_sueldo=0
  if sueldo<=1000:
      bono_por_sueldo=sueldo*0.25
  if sueldo>1000 and sueldo<=3500:
      bono_por_sueldo=sueldo*0.15
  if sueldo>3500:
      bono_por_sueldo=sueldo*0.1
  if bono_por_antiguedad>bono_por_sueldo:
      bono_mensual=bono_por_antiguedad
  else:
      bono_mensual=bono_por_sueldo
  print ('Valor de bono mensual: ' + repr (bono_mensual))
  print ('Valor de bono por antiguedad: ' + repr (bono_por_antiguedad))
  print ('Valor de bono por sueldo: ' + repr (bono_por_sueldo))
  print ()

def tiposdePoliza():
  edad = float (input ('Ingresa el valor de edad: '))
  print ('Selecciona el valor de tipo de poliza.')
  print ('\t1.- A cobertura amplia')
  print ('\t2.- B da\u00F1os a terceros')
  
  tipo_de_poliza = 0
  while tipo_de_poliza<1 or tipo_de_poliza>2:
    tipo_de_poliza = int (input (': '))
    if tipo_de_poliza<1 or tipo_de_poliza>2:
      print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  print ('Selecciona el valor de toma alcohol.')
  print ('\t1.- si')
  print ('\t2.- no')
  
  toma_alcohol = 0
  while toma_alcohol<1 or toma_alcohol>2:
    toma_alcohol = int (input (': '))
    if toma_alcohol<1 or toma_alcohol>2:
      print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  print ('Selecciona el valor de utiliza lentes.')
  print ('\t1.- si')
  print ('\t2.- no')
  
  utiliza_lentes = 0
  while utiliza_lentes<1 or utiliza_lentes>2:
    utiliza_lentes = int (input (': '))
    if utiliza_lentes<1 or utiliza_lentes>2:
      print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  print ('Selecciona el valor de padece enfermedad.')
  print ('\t1.- si')
  print ('\t2.- no')
  
  padece_enfermedad = 0
  while padece_enfermedad<1 or padece_enfermedad>2:
    padece_enfermedad = int (input (': '))
    if padece_enfermedad<1 or padece_enfermedad>2:
      print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  if tipo_de_poliza==1:
      cuota=1200
  else:
      cuota=950
  cargos=0
  if toma_alcohol==1:
      cargos=cargos+cuota*0.1
  if utiliza_lentes==1:
      cargos=cargos+cuota*0.05
  if padece_enfermedad==1:
      cargos=cargos+cuota*0.05
  if edad>40:
      cargos=cargos+cuota*0.2
  else:
      cargos=cargos+cuota*0.1
  costo_de_la_poliza=cuota+cargos
  print ('Valor de cargos: ' + repr (cargos))
  print ('Valor de costo de la poliza: ' + repr (costo_de_la_poliza))
  print ('Valor de cuota: ' + repr (cuota))
  print ()

def lugarparairdeVacaciones():
  costo_por_km = float (input ('Ingresa el valor de costo por km: '))
  presupuesto = float (input ('Ingresa el valor de presupuesto: '))
  if costo_por_km*750*2<=presupuesto:
      print ('M\u00E9xico')
  else:
      print ('Quedarse en casa')
  if costo_por_km*800*2<=presupuesto:
      print ('Acapulco')
  if costo_por_km*1200*2<=presupuesto:
      print ('Puerto Vallarta')
  if costo_por_km*1800*2<=presupuesto:
      print ('Canc\u00FAn')
  print ()

def bonoporAntiguedad():
  antiguedad = int (input ('Ingresa el valor de antiguedad: '))
  if antiguedad<=5:
      bono=antiguedad*100
  else:
      bono=1000
  print ('Valor de bono: ' + repr (bono))
  print ()

def sueldosemanalBaseHorasTrabajadas():
  horas_trabajadas = float (input ('Ingresa el valor de horas trabajadas: '))
  pago_por_hora = float (input ('Ingresa el valor de pago por hora: '))
  sueldo_semanal=horas_trabajadas*pago_por_hora
  if horas_trabajadas>40:
      sueldo_semanal=sueldo_semanal+(horas_trabajadas-40)*pago_por_hora
  if horas_trabajadas>45:
      sueldo_semanal=sueldo_semanal+(horas_trabajadas-45)*pago_por_hora
  if horas_trabajadas>50:
      sueldo_semanal=0
      print ('No est\u00E1 permitido.')
  print ('Valor de sueldo semanal: ' + repr (sueldo_semanal))
  print ()

def viajedeestudiosycostodePasaje():
  numero_de_alumnos = int (input ('Ingresa el valor de numero de alumnos: '))
  costo_del_pasaje=70
  if numero_de_alumnos>=20:
      costo_del_pasaje=40
  if numero_de_alumnos>=40:
      costo_del_pasaje=35
  if numero_de_alumnos>100:
      costo_del_pasaje=20
  print ('Valor de costo del pasaje: ' + repr (costo_del_pasaje))
  print ()

def calificacionproporcionada():
  calificacion = int (input ('Ingresa el valor de calificacion: '))
  if calificacion==10:
      print ('A')
  if calificacion==9:
      print ('B')
  if calificacion==8:
      print ('C')
  if calificacion==7:
      print ('D')
  if calificacion==6:
      print ('E')
  if calificacion<=5:
      print ('F')
  print ()

def diasdelaSemanaenBaseaunNumero():
  dia_de_la_semana = int (input ('Ingresa el valor de dia de la semana: '))
  if dia_de_la_semana==1:
      print ('Lunes')
  if dia_de_la_semana==2:
      print ('Martes')
  if dia_de_la_semana==3:
      print ('Mi\u00E9rcoles')
  if dia_de_la_semana==4:
      print ('Jueves')
  if dia_de_la_semana==5:
      print ('Viernes')
  if dia_de_la_semana==6:
      print ('S\u00E1bado')
  if dia_de_la_semana==7:
      print ('Domingo')
  if dia_de_la_semana<1 or dia_de_la_semana>7:
      print ('D\u00EDa no v\u00E1lido')
  print ()

def BonoporDesempeno():
  puntos = float (input ('Ingresa el valor de puntos: '))
  salario_minimo = float (input ('Ingresa el valor de salario minimo: '))
  bono=0
  if puntos<=100:
      bono=salario_minimo
  if puntos>100 and puntos<=150:
      bono=salario_minimo*2
  if puntos>150:
      bono=salario_minimo*3
  print ('Valor de bono: ' + repr (bono))
  print ()

def paquetes():
  #Definir Variables
  resultPaquete=""
  #Datos de entrada
  montoRvDic=float(input("Ingrese el monto que recibe en diciembre:"))
  #Proceso
  if montoRvDic>=50000:
    resultPaquete="Paquete A"
  elif montoRvDic>=20000 and montoRvDic<50000:
    resultPaquete="Paquete B"
  elif montoRvDic>=10000 and montoRvDic<20000:
    resultPaquete="Paquete C"
  else:
    resultPaquete="Paquete D"
  #Datos de salida
  print("La persona comprara el: ", resultPaquete)

def BonoNavideno():
  antiguedad = float (input ('Ingresa el valor de antiguedad: '))
  sueldo = float (input ('Ingresa el valor de sueldo: '))
  if antiguedad>4 or sueldo<2000:
      bono_navideno=sueldo*0.25
  else:
      bono_navideno=sueldo*0.2
  print ('Valor de bono navideno: ' + repr (bono_navideno))
  print ()

def TipodeVacunasaAplicar():
  edad = int (input ('Ingresa el valor de edad: '))
  print ('Selecciona el valor de sexo.')
  print ('\t1.- mujer')
  print ('\t2.- hombre')
  print ('\t')
  sexo = 0
  while sexo<1 or sexo>2:
      sexo = int (input (': '))
      if sexo<1 or sexo>2:
          print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  if (sexo==2 and edad>=16 and edad<70) or edad<16:
      print ('A')
  if sexo==1 and edad>=16 and edad<70:
      print ('B')
  if edad>70:
      print ('C')
  print ()

def ventayganaciadepantalosnes():
  N_pantalones = float (input ('Ingresa el valor de N pantalones: '))
  metro_de_tela = float (input ('Ingresa el valor de metro de tela: '))
  print ('Selecciona el valor de modelo.')
  print ('\t1.- A')
  print ('\t2.- B')
  print ('\t')
  modelo = 0
  while modelo<1 or modelo>2:
      modelo = int (input (': '))
      if modelo<1 or modelo>2:
          print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  print ('Selecciona el valor de talla.')
  print ('\t1.- 30')
  print ('\t2.- 32')
  print ('\t3.- 36')
  print ('\t')
  talla = 0
  while talla<1 or talla>3:
      talla = int (input (': '))
      if talla<1 or talla>3:
          print ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
  if modelo==1:
      metros_de_tela=1.5*N_pantalones
  else:
      metros_de_tela=1.8*N_pantalones
  costo_de_la_tela=metros_de_tela*metro_de_tela
  if modelo==1:
      mano_de_obra=costo_de_la_tela*0.8
  else:
      mano_de_obra=costo_de_la_tela*0.95
  if talla==2 or talla==3:
      cargo_por_talla=mano_de_obra*0.04
  else:
      cargo_por_talla=0
  ganancia_extra=(costo_de_la_tela+mano_de_obra+cargo_por_talla)*0.3
  precio_final=costo_de_la_tela+mano_de_obra+cargo_por_talla+ganancia_extra
  ganancia=cargo_por_talla+ganancia_extra
  print ('Valor de cargo por talla: ' + repr (cargo_por_talla))
  print ('Valor de costo de la tela: ' + repr (costo_de_la_tela))
  print ('Valor de ganancia: ' + repr (ganancia))
  print ('Valor de ganancia extra: ' + repr (ganancia_extra))
  print ('Valor de mano de obra: ' + repr (mano_de_obra))
  print ('Valor de metros de tela: ' + repr (metros_de_tela))
  print ('Valor de precio final: ' + repr (precio_final))
  print ()

def bancoBandidodePeluche():
  compras_realizadas = float (input ('Ingresa el valor de compras realizadas: '))
  pago_del_corte_anterior = float (input ('Ingresa el valor de pago del corte anterior: '))
  saldo_anterior = float (input ('Ingresa el valor de saldo anterior: '))
  if saldo_anterior*0.15>pago_del_corte_anterior:
      intereses=saldo_anterior*0.12
      multa=200
  else:
      intereses=0
      multa=0
  saldo_actual=saldo_anterior+compras_realizadas-pago_del_corte_anterior+intereses+multa
  pago_minimo=saldo_actual*0.15
  pago_para_no_generar_intereses=saldo_actual*0.85
  print ('Valor de intereses: ' + repr (intereses))
  print ('Valor de multa: ' + repr (multa))
  print ('Valor de pago minimo: ' + repr (pago_minimo))
  print ('Valor de pago para no generar intereses: ' + repr (pago_para_no_generar_intereses))
  print ('Valor de saldo actual: ' + repr (saldo_actual))
  print ()

sipuedovotarenelecciones()
#pagoSemanaBase40horas()
#regalodel14defebrero()
#cobroporelusodelEstacionamineto()
#costoydescuentodeunArticulo()
#asignaciondeBecas()
#bonomensualporAntiguedad()
#tiposdePoliza()
#lugarparairdeVacaciones()
#bonoporAntiguedad()
#sueldosemanalBaseHorasTrabajadas()
#viajedeestudiosycostodePasaje()
#calificacionproporcionada()
#diasdelaSemanaenBaseaunNumero()
#BonoporDesempeno()
#paquetes()
#BonoNavideno()
#TipodeVacunasaAplicar()
#ventayganaciadepantalosnes()
#bancoBandidodePeluche()