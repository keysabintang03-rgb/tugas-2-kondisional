database_pasien = [
    {"nama": "Budi"},
    {"nama": "Siti"},
    {"nama": "Joko"},
    {"nama": "Aminah"},
    {"nama": "Rian"},
    {"nama": "Lani"},
    {"nama": "Gatot"},
    {"nama": "Dewi"},
    {"nama": "Hendra"},
    {"nama": "Rina"}
]

print("\n\n=== INPUT DETAIL PASIEN RUMAH SAKIT ===")
for pasien in database_pasien:
    print(f"\n--- Data untuk Pasien: {pasien['nama']} ---")
    pasien["penyakit"] = input(f"Masukkan diagnosis penyakit {pasien['nama']}: ")
    pasien["suhu"] = float(input(f"Masukkan suhu tubuh {pasien['nama']} (°C): "))
    pasien["usia"] = int(input(f"Masukkan usia {pasien['nama']} (tahun): "))
    pasien["hari_inap"] = int(input(f"Masukkan lama hari inap {pasien['nama']}: "))

print("\n\n=== SISTEM MONITORING & TRIASE PASIEN OPNAME ===")
for pasien in database_pasien:
    print(f"\nPasien: {pasien['nama']} ({pasien['penyakit']})")
    
    # 1. Analisis Suhu Tubuh (Operator > dan <=)
    if pasien['suhu'] > 38.0:
        status_suhu = "Hipertermia (Demam Tinggi)"
    elif pasien['suhu'] >= 37.5:
        status_suhu = "Subfebris (Demam Ringan)"
    else:
        status_suhu = "Normal"
    print(f"-> Kondisi Fisik : Suhu {pasien['suhu']}°C ({status_suhu})")
        
    # 2. Pengelompokan Usia Kerentanan (Operator >= dan <)
    if pasien['usia'] >= 60:
        kategori_usia = "Lansia (Risiko Tinggi)"
    elif pasien['usia'] < 13:
        kategori_usia = "Anak-anak (Perhatian Khusus)"
    else:
        kategori_usia = "Dewasa"
    print(f"-> Kategori Usia : {pasien['usia']} tahun -> {kategori_usia}")
        
    # 3. Durasi Perawatan Pasien (Operator >)
    if pasien['hari_inap'] > 10:
        print(f"-> Evaluasi Medis: [LONG-STAY] Sudah dirawat {pasien['hari_inap']} hari. Butuh peninjauan ulang tim dokter.")
    else:
        print(f"-> Evaluasi Medis: [REGULER] Perawatan berjalan (Hari ke-{pasien['hari_inap']}).")