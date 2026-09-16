import os, json

lessons_data = [
    # Module 1: Fondasi Rust
    {
        "id": 1,
        "slug": "apa-itu-rust",
        "title": "1. Apa Itu Rust & Mengapa Rust?",
        "module": "Fondasi Rust",
        "moduleId": 1,
        "duration": "15 m",
        "level": "Pemula",
        "content": "# Apa Itu Rust?\n\n**Rust** adalah bahasa pemrograman sistem yang berfokus pada **kecepatan, keamanan memori, dan konkurensi** tanpa menggunakan *Garbage Collector* (GC).\n\n## Mengapa Memilih Rust?\n1. **Memory Safety Tanpa GC:** Mencegah Null Pointer Dereference, Use-After-Free, dan Data Race saat kompilasi.\n2. **Zero-Cost Abstractions:** Fitur tingkat tinggi seperti iterators, pattern matching, dan generics dioptimalkan menjadi kode mesin yang sangat cepat.\n3. **Fearless Concurrency:** Compiler memastikan tidak ada data race antar-thread sebelum program dijalankan.\n4. **Toolchain Modern:** Disertai `cargo` (package manager & build tool), `clippy` (linter), dan `rustfmt` (formatter).\n",
        "defaultCode": 'fn main() {\n    println!("Halo dari Rust! 🦀");\n    println!("Keamanan memori tanpa garbage collector.");\n}',
        "expectedOutput": "Halo dari Rust!",
        "hint": "Gunakan macro println! untuk mencetak teks ke console.",
        "quiz": {
            "question": "Bagaimana Rust menjamin keamanan memori tanpa Garbage Collector?",
            "options": [
                "Melalui sistem Ownership dan Borrow Checker pada saat kompilasi",
                "Dengan manual malloc/free seperti di C",
                "Dengan runtime background tracing VM",
                "Dengan mematikan pointer sepenuhnya"
            ],
            "answer": 0
        }
    },
    {
        "id": 2,
        "slug": "variabel-dan-mutability",
        "title": "2. Variabel & Mutability (let vs let mut)",
        "module": "Fondasi Rust",
        "moduleId": 1,
        "duration": "15 m",
        "level": "Pemula",
        "content": "# Variabel dan Mutability\n\nDi Rust, **semua variabel secara default bersifat immutable (tidak bisa diubah)**.\n\n```rust\nlet x = 5; // Immutable\n// x = 6;  // ERROR! compiler menolak ini\n```\n\nUntuk membuat variabel yang bisa diubah nilainya, tambahkan kata kunci `mut`:\n\n```rust\nlet mut counter = 10;\ncounter += 1; // Berhasil!\n```\n",
        "defaultCode": 'fn main() {\n    let mut score = 100;\n    println!("Score awal: {}", score);\n    score += 50;\n    println!("Score setelah bonus: {}", score);\n}',
        "expectedOutput": "Score setelah bonus: 150",
        "hint": "Gunakan let mut untuk variabel yang nilainya akan berubah.",
        "quiz": {
            "question": "Apa sifat default dari variabel di Rust yang dideklarasikan dengan `let`?",
            "options": [
                "Immutable (tidak dapat diubah nilainya)",
                "Mutable (bebas diubah nilainya)",
                "Global static",
                "Constant compile-time"
            ],
            "answer": 0
        }
    },
    {
        "id": 3,
        "slug": "tipe-data-primitif",
        "title": "3. Tipe Data Skalar & Majemuk",
        "module": "Fondasi Rust",
        "moduleId": 1,
        "duration": "20 m",
        "level": "Pemula",
        "content": "# Tipe Data di Rust\n\nRust adalah bahasa yang *statically typed*, artinya compiler harus mengetahui tipe semua variabel saat kompilasi.\n\n## 1. Tipe Skalar\n- **Integers:** `i8`..`i128`, `u8`..`u128`, `isize`, `usize`\n- **Floating-point:** `f32`, `f64`\n- **Boolean:** `bool` (`true` / `false`)\n- **Character:** `char` (4-byte Unicode scalar value)\n\n## 2. Tipe Majemuk\n- **Tuple:** `(i32, f64, char)`\n- **Array:** `[i32; 5]`\n",
        "defaultCode": 'fn main() {\n    let tup: (i32, f64, char) = (500, 6.4, \'🦀\');\n    let (x, y, z) = tup;\n    println!("Tuple: x={}, y={}, z={}", x, y, z);\n}',
        "expectedOutput": "Tuple: x=500",
        "hint": "Tuple bisa diakses langsung via tup.0 atau pattern matching destructuring.",
        "quiz": {
            "question": "Berapa ukuran memori dari tipe data `char` di Rust?",
            "options": [
                "4 bytes (Unicode Scalar Value)",
                "1 byte (ASCII)",
                "2 bytes (UTF-16)",
                "8 bytes (64-bit)"
            ],
            "answer": 0
        }
    },
    {
        "id": 4,
        "slug": "fungsi-dan-ekspresi",
        "title": "4. Fungsi, Parameter & Return Value",
        "module": "Fondasi Rust",
        "moduleId": 1,
        "duration": "15 m",
        "level": "Pemula",
        "content": "# Fungsi di Rust\n\nDeklarasi fungsi menggunakan kata kunci `fn`, dengan konvensi penamaan *snake_case*.\n\n```rust\nfn tambah(a: i32, b: i32) -> i32 {\n    a + b // Tanpa titik koma = ekspresi return!\n}\n```\n",
        "defaultCode": 'fn hitung_luas(panjang: i32, lebar: i32) -> i32 {\n    panjang * lebar\n}\n\nfn main() {\n    let luas = hitung_luas(10, 5);\n    println!("Luas persegi panjang: {} m2", luas);\n}',
        "expectedOutput": "Luas persegi panjang: 50 m2",
        "hint": "Ekspresi tanpa titik koma di akhir blok fungsi otomatis menjadi return value.",
        "quiz": {
            "question": "Mengapa baris terakhir fungsi `panjang * lebar` tidak memerlukan kata kunci `return`?",
            "options": [
                "Karena di Rust ekspresi tanpa titik koma di akhir blok dievaluasi sebagai return value",
                "Karena hanya boleh ada 1 baris per fungsi",
                "Karena keyword return sudah dihapus di Rust",
                "Karena fungsi bertipe void"
            ],
            "answer": 0
        }
    },

    # Module 2: Ownership & Memori
    {
        "id": 5,
        "slug": "ownership-konsep-utama",
        "title": "5. Ownership: Aturan Emas Memori Rust",
        "module": "Ownership & Memori",
        "moduleId": 2,
        "duration": "25 m",
        "level": "Menengah",
        "content": "# Sistem Ownership di Rust\n\nOwnership menjamin keamanan memori tanpa garbage collector.\n\n## Tiga Aturan Emas Ownership:\n1. Setiap nilai di Rust memiliki satu pemilik (*owner*).\n2. Hanya boleh ada satu owner pada satu waktu.\n3. Ketika owner keluar dari scope (`}`), nilai tersebut otomatis dibersihkan (*dropped*).\n",
        "defaultCode": 'fn main() {\n    let s1 = String::from("Rustacean");\n    let s2 = s1.clone(); // Deep copy\n    println!("s1: {}, s2: {}", s1, s2);\n}',
        "expectedOutput": "s1: Rustacean, s2: Rustacean",
        "hint": "Gunakan .clone() jika ingin menyalin data heap tanpa memindahkan ownership.",
        "quiz": {
            "question": "Apa yang terjadi ketika variabel `s1` di-assign ke `s2` pada tipe data heap seperti `String`?",
            "options": [
                "Ownership berpindah (Move) ke s2, dan s1 menjadi tidak valid",
                "Data disalin otomatis secara deep copy",
                "Rust membuat pointer alias dengan garbage collection",
                "Terjadi runtime panic exception"
            ],
            "answer": 0
        }
    },
    {
        "id": 6,
        "slug": "borrowing-dan-references",
        "title": "6. Borrowing & References (&T dan &mut T)",
        "module": "Ownership & Memori",
        "moduleId": 2,
        "duration": "20 m",
        "level": "Menengah",
        "content": "# References & Borrowing\n\nMeminjam (*borrow*) nilai menggunakan referensi (`&`).\n\n## Aturan Borrowing:\n1. Boleh memiliki banyak referensi immutable (`&T`), ATAU\n2. Tepat satu referensi mutable (`&mut T`) pada satu waktu.\n3. Referensi harus selalu valid (tidak boleh dangling).\n",
        "defaultCode": 'fn tambah_teks(s: &mut String) {\n    s.push_str(" adalah bahasa masa depan! 🚀");\n}\n\nfn main() {\n    let mut pesan = String::from("Rust");\n    tambah_teks(&mut pesan);\n    println!("{}", pesan);\n}',
        "expectedOutput": "Rust adalah bahasa masa depan!",
        "hint": "Gunakan &mut untuk meminjam data secara mutable.",
        "quiz": {
            "question": "Berapa banyak referensi mutable (`&mut T`) yang diperbolehkan aktif bersamaan dalam satu scope untuk satu data?",
            "options": [
                "Hanya 1 referensi mutable",
                "Tidak terbatas",
                "Maksimal 2 referensi",
                "Sebanyak yang dialokasikan di stack"
            ],
            "answer": 0
        }
    },
    {
        "id": 7,
        "slug": "slices",
        "title": "7. Slices: Referensi ke Bagian Koleksi",
        "module": "Ownership & Memori",
        "moduleId": 2,
        "duration": "15 m",
        "level": "Menengah",
        "content": "# Slices di Rust\n\n*Slice* adalah referensi ke rangkaian elemen berurutan dalam koleksi tanpa menyalin datanya.\n\n```rust\nlet s = String::from(\"hello world\");\nlet hello: &str = &s[0..5];\n```\n",
        "defaultCode": 'fn kata_pertama(s: &str) -> &str {\n    let bytes = s.as_bytes();\n    for (i, &item) in bytes.iter().enumerate() {\n        if item == b\' \' {\n            return &s[0..i];\n        }\n    }\n    &s[..]\n}\n\nfn main() {\n    let kalimat = "Belajar Rust itu asyik";\n    println!("Kata pertama: {}", kata_pertama(kalimat));\n}',
        "expectedOutput": "Kata pertama: Belajar",
        "hint": "Tipe &str adalah string slice yang mereferensikan bagian dari teks.",
        "quiz": {
            "question": "Apakah String slice (`&str`) menyimpan kepemilikan data string di heap?",
            "options": [
                "Tidak, slice hanya meminjam pointer dan panjang ke data yang sudah ada",
                "Ya, slice membuat duplikasi buffer di heap",
                "Ya, slice memiliki ownership penuh",
                "Hanya jika diubah menjadi mutable"
            ],
            "answer": 0
        }
    },

    # Module 3: Struktur Data & OOP
    {
        "id": 8,
        "slug": "structs-dan-methods",
        "title": "8. Structs & Implementasi Method (`impl`)",
        "module": "Struktur Data & OOP",
        "moduleId": 3,
        "duration": "20 m",
        "level": "Menengah",
        "content": "# Structs & Methods\n\nStruct digunakan untuk membuat tipe data kustom.\n\n```rust\nstruct Rectangle {\n    width: u32,\n    height: u32,\n}\n\nimpl Rectangle {\n    fn area(&self) -> u32 {\n        self.width * self.height\n    }\n}\n```\n",
        "defaultCode": 'struct Rectangle {\n    width: u32,\n    height: u32,\n}\n\nimpl Rectangle {\n    fn area(&self) -> u32 {\n        self.width * self.height\n    }\n}\n\nfn main() {\n    let rect = Rectangle { width: 30, height: 50 };\n    println!("Area: {} px", rect.area());\n}',
        "expectedOutput": "Area: 1500 px",
        "hint": "Gunakan blok impl NamaStruct untuk mendefinisikan method.",
        "quiz": {
            "question": "Apa fungsi parameter `&self` pada method di dalam blok `impl`?",
            "options": [
                "Meminjam instance struct saat ini secara immutable",
                "Membuat static method",
                "Menghapus struct dari memori",
                "Menjadikan method private"
            ],
            "answer": 0
        }
    },
    {
        "id": 9,
        "slug": "enums-dan-option",
        "title": "9. Enums & Tipe `Option<T>` (Anti-Null)",
        "module": "Struktur Data & OOP",
        "moduleId": 3,
        "duration": "20 m",
        "level": "Menengah",
        "content": "# Enums & Option di Rust\n\nRust menggantikan konsep `null` dengan enum standar: **`Option<T>`**:\n\n```rust\nenum Option<T> {\n    Some(T),\n    None,\n}\n```\n",
        "defaultCode": 'fn bagi(pembilang: f64, penyebut: f64) -> Option<f64> {\n    if penyebut == 0.0 {\n        None\n    } else {\n        Some(pembilang / penyebut)\n    }\n}\n\nfn main() {\n    match bagi(10.0, 2.0) {\n        Some(hasil) => println!("Hasil: {}", hasil),\n        None => println!("Error: Dibagi nol"),\n    }\n}',
        "expectedOutput": "Hasil: 5",
        "hint": "Option<T> memiliki dua varian: Some(T) atau None.",
        "quiz": {
            "question": "Mengapa Rust tidak menyediakan tipe `null`?",
            "options": [
                "Untuk mencegah Null Pointer Exception dengan menggunakan enum Option<T>",
                "Karena Rust hanya mendukung integer",
                "Karena memori Rust tidak memiliki alamat 0",
                "Agar sintaks terlihat lebih pendek"
            ],
            "answer": 0
        }
    },
    {
        "id": 10,
        "slug": "pattern-matching-match",
        "title": "10. Pattern Matching (`match` & `if let`)",
        "module": "Struktur Data & OOP",
        "moduleId": 3,
        "duration": "20 m",
        "level": "Menengah",
        "content": "# Pattern Matching\n\n`match` di Rust sangat ekspresif dan harus **exhaustive** (mencakup semua varian).\n",
        "defaultCode": 'enum Status {\n    Pending,\n    Success(String),\n    Failed(u32),\n}\n\nfn main() {\n    let s = Status::Success(String::from("Data tersimpan"));\n    match s {\n        Status::Pending => println!("Menunggu..."),\n        Status::Success(pesan) => println!("Sukses: {}", pesan),\n        Status::Failed(kode) => println!("Gagal: {}", kode),\n    }\n}',
        "expectedOutput": "Sukses: Data tersimpan",
        "hint": "Pola match memeriksa nilai dan mengekstrak data dari varian enum.",
        "quiz": {
            "question": "Apa syarat utama saat menggunakan ekspresi `match` di Rust?",
            "options": [
                "Pola match harus exhaustive (mencakup seluruh kemungkinan cabang)",
                "Harus selalu memiliki tepat 2 cabang",
                "Hanya bisa mencocokkan tipe string",
                "Harus ada kata kunci break di setiap arm"
            ],
            "answer": 0
        }
    },

    # Module 4: Error Handling & Koleksi
    {
        "id": 11,
        "slug": "error-handling-result",
        "title": "11. Error Handling (`Result<T, E>` & `?`)",
        "module": "Error & Koleksi",
        "moduleId": 4,
        "duration": "25 m",
        "level": "Menengah",
        "content": "# Error Handling\n\nRecoverable errors ditangani dengan enum **`Result<T, E>`**:\n\n```rust\nenum Result<T, E> {\n    Ok(T),\n    Err(E),\n}\n```\n\nOperator `?` meneruskan error secara otomatis jika bernilai `Err`.\n",
        "defaultCode": 'fn parse_umur(input: &str) -> Result<u32, &str> {\n    match input.parse::<u32>() {\n        Ok(u) if u > 0 && u <= 120 => Ok(u),\n        Ok(_) => Err("Umur di luar batas!"),\n        Err(_) => Err("Bukan angka valid!"),\n    }\n}\n\nfn main() {\n    match parse_umur("25") {\n        Ok(umur) => println!("Umur: {} tahun", umur),\n        Err(e) => println!("Error: {}", e),\n    }\n}',
        "expectedOutput": "Umur: 25 tahun",
        "hint": "Result<T, E> mengembalikan Ok(nilai) atau Err(error).",
        "quiz": {
            "question": "Apa fungsi operator `?` di belakang ekspresi Result?",
            "options": [
                "Unwrap nilai jika Ok, atau langsung me-return Err dari fungsi saat ini",
                "Memicu panic jika terjadi error",
                "Mengubah Result menjadi boolean",
                "Menjalankan baris tersebut secara asynchronous"
            ],
            "answer": 0
        }
    },
    {
        "id": 12,
        "slug": "koleksi-vector-dan-hashmap",
        "title": "12. Koleksi: Vector (`Vec<T>`) & HashMap",
        "module": "Error & Koleksi",
        "moduleId": 4,
        "duration": "20 m",
        "level": "Menengah",
        "content": "# Koleksi Standar di Rust\n\n- **Vector (`Vec<T>`):** Array dinamis di heap.\n- **HashMap (`HashMap<K, V>`):** Key-value dictionary cepat.\n",
        "defaultCode": 'use std::collections::HashMap;\n\nfn main() {\n    let mut map = HashMap::new();\n    map.insert("Rust", "Aman & Cepat");\n    map.insert("Go", "Sederhana & Ringan");\n    println!("Rust adalah: {}", map["Rust"]);\n}',
        "expectedOutput": "Rust adalah: Aman & Cepat",
        "hint": "Gunakan HashMap::new() dan .insert(key, value).",
        "quiz": {
            "question": "Di mana elemen dari `Vec<T>` disimpan di memori?",
            "options": [
                "Di Heap (pointer dan capacity disimpan di stack)",
                "Di Stack statis",
                "Di ROM",
                "Di Virtual Register"
            ],
            "answer": 0
        }
    },

    # Module 5: Lanjutan & Concurrency
    {
        "id": 13,
        "slug": "generics-dan-traits",
        "title": "13. Generics & Traits",
        "module": "Lanjutan & Concurrency",
        "moduleId": 5,
        "duration": "25 m",
        "level": "Lanjutan",
        "content": "# Generics & Traits\n\nTrait mendefinisikan kemampuan atau kontrak perilaku yang dapat diimplementasikan oleh suatu tipe.\n",
        "defaultCode": 'trait Ringkasan {\n    fn ringkas(&self) -> String;\n}\n\nstruct Artikel {\n    judul: String,\n}\n\nimpl Ringkasan for Artikel {\n    fn ringkas(&self) -> String {\n        format!("Judul: {}", self.judul)\n    }\n}\n\nfn main() {\n    let a = Artikel { judul: String::from("Rust 2026") };\n    println!("{}", a.ringkas());\n}',
        "expectedOutput": "Judul: Rust 2026",
        "hint": "Gunakan impl TraitName for StructName.",
        "quiz": {
            "question": "Apakah Generics di Rust menyebabkan runtime performance overhead?",
            "options": [
                "Tidak, karena Monomorphization mengoptimalkannya saat kompilasi (zero-cost)",
                "Ya, karena dynamic dispatch vtable",
                "Ya, karena memory boxing",
                "Hanya jika diakses dari multi-thread"
            ],
            "answer": 0
        }
    },
    {
        "id": 14,
        "slug": "iterators-dan-closures",
        "title": "14. Iterators & Closures",
        "module": "Lanjutan & Concurrency",
        "moduleId": 5,
        "duration": "20 m",
        "level": "Lanjutan",
        "content": "# Iterators & Closures\n\nIterator di Rust bersifat lazy dan sangat optimal (seringkali lebih cepat dibanding loop manual).\n",
        "defaultCode": 'fn main() {\n    let angka = vec![1, 2, 3, 4, 5, 6];\n    let total: i32 = angka.iter().filter(|&&x| x % 2 == 0).sum();\n    println!("Total genap: {}", total);\n}',
        "expectedOutput": "Total genap: 12",
        "hint": "Gunakan iterator adaptor .filter() dan consumer .sum().",
        "quiz": {
            "question": "Mengapa iterator adaptor di Rust disebut lazy?",
            "options": [
                "Karena tidak mengeksekusi komputasi sampai method consumer dipanggil",
                "Karena lambat di runtime",
                "Karena hanya berjalan di background",
                "Karena membutuhkan dynamic memory"
            ],
            "answer": 0
        }
    },
    {
        "id": 15,
        "slug": "concurrency-threads-channels",
        "title": "15. Concurrency: Threads & Channels",
        "module": "Lanjutan & Concurrency",
        "moduleId": 5,
        "duration": "25 m",
        "level": "Lanjutan",
        "content": "# Fearless Concurrency\n\nRust menjamin bebas data-race saat kompilasi melalui sistem ownership dan tipe `Send` & `Sync`.\n",
        "defaultCode": 'use std::sync::mpsc;\nuse std::thread;\n\nfn main() {\n    let (tx, rx) = mpsc::channel();\n    thread::spawn(move || {\n        tx.send("Data dari thread! 🦀").unwrap();\n    });\n    println!("Menerima: {}", rx.recv().unwrap());\n}',
        "expectedOutput": "Menerima: Data dari thread!",
        "hint": "Gunakan std::sync::mpsc::channel() untuk message passing antar-thread.",
        "quiz": {
            "question": "Apa arti singkatan `mpsc` pada library standar Rust?",
            "options": [
                "Multiple Producer, Single Consumer",
                "Multi Processing Safe Channel",
                "Memory Protected Segment Code",
                "Main Process Signal Controller"
            ],
            "answer": 0
        }
    }
]

