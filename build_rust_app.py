import os, json

lessons_data = [
    # Module 1: Pengenalan & Fondasi
    {
        "id": 1,
        "slug": "apa-itu-rust",
        "title": "1. Apa Itu Rust & Mengapa Rust?",
        "module": "Fondasi Rust",
        "moduleId": 1,
        "duration": "15 m",
        "level": "Pemula",
        "content": """# Apa Itu Rust?

**Rust** adalah bahasa pemrograman sistem yang berfokus pada **kecepatan, keamanan memori, dan konkurensi** tanpa menggunakan *Garbage Collector* (GC).

## Mengapa Memilih Rust?
1. **Memory Safety Tanpa GC:** Mencegah Null Pointer Dereference, Use-After-Free, dan Data Race saat kompilasi.
2. **Zero-Cost Abstractions:** Fitur tingkat tinggi seperti iterators, pattern matching, dan generics dioptimalkan menjadi kode mesin yang sangat cepat.
3. **Fearless Concurrency:** Compiler memastikan tidak ada data race antar-thread sebelum program dijalankan.
4. **Toolchain Modern:** Disertai `cargo` (package manager & build tool), `clippy` (linter), dan `rustfmt` (formatter).

Mari coba jalankan kode pertama di editor!
""",
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
        "content": """# Variabel dan Mutability

Di Rust, **semua variabel secara default bersifat immutable (tidak bisa diubah)**.

```rust
let x = 5; // Immutable
// x = 6;  // ERROR! compiler menolak ini
```

Untuk membuat variabel yang bisa diubah nilainya, tambahkan kata kunci `mut`:

```rust
let mut counter = 10;
counter += 1; // Berhasil!
```

### Konstanta (`const`)
Konstanta harus selalu memiliki tipe data eksplisit dan nilainya harus berupa ekspresi konstan:
```rust
const MAX_POINTS: u32 = 100_000;
```
""",
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
        "content": """# Tipe Data di Rust

Rust adalah bahasa yang *statically typed*, artinya compiler harus mengetahui tipe semua variabel saat kompilasi.

## 1. Tipe Skalar (Scalar Types)
- **Integers:** `i8`, `i16`, `i32`, `i64`, `i128`, `isize` (signed) dan `u8`..`u128`, `usize` (unsigned).
- **Floating-point:** `f32`, `f64` (default).
- **Boolean:** `bool` (`true` / `false`).
- **Character:** `char` (4-byte Unicode scalar value, contoh: `'🦀'`).

## 2. Tipe Majemuk (Compound Types)
- **Tuple:** Menggabungkan beberapa nilai dengan tipe berbeda `(i32, f64, u8)`.
- **Array:** Kumpulan nilai bertipe sama dengan panjang tetap `[i32; 5]`.
""",
        "defaultCode": 'fn main() {\n    let tup: (i32, f64, char) = (500, 6.4, \'🦀\');\n    let (x, y, z) = tup;\n    println!("Tuple: x={}, y={}, z={}", x, y, z);\n    \n    let numbers = [1, 2, 3, 4, 5];\n    println!("Array length: {}", numbers.len());\n}',
        "expectedOutput": "Tuple: x=500",
        "hint": "Tuple bisa di-destructure atau diakses menggunakan indeks tup.0, tup.1.",
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
        "content": """# Fungsi di Rust

Deklarasi fungsi menggunakan kata kunci `fn`, dengan konvensi penamaan *snake_case*.

```rust
fn tambah(a: i32, b: i32) -> i32 {
    a + b // Tanpa titik koma = ekspresi return!
}
```

### Statement vs Expression
- **Statement:** Instruksi yang menjalankan aksi dan **tidak** menghasilkan nilai (diakhiri titik koma `;`).
- **Expression:** Bagian kode yang menghasilkan nilai (tanpa titik koma di akhir blok).
""",
        "defaultCode": 'fn hitung_luas(panjang: i32, lebar: i32) -> i32 {\n    panjang * lebar\n}\n\nfn main() {\n    let luas = hitung_luas(10, 5);\n    println!("Luas persegi panjang: {} m2", luas);\n}',
        "expectedOutput": "Luas persegi panjang: 50 m2",
        "hint": "Ekspresi tanpa titik koma di akhir fungsi otomatis menjadi return value.",
        "quiz": {
            "question": "Mengapa baris terakhir fungsi `panjang * lebar` tidak memerlukan kata kunci `return` dan titik koma?",
            "options": [
                "Karena di Rust, baris ekspresi tanpa titik koma di akhir blok dievaluasi sebagai return value",
                "Karena compiler Rust hanya membaca 1 baris per fungsi",
                "Karena keyword return sudah dihapus di Rust modern",
                "Karena fungsi tersebut bertipe void"
            ],
            "answer": 0
        }
    },

    # Module 2: Ownership & Memory Model
    {
        "id": 5,
        "slug": "ownership-konsep-utama",
        "title": "5. Ownership: Aturan Emas Memori Rust",
        "module": "Ownership & Memori",
        "moduleId": 2,
        "duration": "25 m",
        "level": "Menengah",
        "content": """# Sistem Ownership di Rust

Ownership adalah fitur paling unik di Rust yang menjamin keamanan memori tanpa garbage collector.

## Tiga Aturan Emas Ownership:
1. **Setiap nilai di Rust memiliki satu pemilik (*owner*).**
2. **Hanya boleh ada satu owner pada satu waktu.**
3. **Ketika owner keluar dari scope (`}`), nilai tersebut otomatis dibersihkan (*dropped*).**

### Perpindahan Kepemilikan (Move):
```rust
let s1 = String::from("hello");
let s2 = s1; // Nilai s1 dipindahkan ke s2. s1 tidak lagi valid!
// println!("{}", s1); // COMPILE ERROR! value borrowed here after move
```
""",
        "defaultCode": 'fn main() {\n    let s1 = String::from("Rustacean");\n    let s2 = s1.clone(); // Deep copy\n    println!("s1: {}, s2: {}", s1, s2);\n}',
        "expectedOutput": "s1: Rustacean, s2: Rustacean",
        "hint": "Gunakan .clone() jika ingin menyalin data heap tanpa memindahkan ownership.",
        "quiz": {
            "question": "Apa yang terjadi ketika variabel `s1` di-assign ke `s2` pada tipe data yang dialokasikan di heap seperti `String`?",
            "options": [
                "Ownership berpindah (Move) ke s2, dan s1 menjadi tidak valid",
                "Data disalin otomatis secara deep copy di background",
                "Rust membuat pointer alias dengan garbage collector reference counter",
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
        "content": """# References & Borrowing

Alih-alih memindahkan kepemilikan, kita bisa meminjam (*borrow*) nilai menggunakan referensi (`&`).

## Aturan Borrowing:
1. Anda boleh memiliki **banyak referensi immutable (`&T`)**, ATAU
2. Tepat **satu referensi mutable (`&mut T`)** pada satu waktu.
3. Referensi harus selalu valid (tidak boleh *dangling pointer*).

```rust
fn hitung_panjang(s: &String) -> usize {
    s.len()
} // s keluar dari scope, tapi karena s hanya referensi, data asli tidak di-drop!
```
""",
        "defaultCode": 'fn tambah_teks(s: &mut String) {\n    s.push_str(" adalah bahasa masa depan! 🚀");\n}\n\nfn main() {\n    let mut pesan = String::from("Rust");\n    tambah_teks(&mut pesan);\n    println!("{}", pesan);\n}',
        "expectedOutput": "Rust adalah bahasa masa depan!",
        "hint": "Gunakan &mut untuk meminjam data secara mutable.",
        "quiz": {
            "question": "Berapa banyak referensi mutable (`&mut T`) yang diperbolehkan aktif bersamaan dalam satu scope untuk satu data?",
            "options": [
                "Hanya 1 referensi mutable",
                "Tidak terbatas asalkan tidak ada thread lain",
                "Maksimal 2 referensi",
                "Sebanyak yang dialokasikan di stack"
            ],
            "answer": 0
        }
    },
    {
        "id": 7,
        "slug": "slices",
        "title": "7. Slices: Referensi ke Sekumpulan Elemen",
        "module": "Ownership & Memori",
        "moduleId": 2,
        "duration": "15 m",
        "level": "Menengah",
        "content": """# Slices di Rust

*Slice* adalah referensi ke rangkaian elemen berurutan dalam suatu koleksi tanpa menyalin datanya.

## String Slices (`&str`)
```rust
let s = String::from("hello world");
let hello: &str = &s[0..5];
let world: &str = &s[6..11];
```

## Array Slices
```rust
let a = [1, 2, 3, 4, 5];
let slice: &[i32] = &a[1..3]; // berisi [2, 3]
```
""",
        "defaultCode": 'fn kata_pertama(s: &str) -> &str {\n    let bytes = s.as_bytes();\n    for (i, &item) in bytes.iter().enumerate() {\n        if item == b\' \' {\n            return &s[0..i];\n        }\n    }\n    &s[..]\n}\n\nfn main() {\n    let kalimat = "Belajar Rust itu menyenangkan";\n    let kata = kata_pertama(kalimat);\n    println!("Kata pertama: {}", kata);\n}',
        "expectedOutput": "Kata pertama: Belajar",
        "hint": "Tipe &str adalah string slice yang mereferensikan bagian dari teks.",
        "quiz": {
            "question": "Apakah String slice (`&str`) menyimpan kepemilikan data string di heap?",
            "options": [
                "Tidak, slice hanya meminjam pointer dan panjang (length) ke data yang sudah ada",
                "Ya, slice membuat duplikasi buffer di heap",
                "Ya, slice memiliki ownership penuh",
                "Hanya jika diubah menjadi mutable"
            ],
            "answer": 0
        }
    },

    # Module 3: Structs, Enums & Pattern Matching
    {
        "id": 8,
        "slug": "structs-dan-methods",
        "title": "8. Structs & Implementasi Method (`impl`)",
        "module": "Struktur Data & OOP",
        "moduleId": 3,
        "duration": "20 m",
        "level": "Menengah",
        "content": """# Structs di Rust

Struct digunakan untuk membuat tipe data kustom yang mengelompokkan data terkait.

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}
```

## Implementasi Method (`impl`)
Method didefinisikan di dalam blok `impl` dengan parameter pertama `&self`:

```rust
impl User {
    fn status(&self) -> &str {
        if self.active { "Aktif" } else { "Non-aktif" }
    }
}
```
""",
        "defaultCode": 'struct Rectangle {\n    width: u32,\n    height: u32,\n}\n\nimpl Rectangle {\n    fn area(&self) -> u32 {\n        self.width * self.height\n    }\n}\n\nfn main() {\n    let rect = Rectangle { width: 30, height: 50 };\n    println!("Area persegi panjang: {} px", rect.area());\n}',
        "expectedOutput": "Area persegi panjang: 1500 px",
        "hint": "Gunakan blok impl NamaStruct untuk mendefinisikan method.",
        "quiz": {
            "question": "Apa fungsi parameter `&self` pada method di dalam blok `impl`?",
            "options": [
                "Meminjam instance struct saat ini secara immutable",
                "Membuat static method yang tidak terikat instance",
                "Menghapus struct dari memori",
                "Menjadikan method tersebut private"
            ],
            "answer": 0
        }
    },
    {
        "id": 9,
        "slug": "enums-dan-option",
        "title": "9. Enums & Tipe `Option<T>` (Solusi Anti-Null)",
        "module": "Struktur Data & OOP",
        "moduleId": 3,
        "duration": "20 m",
        "level": "Menengah",
        "content": """# Enums & Option di Rust

Enum di Rust sangat kuat karena setiap varian dapat menyimpan data!

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}
```

## Tiada Nilai `null` di Rust!
Rust menggantikan konsep `null` dengan enum bawaan standar: **`Option<T>`**:

```rust
enum Option<T> {
    Some(T),
    None,
}
```
Compiler memaksa developer menangani kemungkinan `None` sebelum mengakses data!
""",
        "defaultCode": 'fn bagi(pembilang: f64, penyebut: f64) -> Option<f64> {\n    if penyebut == 0.0 {\n        None\n    } else {\n        Some(pembilang / penyebut)\n    }\n}\n\nfn main() {\n    match bagi(10.0, 2.0) {\n        Some(hasil) => println!("Hasil pembagian: {}", hasil),\n        None => println!("Error: Pembagian dengan nol!"),\n    }\n}',
        "expectedOutput": "Hasil pembagian: 5",
        "hint": "Option<T> memiliki dua varian: Some(T) atau None.",
        "quiz": {
            "question": "Mengapa Rust tidak menyediakan tipe `null` seperti pada bahasa C atau Java lama?",
            "options": [
                "Untuk mencegah bahaya Null Pointer Exception / billion-dollar mistake dengan menggunakan enum Option<T>",
                "Karena Rust hanya mendukung tipe integer",
                "Karena memori Rust tidak memiliki alamat 0",
                "Agar sintaks terlihat lebih pendek"
            ],
            "answer": 0
        }
    },
    {
        "id": 10,
        "slug": "pattern-matching-match",
        "title": "10. Pattern Matching yang Kuat (`match` & `if let`)",
        "module": "Struktur Data & OOP",
        "moduleId": 3,
        "duration": "20 m",
        "level": "Menengah",
        "content": """# Pattern Matching di Rust

`match` di Rust sangat ekspresif dan harus **exhaustive** (mencakup semua kemungkinan varian).

```rust
let number = 13;
match number {
    1 => println!("Satu"),
    2 | 3 | 5 | 7 | 11 | 13 => println!("Bilangan prima!"),
    14..=20 => println!("Antara 14 dan 20"),
    _ => println!("Lainnya"), // Wildcard default
}
```

### `if let` (Sintaks Ringkas)
Jika hanya peduli pada satu varian:
```rust
if let Some(nilai) = config_max {
    println!("Max value: {}", nilai);
}
```
""",
        "defaultCode": 'enum Status {\n    Pending,\n    Success(String),\n    Failed(u32),\n}\n\nfn proses_status(s: Status) {\n    match s {\n        Status::Pending => println!("Sedang diproses..."),\n        Status::Success(pesan) => println!("Berhasil: {}", pesan),\n        Status::Failed(code) => println!("Gagal dengan kode: {}", code),\n    }\n}\n\nfn main() {\n    proses_status(Status::Success(String::from("Data tersimpan!")));\n}',
        "expectedOutput": "Berhasil: Data tersimpan!",
        "hint": "Pola match memeriksa nilai dan mengekstrak data dari varian enum.",
        "quiz": {
            "question": "Apa yang terjadi jika kita menggunakan `match` tetapi melewatkan salah satu kemungkinan varian enum?",
            "options": [
                "Compiler menolak dengan error bahwa pola belum exhaustive",
                "Program tetap berjalan dan mengabaikan varian tersebut",
                "Otomatis memicu silent fallback",
                "Compiler membuat exception runtime"
            ],
            "answer": 0
        }
    },

    # Module 4: Error Handling & Collections
    {
        "id": 11,
        "slug": "error-handling-result",
        "title": "11. Error Handling Idiomatik (`Result<T, E>` & `?`)",
        "module": "Error & Koleksi",
        "moduleId": 4,
        "duration": "25 m",
        "level": "Menengah",
        "content": """# Error Handling di Rust

Rust membedakan error menjadi dua kategori:
1. **Unrecoverable Errors:** Menggunakan macro `panic!("pesan")` (menghentikan program).
2. **Recoverable Errors:** Menggunakan enum **`Result<T, E>`**:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

## Operator Tanda Tanya (`?`)
Operator `?` meneruskan error secara otomatis ke pemanggil fungsi jika bernilai `Err`, atau mengekstrak nilai jika `Ok`:

```rust
fn baca_file() -> Result<String, std::io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}
```
""",
        "defaultCode": 'fn parse_umur(input: &str) -> Result<u32, &str> {\n    match input.parse::<u32>() {\n        Ok(u) if u > 0 && u <= 120 => Ok(u),\n        Ok(_) => Err("Umur di luar batas wajar!"),\n        Err(_) => Err("Bukan angka yang valid!"),\n    }\n}\n\nfn main() {\n    match parse_umur("25") {\n        Ok(umur) => println!("Umur valid: {} tahun", umur),\n        Err(err) => println!("Error: {}", err),\n    }\n}',
        "expectedOutput": "Umur valid: 25 tahun",
        "hint": "Result<T, E> mengembalikan Ok(nilai) saat sukses atau Err(error) saat gagal.",
        "quiz": {
            "question": "Apa fungsi operator `?` di belakang ekspresi yang menghasilkan `Result`?",
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
        "content": """# Koleksi Standar di Rust

## 1. Vector (`Vec<T>`)
Array dinamis yang tersimpan di heap dan bisa bertambah ukurannya.

```rust
let mut v = Vec::new();
v.push(10);
v.push(20);

let v2 = vec![1, 2, 3, 4, 5]; // Menggunakan macro vec!
```

## 2. HashMap (`HashMap<K, V>`)
Struktur data key-value yang cepat (menggunakan SipHash default).

```rust
use std::collections::HashMap;

let mut skor = HashMap::new();
skor.insert(String::from("Biru"), 10);
skor.insert(String::from("Kuning"), 50);

let nilai = skor.get("Biru").copied().unwrap_or(0);
```
""",
        "defaultCode": 'use std::collections::HashMap;\n\nfn main() {\n    let mut kata_hitung = HashMap::new();\n    let teks = "rust itu cepat dan rust itu aman";\n    \n    for kata in teks.split_whitespace() {\n        let count = kata_hitung.entry(kata).or_insert(0);\n        *count += 1;\n    }\n    \n    println!("Jumlah kata 'rust': {}", kata_hitung["rust"]);\n}',
        "expectedOutput": "Jumlah kata 'rust': 2",
        "hint": "Gunakan .entry(key).or_insert(val) untuk mengupdate value jika key sudah ada.",
        "quiz": {
            "question": "Di manakah data elemen-elemen dari `Vec<T>` disimpan di memori?",
            "options": [
                "Di Heap (dengan pointer, capacity, dan length di Stack)",
                "Seluruhnya di Stack statis",
                "Di Text section binary",
                "Di Thread-local static memory"
            ],
            "answer": 0
        }
    },

    # Module 5: Generics, Traits & Concurrency
    {
        "id": 13,
        "slug": "generics-dan-traits",
        "title": "13. Generics & Traits (Abstraksi Polimorfisme)",
        "module": "Lanjutan & Concurrency",
        "moduleId": 5,
        "duration": "25 m",
        "level": "Lanjutan",
        "content": """# Generics & Traits

## Generics
Membuat fungsi atau struct yang bekerja untuk berbagai tipe data tanpa duplikasi kode:

```rust
fn terbesar<T: PartialOrd>(list: &[T]) -> &T {
    let mut max = &list[0];
    for item in list {
        if item > max { max = item; }
    }
    max
}
```

## Traits (Mirip Interface di Bahasa Lain)
Trait mendefinisikan kemampuan atau kontrak perilaku yang bisa diimplementasikan oleh suatu tipe.

```rust
pub trait Ringkasan {
    fn ringkas(&self) -> String;
}
```
""",
        "defaultCode": 'trait Deskripsi {\n    fn deskripsikan(&self) -> String;\n}\n\nstruct Mobil {\n    merk: String,\n    tahun: u32,\n}\n\nimpl Deskripsi for Mobil {\n    fn deskripsikan(&self) -> String {\n        format!("Mobil {} keluaran tahun {}", self.merk, self.tahun)\n    }\n}\n\nfn cetak_info(item: &impl Deskripsi) {\n    println!("{}", item.deskripsikan());\n}\n\nfn main() {\n    let m = Mobil { merk: String::from("Toyota"), tahun: 2024 };\n    cetak_info(&m);\n}',
        "expectedOutput": "Mobil Toyota keluaran tahun 2024",
        "hint": "Gunakan impl TraitName for StructName untuk mengimplementasikan trait.",
        "quiz": {
            "question": "Apakah abstraksi Generics di Rust memperlambat performa runtime?",
            "options": [
                "Tidak, karena Rust menggunakan teknik Monomorphization (zero-cost abstraction saat kompilasi)",
                "Ya, karena ada dynamic lookup vtable di runtime",
                "Ya, karena memory boxing",
                "Hanya jika menggunakan tipe primitive"
            ],
            "answer": 0
        }
    },
    {
        "id": 14,
        "slug": "iterators-dan-closures",
        "title": "14. Iterators & Closures (Functional Rust)",
        "module": "Lanjutan & Concurrency",
        "moduleId": 5,
        "duration": "20 m",
        "level": "Lanjutan",
        "content": """# Iterators & Closures

Rust mendukung gaya pemrograman fungsional yang sangat cepat.

## Closures (Anonymous Functions)
```rust
let kali_dua = |x: i32| x * 2;
println!("{}", kali_dua(5)); // 10
```

## Iterators
Semua iterator bersifat **lazy** (tidak dieksekusi sebelum dipanggil *consuming adaptor* seperti `.collect()`):

```rust
let v1 = vec![1, 2, 3];
let v2: Vec<i32> = v1.iter().map(|x| x + 1).collect();
```
""",
        "defaultCode": 'fn main() {\n    let angka = vec![1, 2, 3, 4, 5, 6];\n    \n    // Ambil angka genap, kalikan 10, lalu jumlahkan\n    let total: i32 = angka\n        .iter()\n        .filter(|&&x| x % 2 == 0)\n        .map(|&x| x * 10)\n        .sum();\n        \n    println!("Total nilai genap x10: {}", total);\n}',
        "expectedOutput": "Total nilai genap x10: 120",
        "hint": "Gunakan chain method .filter(), .map(), dan .sum() pada iterator.",
        "quiz": {
            "question": "Mengapa iterator adaptor seperti `.map()` atau `.filter()` disebut lazy di Rust?",
            "options": [
                "Karena mereka tidak melakukan komputasi apapun sampai method consumer (seperti .collect() atau .sum()) dipanggil",
                "Karena dijalankan di background thread dengan prioritas rendah",
                "Karena hanya bekerja pada array kosong",
                "Karena menggunakan asynchronous promise"
            ],
            "answer": 0
        }
    },
    {
        "id": 15,
        "slug": "concurrency-threads-channels",
        "title": "15. Fearless Concurrency (Threads & Channels)",
        "module": "Lanjutan & Concurrency",
        "moduleId": 5,
        "duration": "25 m",
        "level": "Lanjutan",
        "content": """# Fearless Concurrency di Rust

Rust menjamin tidak ada data race saat kompilasi berkat sistem ownership!

## 1. Multi-threading dengan `std::thread`
```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Halo dari thread terpisah!");
});
handle.join().unwrap();
```

## 2. Message Passing dengan Channels (mpsc)
*Multiple Producer, Single Consumer*:

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    tx.send("Pesan rahasia").unwrap();
});

let msg = rx.recv().unwrap();
```
""",
        "defaultCode": 'use std::sync::mpsc;\nuse std::thread;\nuse std::time::Duration;\n\nfn main() {\n    let (tx, rx) = mpsc::channel();\n    \n    thread::spawn(move || {\n        let pesan = String::from("Data dari Worker Thread 🚀");\n        tx.send(pesan).unwrap();\n    });\n    \n    let hasil = rx.recv().unwrap();\n    println!("Menerima: {}", hasil);\n}',
        "expectedOutput": "Menerima: Data dari Worker Thread",
        "hint": "Gunakan move closure untuk memindahkan ownership sender tx ke dalam thread.",
        "quiz": {
            "question": "Apa arti singkatan `mpsc` pada channel konkurensi di library standar Rust?",
            "options": [
                "Multiple Producer, Single Consumer",
                "Multi Processing Single Core",
                "Memory Protected Safe Channel",
                "Message Passing Socket Connection"
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

# Write app.js
app_js_content = f"""// Rust Learning Path — Interactive Client App
const MODULES = {json.dumps(MODULES, indent=2)};
const lessons = {json.dumps(lessons_data, indent=2)};
"""
with open("/data/data/com.termux/files/home/rust-learning-path/app.js", "w", encoding="utf-8") as f:
    f.write(app_js_content)

# Write individual markdown files in lessons/
for item in lessons_data:
    md_path = f"/data/data/com.termux/files/home/rust-learning-path/lessons/{item['slug']}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(item["content"])

print(f"Generated {len(lessons_data)} lessons for Rust Learning Path.")
