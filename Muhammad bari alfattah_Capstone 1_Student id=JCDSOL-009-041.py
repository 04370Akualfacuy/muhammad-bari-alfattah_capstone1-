#capstone project 1 data scientist
#nama=muhammad bari alfattah
#student id=JCDSOL-009-041

#membuat data list yang akan digunakan

sembako=[ {'barang':'beras',
           'stock':'400 kg',
           'harga':12500},
         {'barang':'garam',
           'stock':'600 kg',
           'harga':12000} ,
         {'barang' :'gula',
           'stock':'800 kg',
           'harga':13500} ,
         {'barang' :'susu',
           'stock' :'200 kg',
           'harga':43000}       
         ]

#digunakan untuk nanti menjadi variabel untuk masukkan tipe data yang diperlukan 

#membuat tampilan list daftar barang secara rapi menggunakan function
def stocksekarang():
    print('''\t\tstock sembako \n Index\t| Nama  \t| Stock  \t| Harga''')
    for i in range(len(sembako)) :
        print('{}\t| {}  \t| {}\t| {}'.format(i,sembako[i]['barang'],sembako[i]['stock'],sembako[i]['harga']))
# membuat opsi baca data
def milihbacadata():#defnisikan untuk membuat penulisan data yang dibuat
      while True:#membuat looping sehingga pilihan bisa dilakukan kembali
               opsibacadata=input('''silahkan pilih opsi untuk stock dalam gudang :
            1.Menampilkan data gudang keseluruhan
            2.menampilkan data berdasarkan index barang
            3.kembali ke menu utama
            ''')
               if(opsibacadata=='1'):
                      stocksekarang()
               elif (opsibacadata=='2'):            
                     a=int(input('masukkan nomor index barang:'))
                     if (a <len(sembako) or a==0):
                        print('''\t\tstock sembako \n Index\t| Nama  \t| Stock  \t| Harga''')
                        print('{}\t| {}  \t| {}\t| {}'.format(a,sembako[a]['barang'],sembako[a]['stock'],sembako[a]['harga']))
                     elif(a >(len(sembako)-1)):
                           print("data tidak dapat ditemukan")
               elif(opsibacadata=='3'):
                     break
                      
                 
def nambahstock():#fitur untuk mengupdate stock
      while True :
            menunambahstock=input('''silahkan pilih menu dalam penambahan stock :
                                  1.menambah stock
                                  2.kembali ke menu utama
                                  ''')
            if(menunambahstock=='1'):
                  stockditambah=input('masukkan nama barang :')
                  for i in sembako:
                    if (i['barang']==stockditambah):
                      print('data sudah ada')
                      break
                    else:
                      barangadd=input('''data belum tersimpan silahkan tulis secara lengkap :
                                      nama barang tambahan :''')
                      stockadd=input('masukkan jumlah stock tambahan :')
                      hargaadd=input('masukkan harga stock tambahan :')
                      disimpan=input('''apakah data ingin disimpan?
                            1.yes
                            2.no \n
                               ''')
                      if (disimpan=='1'):
                            sembako.append({
                              'barang':barangadd,
                              'stock' :stockadd,
                              'harga' :hargaadd
                            })
                            print('data sudah ditambahkan')
                            break                                    
                      elif(disimpan=='2'):
                            break                          
            elif (menunambahstock=='2'):
                break
def updatestock():#digunakan untuk mendefinisikan update pada stock
      while True:
            menuupdate=input('''silahkan pilih menu pada update stock
                  1.update stock
                  2.kembali kemenu utama
                  ''')
            if(menuupdate=='1'):
                  dataupdate=input('silahkan masukkan nama barang yang ingin diupdate:')
                  for m in sembako:
                        if(m['barang']==dataupdate):
                            print(f'{m}data didiupdate ada pada gudang  ')
                            baru=input('''apa ingin lanjut update ?
                                               1.yes
                                               2.no
                                               ''')
                            if(baru=='1'):
                                 updatenggak=input('''silahkan pilih kolom yang ingin diupdate
                                                            1.harga barang
                                                            2.stock barang
                                                            3.harga dan stock barang''')
                                 if(updatenggak=='1'):
                                       hargabaru1=input('masukkan harga baru:')
                                       simpan1=input('''apa data ingin disimpan?
                                                       1.yes
                                                       2.no
                                                       ''')
                                       if(simpan1=='1'):
                                             sembako[sembako.index(m)]['harga']=hargabaru1 
                                             print('data harga sudah diupdate')
                                       elif(simpan1=='2'):
                                           break  
                                 elif(updatenggak=='2'):
                                     stockbaru1=input('masukkan stock baru ')
                                     simpan2=input('''apa data ingin disimpan?
                                                             1.yes
                                                             2.no''')
                                     if(simpan2=='1'):
                                         sembako[sembako.index(m)]['stock']=stockbaru1
                                         print('data stock sudah diupdate')
                                     elif(simpan2=='2'):
                                         break
                                 elif(updatenggak=='3'):
                                     hargabaru=input('silahkan masukkan harga yang baru:')
                                     stockbaru=input('silahkan pilih stock yang baru:')
                                     simpan3=input('''apa data ingin disimpan?
                                                        1.yes
                                                        2.no''')
                                     if(simpan3=='1'):
                                          sembako[sembako.index(m)]['harga']=hargabaru
                                          sembako[sembako.index(m)]['stock']=stockbaru
                                          print('data sudah diupdate')
                                     elif(simpan3=='2'):
                                          break 
                            elif(baru=='2'):
                                break# apa data ingin diupdate atau nggak
                            
                        else:#menunjukkan data ada atau nggak pada gudang
                              print('data yang anda masukan tidak ada')
                              break
                                  
            elif(menuupdate=='2'):
                  break

def hapusstock():#digunakan untuk kelooping tersebut
      while True:
            menudeletestock=input('''masukkan pilihan pada delete stock:
                                  1.menghapus stock 
                                  2.kembali kemenu utama
                                  ''')
            if (menudeletestock=='1'):
                  stockdidelete=input('masukkan nama stock barang yang ingin dihapus :')
                  for j in sembako:
                        if(j['barang']==stockdidelete):
                              pilihan=input('''apakah data ingin dihapus?
                                            1.yes
                                            2.no
                                    ''')
                              if(pilihan=='1'):
                                    for k in sembako:
                                          if (k['barang']==stockdidelete):
                                                ja=sembako.index(k)
                                                del sembako[ja]
                                                print('data berhasil dihapus')
                                                break                                                                                                  
                              elif(pilihan =='2'):
                                    break 
                        else:
                              print('data yang dicari tidak ditemukan')
                              break
                        break
                  
            elif(menudeletestock=='2'):
                  break

#membuat tampilan nemu utama 
while True:
            opsi=input('''Selamat datang dalam data stock gudang sembako!
                silahkan pilih opsi yang ingin digunakan:
                1.Menambahkan stock barang
                2.Menampilkan stock barang dalam gudang
                3.Mengupdate stock pada barang dalam gudang 
                4.Menghapus stock  dalam gudang
                5.Keluar dari program
                   ''')
            if (opsi=='1'):
                  nambahstock()
            elif(opsi=='2'):
                  milihbacadata()
            elif(opsi=='3'):
                  updatestock()
            elif(opsi=='4'):
                  hapusstock()
            elif(opsi=='5'):
                  break
            else:
                print('pilihan yang anda masukkan salah')
      