MODULES = [
    {"id": 1, "title": "Fondasi Rust", "icon": "fa-solid fa-flag", "desc": "Sintaks & tipe dasar"},
    {"id": 2, "title": "Ownership & Memori", "icon": "fa-solid fa-shield-halved", "desc": "Borrowing & slices"},
    {"id": 3, "title": "Struktur Data & OOP", "icon": "fa-solid fa-cubes", "desc": "Struct, enum, match"},
    {"id": 4, "title": "Error & Koleksi", "icon": "fa-solid fa-boxes-stacked", "desc": "Result, Vec, HashMap"},
    {"id": 5, "title": "Lanjutan & Concurrency", "icon": "fa-solid fa-bolt", "desc": "Traits, threads, async"}
]

os.makedirs("/data/data/com.termux/files/home/rust-learning-path/lessons", exist_ok=True)
for l in lessons_data:
    with open(f"/data/data/com.termux/files/home/rust-learning-path/lessons/{l['slug']}.md", "w", encoding="utf-8") as f:
        f.write(l["content"])

app_code = f"const MODULES = {json.dumps(MODULES, indent=2)};\nconst lessons = {json.dumps(lessons_data, indent=2)};\n"

with open("/data/data/com.termux/files/home/rust-learning-path/app.js", "w", encoding="utf-8") as f:
    f.write(app_code)

print("SUCCESS: Rust data written.")
