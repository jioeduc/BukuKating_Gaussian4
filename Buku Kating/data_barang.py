data_barang = [

    {
       "nama_barang": "sepatu"
       "harga_barang": 250000,
       "jumlah_barang": 1,
       "status_pengiriman": True, 
       "status_penerimaan": False, 
       "status_akhir": False  
    },
    {
       "nama_barang": "gaun"
       "harga_barang": 180000,
       "jumlah_barang": 2,
       "status_pengiriman": True, 
       "status_penerimaan": True, 
       "status_akhir": False
    },
    {
       "nama_barang": "sandal"
       "harga_barang": 125500,
       "jumlah_barang": 3,
       "status_pengiriman": False, 
       "status_penerimaan": False, 
       "status_akhir": False
    },
    {
       "nama_barang": "snack"
       "harga_barang": 89999,
       "jumlah_barang": 4,
       "status_pengiriman": True, 
       "status_penerimaan": False, 
       "status_akhir": False
    },
    {
       "nama_barang": "kipas"
       "harga_barang": 379800,
       "jumlah_barang": 1,
       "status_pengiriman": True, 
       "status_penerimaan": True, 
       "status_akhir": True
    },
    {
       "nama_barang": "handphone"
       "harga_barang": 7650980,
       "jumlah_barang": 1,
       "status_pengiriman": False, 
       "status_penerimaan": True, 
       "status_akhir": False
    },
    {
       "nama_barang": "keyboard"
       "harga_barang": 678900,
       "jumlah_barang": 6,
       "status_pengiriman": True, 
       "status_penerimaan": False, 
       "status_akhir": True
    },
    {
       "nama_barang": "mouse"
       "harga_barang": 876500,
       "jumlah_barang": 8,
       "status_pengirima": False, 
       "status_penerimaan": True, 
       "status_akhir": False
    },
    {
       "nama_barang": "binder"
       "harga_barang": 45680,
       "jumlah_barang": 7,
       "status_pengiriman": True, 
       "status_penerimaan": True, 
       "status_akhir": True
    },
    {
       "nama_barang": "usb"
       "harga_barang": 465700,
       "jumlah_barang": 8,
       "status_pengiriman": True, 
       "status_penerimaan": True, 
       "status_akhir": False
    }
]
print(f"Nama Barang: {nama_barang}, Harga: {harga_barang}, Jumlah: {jumlah_barang}")
print(f"Status Pengiriman: {'Terkirim' if ['status_pengiriman'] else 'Belum Terkirim}")
print(f"Status Penerimaan: {'Diterima' if ['status_penerimaan'] else 'Belum Diterima'}")
print(f"Status Akhir: {'Selesai' if ['status_akhir'] else 'Tidak Selesai'}")