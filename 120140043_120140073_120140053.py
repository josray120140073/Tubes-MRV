import numpy as np
import xlrd

def inputmatriks(matriks, baris, kolom):
  if pilih == "1":
    for i in range(0, baris):
      for j in range(0, kolom):
        if j != kolom-1:
          print(f" A[{i+1}][{j+1}] : ", end="")
        else:
          print(f"Hasil ke-{i+1} : ", end="")
        matriks[i][j] = float(input())
        if j == kolom-1:
          print("="*40)

def inputfile(matriks, data, baris, kolom):
  loc = data
  wb = xlrd.open_workbook(loc)
  sheet = wb.sheet_by_index(0)
  sheet.cell_value(0, 0)
  
  for i in range(baris):
    for j in range(kolom):
      matriks[i,j]=float(sheet.cell_value(i, j))
  return matriks

def output(matriksKW, baris, kolom):
  for i in range(baris):
    print(" [", end="")
    for j in range(kolom):
      if j == kolom-1:
        print(" |", end="")
      print("",round(matriksKW[i][j], 2), end="")
    print(" ]")


def hilbert(matriks, baris, kolom, mode = 0):
  for i in range (0, baris):
    for j in range (0, kolom):
      if j == kolom-1:
        matriks[i][j] = 1
      else:
        matriks[i][j] = 1/(i+j+1)
 

def interpolasi(drajat, x, y, matriks):
  
  for i in range(derajat):
    x[i]= float(input(f"Masukkan nilai x{i} = "))
    y[i]= float(input(f"Masukkan nilai y{i} = "))
 
    print()
  for i in range(derajat):
    matriks.append([])
    for j in range(derajat+1):
      if j == derajat:
        matriks[i].append(y[i])
      else:
        matriks[i].append(pow(x[i],j))
            
  for i in range(drajat):
    print(" [", end="")
    for j in range(drajat+1):
      if j == drajat:
        print(" |", end="")
      print("",round(matriks[i][j], 2), end="")
    print(" ]")

def jordan_interpolasi(matriks, baris, kolom, A):
  z = 0
  for i in range(baris):
    if matriks[i][z] == 0:
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          for k in range(kolom):
            matriks[i][k],matriks[j][k] = matriks[j][k],matriks[i][k]
    if matriks[i][z] != 0:
      if matriks[i][z] != 1:
        temp = matriks[i][z]
        for j in range(z,kolom):
          matriks[i][j] /= temp
      
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          temp = matriks[j][z] / matriks[i][z]
          for k in range(z,kolom):
            matriks[j][k] -= (temp * matriks[i][k])
      z += 1
    else:
      z += 1
      i -= 1
 
  cekIsi = False
  cekHasil = False
  for i in range(baris):
    for j in range(kolom):
      if j < kolom-1:
        if matriks[i][j] == 0: 
          cekIsi = True
        else:
          cekIsi = False
      else:
        if matriks[i][j] == 0:
          cekHasil = True
        else:
          cekHasil = False
    if cekIsi == True and cekHasil == True:
      print("="*40)
      print("="+"Banyak Solusi".center(38)+"=")
      print("="*40)
      print("Setelah Operasi Baris Elementer")       
      output(matriks, baris, kolom)
      print("="*40)
      return 0

  for i in range(baris-1, -1, -1):
    for j in range(kolom-1):
      if matriks[i][j] != 0:
        for k in range(i-1, -1, -1):
          temp = matriks[k][j] / matriks[i][j]
          for l in range(j, kolom):
            matriks[k][l] -= (temp * matriks[i][l])
  print("Setelah Operasi Baris Elementer")  
  print("="*40)     
  output(matriks, baris, kolom)
  print("="*40)
  for i in range (baris):
    for j in range(kolom):
      if j == kolom -1:
        A[i] = matriks[i][j]
  for i in range(baris):
    cek = False
    for j in range(kolom):
      if matriks[i][j] != 0 and j < kolom-1:
        if cek == True:
          print(" +", end="")
        if matriks[i][j] != 1:
          print(f" {matriks[i][j]}", end="")
        print(f"x{j+1}", end="")
        cek = True
    if cek == True:
      print(f" = {round(matriks[i][j], 2)}")

def gauss_interpolasi(matriks, baris, kolom, A):
  z = 0
  for i in range(baris):
    if matriks[i][z] == 0:
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          for k in range(kolom):
            matriks[i][k],matriks[j][k] = matriks[j][k],matriks[i][k]
    if matriks[i][z] != 0:
      if matriks[i][z] != 1:
        temp = matriks[i][z]
        for j in range(z,kolom):
          matriks[i][j] /= temp
      
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          temp = matriks[j][z] / matriks[i][z]
          for k in range(z,kolom):
            matriks[j][k] -= (temp * matriks[i][k])
      z += 1
    else:
      z += 1
      i -= 1
  print("="*40)
  print("Setelah Operasi Baris Elementer")  
  print("="*40)     
  output(matriks, baris, kolom)
  print("="*40)
 
  cekIsi = False
  cekHasil = False
  for i in range(baris):
    for j in range(kolom):
      if j < kolom-1:
        if matriks[i][j] == 0: 
          cekIsi = True
        else:
          cekIsi = False
      else:
        if matriks[i][j] == 0:
          cekHasil = True
        else:
          cekHasil = False
    if cekIsi == True and cekHasil == False:
      print("="*40)
      print("="+"Tidak Ada Solusi".center(38)+"=")
      unik = False
      return 0
    if cekIsi == True and cekHasil == True:
      print("="*40)
      print("="+"Banyak Solusi".center(38)+"=")
      print("="*40)
      return 0

  for i in range(baris-1, -1, -1):
    for j in range(kolom-1):
      if matriks[i][j] != 0:
        for k in range(i-1, -1, -1):
          temp = matriks[k][j] / matriks[i][j]
          for l in range(j, kolom):
            matriks[k][l] -= (temp * matriks[i][l])
 
  for i in range (baris):
    for j in range(kolom):
      if j == kolom -1:
        A[i] = matriks[i][j]
  for i in range(baris):
    cek = False
    for j in range(kolom):
      if matriks[i][j] != 0 and j < kolom-1:
        if cek == True:
          print(" +", end="")
        if matriks[i][j] != 1:
          print(f" {matriks[i][j]}", end="")
        print(f"x{j+1}", end="")
        cek = True
    if cek == True:
      print(f" = {round(matriks[i][j], 2)}")

def cekhasil(matriks, baris, kolom):
  cekIsi = False
  cekHasil = False
  for i in range(baris):
    for j in range(kolom):
      if j < kolom-1:
        if matriks[i][j] == 0: 
          cekIsi = True
        else:
          cekIsi = False
      else:
        if matriks[i][j] == 0:
          cekHasil = True
        else:
          cekHasil = False
    if cekIsi == True and cekHasil == False:
      print("="*40)
      print("="+"Tidak Ada Solusi".center(38)+"=")
      return 0
    if cekIsi == True and cekHasil == True:
      print("="*40)
      print("="+"Banyak Solusi".center(38)+"=")
      print("="*40)
      break

def jordan(matriks, baris, kolom):
  output(matriks, baris, kolom)
  z = 0
  for i in range(baris):
    if matriks[i][z] == 0:
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          for k in range(kolom):
            matriks[i][k],matriks[j][k] = matriks[j][k],matriks[i][k]
          print("="*40)
    if matriks[i][z] != 0:
      if matriks[i][z] != 1:
        temp = matriks[i][z]
        for j in range(z,kolom):
          matriks[i][j] /= temp
      
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          temp = matriks[j][z] / matriks[i][z]
          for k in range(z,kolom):
            matriks[j][k] -= (temp * matriks[i][k])
      z += 1
    else:
      z += 1
      i -= 1
  cekhasil(matriks, baris, kolom)
  for i in range(baris-1, -1, -1):
    for j in range(kolom-1):
      if matriks[i][j] != 0:
        for k in range(i-1, -1, -1):
          temp = matriks[k][j] / matriks[i][j]
          for l in range(j, kolom):
            matriks[k][l] -= (temp * matriks[i][l])
  print("Setelah Operasi Baris Elementer")       
  output(matriks, baris, kolom)
  print("="*40)
  for i in range(baris):
    cek = False
    for j in range(kolom):
      if matriks[i][j] != 0 and j < kolom-1:
        if cek == True:
          print(" +", end="")
        if matriks[i][j] != 1:
          print(f" {matriks[i][j]}", end="")
        print(f"x{j+1}", end="")
        cek = True
    if cek == True:
      print(f" = {round(matriks[i][j], 2)}")
  

def gauss(matriks, baris, kolom):
  output(matriks, baris, kolom)
  z = 0
  for i in range(baris):
    if matriks[i][z] == 0:
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          for k in range(kolom):
            matriks[i][k],matriks[j][k] = matriks[j][k],matriks[i][k]
          print("="*40)
          output(matriks, baris, kolom)
    if matriks[i][z] != 0:
      if matriks[i][z] != 1:
        temp = matriks[i][z]
        for j in range(z,kolom):
          matriks[i][j] /= temp
      
      for j in range(i+1,baris):
        if matriks[j][z] != 0:
          temp = matriks[j][z] / matriks[i][z]
          for k in range(z,kolom):
            matriks[j][k] -= (temp * matriks[i][k])
      z += 1
    else:
      z += 1
      i -= 1
  
  print("Setelah Operasi Baris Elementer")
  output(matriks, baris, kolom)
  print("="*40)
  cekhasil(matriks, baris, kolom)
  for i in range(baris-1, -1, -1):
    for j in range(kolom-1):
      if matriks[i][j] != 0:
        for k in range(i-1, -1, -1):
          temp = matriks[k][j] / matriks[i][j]
          for l in range(j, kolom):
            matriks[k][l] -= (temp * matriks[i][l])
  for i in range(baris):
    cek = False
    for j in range(kolom):
      if matriks[i][j] != 0 and j < kolom-1:
        if cek == True:
          print(" +", end="")
        if matriks[i][j] != 1:
          print(f" {matriks[i][j]}", end="")
        print(f"x{j+1}", end="")
        cek = True
    if cek == True:
      print(f" = {round(matriks[i][j], 2)}")

lanjut = "y"

while(lanjut == "y"):
  print ("="*40)
  print("Matrix dan Ruang Vektor".center(38))
  print("Tugas Besar".center(38))
  print ("="*40)
  print("Menu-menu yang tersedia :")
  print("1. Sistem Persamaan Linear")
  print("2. Matriks Hilbert")
  print("3. interpolasi")
  print("="*40)
  pilih = input("Pilih Menu : ")
  print("="*40)


  if pilih == "1":
    print("Metode yang ingin digukan :")
    print("1. Eliminasi Gauss")
    print("2. Eliminasi Gauss-Jordan")
    print("="*40)
    metode = input("Pilih metode : ")
    print("="*40)
    baris = int(input("Masukan jumlah baris : "))
    kolom = int(input("Masukan jumlah variabel : "))
    kolom = kolom +1
    matriks = np.zeros((baris, kolom))
    print("="*40)
    print ("Menu ")
    print("1. Inputan konsol")
    print("2. Inputan file")
    print("="*40)
    pilih = input("Pilih menu : ")

    if pilih == "1":
       inputmatriks(matriks, baris, kolom)
    elif pilih == "2":
      data = input("Nama file : ")
      inputfile(matriks, data, baris, kolom)

    if metode == "1":
     gauss(matriks, baris, kolom)
    elif metode == "2":
      jordan(matriks, baris, kolom)
  
  elif pilih == "2":
    print("Metode yang ingin digukan :")
    print("1. Eliminasi Gauss")
    print("2. Eliminasi Gauss-Jordan")
    print("="*40)
    metode = input("Pilih metode : ")
    print("="*40)
    
    if metode == "1":
      baris = int(input("Masukan jumlah baris : "))
      kolom = int(input("Masukan jumlah variabel : "))
      kolom = kolom +1
      matriks = np.zeros((baris, kolom))
      hilbert(matriks, baris, kolom)
      gauss(matriks, baris, kolom)
    elif metode == "2":
      baris = int(input("Masukan jumlah baris : "))
      kolom = int(input("Masukan jumlah variabel : "))
      kolom = kolom +1
      matriks = np.zeros((baris, kolom))
      hilbert(matriks, baris, kolom)
      jordan(matriks, baris, kolom)
  elif pilih == "3":
    print("Metode yang ingin digukan :")
    print("1. Eliminasi Gauss")
    print("2. Eliminasi Gauss-Jordan")
    print("="*40)
    metode = input("Pilih metode : ")
    print("="*40)

    derajat = int(input("Masukkan banyak derajat polinom: "))
    titik = float(input("Masukan titik yang ingin di cari : "))
    x = [0]*derajat
    y = [0]*derajat
    matriks = []
    A = np.zeros(derajat)
    hasil = 0 
    if metode == "1":
      interpolasi(derajat, x, y, matriks)
      gauss_interpolasi(matriks, derajat, derajat+1, A)
      for i in range (0, derajat):
        if i == 1:
          A[i] *= titik
        elif i > 1:
          A[i] *= titik**i
        else:
          A[i] = A[i]
        hasil += A[i]
    elif metode == "2":
      interpolasi(derajat, x, y, matriks)
      jordan_interpolasi(matriks, derajat, derajat+1, A)
      for i in range (0, derajat):
        if i == 1:
          A[i] *= titik
        elif i > 1:
          A[i] *= titik**i
        else:
          A[i] = A[i]
        hasil += A[i]
    

    print ("Hasil nya adalah : ", hasil)
  lanjut = input("jika ingin lanjut masukan y : ")