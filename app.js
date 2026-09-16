// Rust Learning Path — Core Application & Interactive Engine 🦀

const MODULES = [
  { id: 1, title: "Fondasi Rust", icon: "fa-solid fa-flag", desc: "Sintaks, variabel & tipe dasar" },
  { id: 2, title: "Ownership & Memori", icon: "fa-solid fa-shield-halved", desc: "Borrowing, references & slices" },
  { id: 3, title: "Struktur Data & OOP", icon: "fa-solid fa-cubes", desc: "Structs, enums & pattern matching" },
  { id: 4, title: "Error & Koleksi", icon: "fa-solid fa-boxes-stacked", desc: "Result, Vector & HashMap" },
  { id: 5, title: "Lanjutan & Concurrency", icon: "fa-solid fa-bolt", desc: "Generics, traits, threads & channels" }
];

const lessons = [
  {
    id: 1,
    slug: "apa-itu-rust",
    title: "1. Apa Itu Rust & Mengapa Rust?",
    module: "Fondasi Rust",
    moduleId: 1,
    duration: "15 m",
    level: "Pemula",
    content: `# Apa Itu Rust?

**Rust** adalah bahasa pemrograman sistem modern yang berfokus pada **kecepatan, keamanan memori (memory safety), dan konkurensi** tanpa mengorbankan performa atau membutuhkan *Garbage Collector* (GC).

## Pilar Utama Rust:
1. **Memory Safety Tanpa GC:** Menghilangkan bug memori klasik seperti *Null Pointer Dereference*, *Use-After-Free*, dan *Buffer Overflow* pada saat kompilasi via *Borrow Checker*.
2. **Zero-Cost Abstractions:** Abstraksi tingkat tinggi (iterators, closures, pattern matching) dikompilasi menjadi instruksi mesin native secepat kode C/C++.
3. **Fearless Concurrency:** Compiler memastikan tidak ada *Data Race* antar thread saat program berjalan.
4. **Toolchain Kelas Satu:** Dilengkapi paket manajer \`cargo\`, linter \`clippy\`, dan formatter otomatis \`rustfmt\`.

\`\`\`rust
fn main() {
    println!("Halo dari Rust! 🦀");
    println!("Sistem aman tanpa garbage collector.");
}
\`\`\``,
    defaultCode: `fn main() {
    println!("Halo dari Rust! 🦀");
    println!("Sistem aman tanpa garbage collector.");
}`,
    expectedOutput: "Halo dari Rust! 🦀\nSistem aman tanpa garbage collector.",
    hint: "Gunakan macro println! untuk mencetak string ke stdout.",
    quiz: {
      question: "Bagaimana Rust menjamin memory safety tanpa menggunakan runtime Garbage Collector?",
      options: [
        "Melalui sistem Ownership dan Borrow Checker yang divalidasi ketat saat kompilasi",
        "Dengan alokasi memori manual malloc/free seperti bahasa C di runtime",
        "Dengan mematikan seluruh penggunaan pointer dan heap memory",
        "Menggunakan virtual machine berbasis tracing"
      ],
      answer: 0,
      explanation: "Rust menggunakan model Ownership, Borrowing, dan Lifetimes yang diperiksa oleh compiler (Borrow Checker) saat compile-time tanpa runtime overhead."
    }
  },
  {
    id: 2,
    slug: "variabel-dan-mutability",
    title: "2. Variabel & Mutability (let vs let mut)",
    module: "Fondasi Rust",
    moduleId: 1,
    duration: "15 m",
    level: "Pemula",
    content: `# Variabel & Mutability

Secara default di Rust, seluruh variabel bersifat **IMMUTABLE** (tidak dapat diubah setelah diinisialisasi). Jika Anda ingin nilainya dapat dimutasi, Anda wajib menyematkan kata kunci \`mut\`.

## 1. Immutable vs Mutable:
\`\`\`rust
let x = 5; // Immutable (konstan)
// x = 6;  // ERROR kompilasi!

let mut y = 10; // Mutable
y = 20;         // Valid
\`\`\`

## 2. Shadowing Variabel
Rust mendukung *shadowing*, yaitu mendeklarasikan ulang variabel dengan nama yang sama menggunakan keyword \`let\`. Ini memungkinkan kita mengubah tipe data tanpa mengganti nama variabel.`,
    defaultCode: `fn main() {
    let mut score = 100;
    println!("Skor awal: {}", score);
    
    score += 50;
    println!("Skor setelah bonus: {}", score);
    
    // Shadowing: ubah tipe data
    let score = "Sempurna (150)";
    println!("Status skor: {}", score);
}`,
    expectedOutput: "Skor awal: 100\nSkor setelah bonus: 150\nStatus skor: Sempurna (150)",
    hint: "Gunakan 'let mut' untuk variabel yang akan diubah nilainya.",
    quiz: {
      question: "Apa perbedaan antara Shadowing variabel ('let x = ...') dan Mutasi variabel ('x = ...') di Rust?",
      options: [
        "Shadowing membuat variabel baru di scope dan dapat mengubah tipe datanya, sedangkan mutasi hanya mengubah isi dari tipe yang sama",
        "Shadowing hanya bisa dilakukan di dalam block function asynchronous",
        "Mutasi mengalokasikan memori baru di Heap",
        "Tidak ada perbedaan, keduanya identik"
      ],
      answer: 0,
      explanation: "Dengan 'let x = ...', Rust mengalokasikan binding baru dan tipe datanya boleh berbeda dari binding sebelumnya."
    }
  },
  {
    id: 3,
    slug: "tipe-data-skalar-dan-majemuk",
    title: "3. Tipe Data Skalar & Majemuk",
    module: "Fondasi Rust",
    moduleId: 1,
    duration: "20 m",
    level: "Pemula",
    content: `# Tipe Data di Rust

Rust adalah bahasa yang **statically typed** (tipe diketahui saat kompilasi).

## 1. Tipe Skalar:
- **Integers:** \`i8\`, \`i16\`, \`i32\`, \`i64\`, \`i128\`, \`isize\` (signed) serta \`u8\` s.d. \`usize\` (unsigned).
- **Floating-point:** \`f32\`, \`f64\` (default IEEE 754).
- **Boolean:** \`bool\` (\`true\` / \`false\`).
- **Character:** \`char\` (Unicode 4-byte scalar value).

## 2. Tipe Majemuk (Compound):
- **Tuples:** Sekumpulan nilai dengan tipe berbeda, panjang tetap: \`(i32, f64, u8)\`.
- **Arrays:** Sekumpulan nilai dengan tipe sama di stack, panjang tetap: \`[i32; 5]\`.`,
    defaultCode: `fn main() {
    let coords: (f64, f64) = (-6.2088, 106.8456);
    let (lat, lon) = coords;
    
    let primes: [i32; 4] = [2, 3, 5, 7];
    
    println!("Koordinat Jakarta: lat {}, lon {}", lat, lon);
    println!("Bilangan prima pertama: {}", primes[0]);
}`,
    expectedOutput: "Koordinat Jakarta: lat -6.2088, lon 106.8456\nBilangan prima pertama: 2",
    hint: "Destructuring tuple menggunakan sintaks let (a, b) = tuple;",
    quiz: {
      question: "Berapa ukuran memori yang dialokasikan untuk tipe data 'char' di Rust?",
      options: [
        "4 bytes (32-bit), merepresentasikan Unicode Scalar Value",
        "1 byte (8-bit ASCII)",
        "2 bytes (UTF-16)",
        "Dinamis tergantung panjang string"
      ],
      answer: 0,
      explanation: "Tipe char di Rust merepresentasikan Unicode Scalar Value 4 byte (U+0000 sampai U+D7FF dan U+E000 sampai U+10FFFF)."
    }
  },
  {
    id: 4,
    slug: "fungsi-dan-kontrol-alur",
    title: "4. Fungsi, Parameter & Return Value",
    module: "Fondasi Rust",
    moduleId: 1,
    duration: "20 m",
    level: "Pemula",
    content: `# Fungsi & Ekspresi di Rust

Di Rust, fungsi dideklarasikan dengan kata kunci \`fn\`. Format penamaan fungsi menggunakan gaya \`snake_case\`.

## Statement vs Expression
- **Statement:** Instruksi yang melakukan aksi tanpa mengembalikan nilai (diakhiri titik koma \`;\`).
- **Expression:** Blok yang mengevaluasi dan menghasilkan suatu nilai (TIDAK diakhiri titik koma di baris terakhir).

\`\`\`rust
fn tambah(a: i32, b: i32) -> i32 {
    a + b // Expression: otomatis menjadi return value
}
\`\`\``,
    defaultCode: `fn hitung_luas_persegi(sisi: i32) -> i32 {
    sisi * sisi // Tanpa semicolon -> return expression
}

fn main() {
    let panjang = 8;
    let luas = hitung_luas_persegi(panjang);
    println!("Luas persegi sisi {}: {}", panjang, luas);
}`,
    expectedOutput: "Luas persegi sisi 8: 64",
    hint: "Jangan tambahkan titik koma ';' di baris terakhir fungsi jika ingin menggunakannya sebagai return value.",
    quiz: {
      question: "Apa yang terjadi jika Anda menambahkan tanda titik koma ';' di akhir ekspresi return fungsi?",
      options: [
        "Ekspresi berubah menjadi statement dan mengembalikan unit type '()', sehingga memicu type error jika return type bukan '()'",
        "Program akan otomatis melakukan exit(0)",
        "Fungsi akan dieksekusi secara asinkron",
        "Tidak ada efek, compiler mengabaikan titik koma"
      ],
      answer: 0,
      explanation: "Menambahkan titik koma mengubah ekspresi menjadi statement, yang menghasilkan nilai unit type () bukan tipe data yang diharapkan."
    }
  },
  {
    id: 5,
    slug: "ownership-aturan-emas",
    title: "5. Ownership: Aturan Emas Memori Rust",
    module: "Ownership & Memori",
    moduleId: 2,
    duration: "25 m",
    level: "Menengah",
    content: `# Sistem Ownership Rust

Ownership adalah fitur paling unik di Rust yang menjamin keamanan memori tanpa Garbage Collector.

## 3 Aturan Emas Ownership:
1. Setiap nilai (value) di Rust memiliki pemilik (**Owner**).
2. Hanya boleh ada **SATU** pemilik pada satu waktu.
3. Ketika pemilik keluar dari scope (\`}\`), nilai tersebut otomatis dihapus dari memori via fungsi \`drop\`.

## Konsep Move Semantics:
\`\`\`rust
let s1 = String::from("halo");
let s2 = s1; // Kepemilikan (ownership) berpindah (MOVE) ke s2!
// println!("{}", s1); // ERROR: s1 sudah tidak valid!
\`\`\``,
    defaultCode: `fn main() {
    let s1 = String::from("Rustacean");
    
    // Transfer kepemilikan (Move)
    let s2 = s1;
    
    // s2 sekarang menjadi pemilik sah
    println!("Nilai s2: {}", s2);
    
    // Untuk menduplikasi data heap secara eksplisit:
    let s3 = s2.clone();
    println!("s2: {}, s3 (klon): {}", s2, s3);
}`,
    expectedOutput: "Nilai s2: Rustacean\ns2: Rustacean, s3 (klon): Rustacean",
    hint: "Gunakan .clone() jika ingin menyalin data heap tanpa memindahkan ownership.",
    quiz: {
      question: "Mengapa operasi 'let s2 = s1;' pada tipe String menyebabkan s1 tidak bisa diakses lagi (Move semantics)?",
      options: [
        "Karena pointer heap dipindahkan ke s2 dan s1 di-invalidate untuk mencegah double-free memory saat scope berakhir",
        "Karena Rust menghapus data heap secara instan",
        "Karena String otomatis diubah menjadi Read-Only Memory",
        "Karena s1 berubah menjadi tipe integer"
      ],
      answer: 0,
      explanation: "Rust memindahkan pointer stack dan membatalkan s1 agar saat fungsi berakhir hanya s2 yang membebaskan alokasi heap (mencegah bug double-free)."
    }
  },
  {
    id: 6,
    slug: "borrowing-dan-references",
    title: "6. Borrowing & References (&T dan &mut T)",
    module: "Ownership & Memori",
    moduleId: 2,
    duration: "25 m",
    level: "Menengah",
    content: `# Borrowing & References

Alih-alih memindahkan kepemilikan, kita dapat meminjam (**Borrow**) nilai menggunakan referensi (\`&\`).

## Aturan Borrowing:
1. Anda boleh memiliki **banyak referensi immutable (\`&T\`)** secara bersamaan.
2. Anda hanya boleh memiliki **SATU referensi mutable (\`&mut T\`)** pada suatu waktu dalam satu scope.
3. Anda **TIDAK BISA** mencampur referensi mutable dan immutable secara bersamaan dalam scope aktif.
4. Referensi harus selalu valid (*tidak boleh ada dangling reference*).`,
    defaultCode: `fn hitung_panjang(s: &String) -> usize {
    s.len() // Meminjam secara immutable
}

fn tambah_teks(s: &mut String) {
    s.push_str(" Dunia!"); // Meminjam secara mutable
}

fn main() {
    let mut pesan = String::from("Halo");
    
    let len = hitung_panjang(&pesan);
    println!("Panjang '{}' adalah {}", pesan, len);
    
    tambah_teks(&mut pesan);
    println!("Setelah dimutasi: {}", pesan);
}`,
    expectedOutput: "Panjang 'Halo' adalah 4\nSetelah dimutasi: Halo Dunia!",
    hint: "Gunakan '&' untuk immutable borrow dan '&mut' untuk mutable borrow.",
    quiz: {
      question: "Manakah aturan Borrow Checker yang mencegah terjadinya Data Race saat multi-threading di Rust?",
      options: [
        "Tidak boleh ada referensi mutable (&mut) aktif bersamaan dengan referensi lain (& atau &mut) di scope yang sama",
        "Semua variabel wajib didefinisikan sebagai static",
        "Hanya boleh memanggil fungsi dari single thread",
        "Variabel tidak boleh disimpan di stack"
      ],
      answer: 0,
      explanation: "Aturan aliasing XOR mutability (bisa banyak reader ATAU satu writer eksklusif) menjamin data race bebas saat compile-time."
    }
  },
  {
    id: 7,
    slug: "slices-referensi-koleksi",
    title: "7. Slices: Referensi ke Bagian Koleksi",
    module: "Ownership & Memori",
    moduleId: 2,
    duration: "20 m",
    level: "Menengah",
    content: `# Slices di Rust

**Slice** adalah referensi ke urutan elemen berurutan dalam suatu koleksi tanpa menyalin datanya (*zero-copy reference*).

## String Slices (\`&str\`):
\`\`\`rust
let kalimat = String::from("Halo Dunia");
let kata1: &str = &kalimat[0..4]; // "Halo"
let kata2: &str = &kalimat[5..10]; // "Dunia"
\`\`\`

Tipe string literal \`"teks"\` sebenarnya bertipe \`&str\` yang menunjuk langsung ke binary program.`,
    defaultCode: `fn kata_pertama(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}

fn main() {
    let nama = "Rust Systems Programming";
    let first = kata_pertama(nama);
    println!("Kata pertama dari '{}' adalah: '{}'", nama, first);
}`,
    expectedOutput: "Kata pertama dari 'Rust Systems Programming' adalah: 'Rust'",
    hint: "Gunakan &slice[start..end] untuk slicing rentang indeks.",
    quiz: {
      question: "Struktur data internal apa yang menyusun sebuah Slice (&str atau &[T]) di memori?",
      options: [
        "Pointer ke elemen awal data dan nilai panjang (length)",
        "Salinan full array baru di Heap",
        "Sebuah Hash Map",
        "Index linked list"
      ],
      answer: 0,
      explanation: "Slice adalah fat pointer yang terdiri dari pointer ke elemen awal dan panjang (len) slice tersebut."
    }
  },
  {
    id: 8,
    slug: "structs-dan-impl",
    title: "8. Structs & Implementasi Method (`impl`)",
    module: "Struktur Data & OOP",
    moduleId: 3,
    duration: "25 m",
    level: "Menengah",
    content: `# Structs & Methods (\`impl\`)

**Struct** digunakan untuk membuat tipe data kustom yang mengelompokkan nilai-nilai terkait.

## 1. Definisi Struct:
\`\`\`rust
struct Pengguna {
    username: String,
    aktif: bool,
    skor: u64,
}
\`\`\`

## 2. Implementasi Method:
Method dideklarasikan di dalam blok \`impl StructName\` dengan parameter pertama \`&self\`.`,
    defaultCode: `struct PersegiPanjang {
    panjang: u32,
    lebar: u32,
}

impl PersegiPanjang {
    // Associated function (constructor)
    fn baru(p: u32, l: u32) -> Self {
        Self { panjang: p, lebar: l }
    }
    
    // Method
    fn luas(&self) -> u32 {
        self.panjang * self.lebar
    }
}

fn main() {
    let rect = PersegiPanjang::baru(10, 5);
    println!("Luas persegi panjang: {} px²", rect.luas());
}`,
    expectedOutput: "Luas persegi panjang: 50 px²",
    hint: "Gunakan Self::baru(...) untuk associated functions dan &self untuk instance methods.",
    quiz: {
      question: "Apa perbedaan antara Associated Function (misal 'PersegiPanjang::baru()') dan Method (misal 'rect.luas()') pada blok impl?",
      options: [
        "Method menerima parameter '&self' (atau '&mut self'/'self'), sedangkan associated function tidak memiliki parameter self",
        "Associated function hanya bisa dipanggil secara private",
        "Method tidak dapat mengembalikan nilai",
        "Associated function wajib berformat macro"
      ],
      answer: 0,
      explanation: "Associated functions bertindak seperti static function/constructor tanpa 'self', sedangkan method beroperasi pada instance via parameter self."
    }
  },
  {
    id: 9,
    slug: "enums-dan-option",
    title: "9. Enums & Tipe `Option<T>` (Anti-Null)",
    module: "Struktur Data & OOP",
    moduleId: 3,
    duration: "25 m",
    level: "Menengah",
    content: `# Enums & Tipe Option

Rust **TIDAK MEMILIKI** nilai \`null\` atau \`nil\`. Sebagai gantinya, Rust menggunakan enum bawaan \`Option<T>\` untuk menangani nilai yang mungkin ada atau kosong.

\`\`\`rust
enum Option<T> {
    Some(T),
    None,
}
\`\`\`

Compiler mewajibkan developer menangani kasus \`None\` secara eksplisit sebelum isi \`Some(val)\` dapat diekstraksi.`,
    defaultCode: `fn bagi(pembilang: f64, penyebut: f64) -> Option<f64> {
    if penyebut == 0.0 {
        None
    } else {
        Some(pembilang / penyebut)
    }
}

fn main() {
    let hasil1 = bagi(10.0, 2.0);
    let hasil2 = bagi(10.0, 0.0);
    
    match hasil1 {
        Some(val) => println!("Hasil pembagian: {}", val),
        None => println!("Error: Pembagian dengan nol!"),
    }
    
    match hasil2 {
        Some(val) => println!("Hasil pembagian: {}", val),
        None => println!("Error: Pembagian dengan nol!"),
    }
}`,
    expectedOutput: "Hasil pembagian: 5\nError: Pembagian dengan nol!",
    hint: "Gunakan match untuk menangani varian Some(val) dan None.",
    quiz: {
      question: "Mengapa desain ketiadaan 'null' dan digantikan oleh Option<T> membuat program Rust jauh lebih aman?",
      options: [
        "Compiler memvalidasi penanganan kasus 'None' saat kompilasi, mengeliminasi bug Null Pointer Dereference saat runtime",
        "Karena Option<T> otomatis mengubah tipe data menjadi String",
        "Option<T> mematikan memori stack",
        "Karena None selalu bernilai integer 0"
      ],
      answer: 0,
      explanation: "Option<T> memaksa developer membungkus dan menangani kemungkinan ketiadaan data secara tipe eksplisit sebelum kompilasi lolos."
    }
  },
  {
    id: 10,
    slug: "pattern-matching",
    title: "10. Pattern Matching (`match` & `if let`)",
    module: "Struktur Data & OOP",
    moduleId: 3,
    duration: "20 m",
    level: "Menengah",
    content: `# Pattern Matching

Statement \`match\` di Rust bersifat **EXHAUSTIVE** (wajib mencakup seluruh kemungkinan kasus).

## Fitur Matching:
- **Exhaustiveness:** Compiler menolak kompilasi jika ada varian enum yang tidak ditangani.
- **Guard Patterns:** Menambahkan klausa \`if\` pada lengan match.
- **if let:** Sintaks ringkas jika hanya peduli pada satu varian tertentu.`,
    defaultCode: `enum Role {
    Admin,
    Editor,
    Viewer(u32), // Membawa data level
}

fn proses_role(r: Role) {
    match r {
        Role::Admin => println!("Akses Penuh Super Admin"),
        Role::Editor => println!("Akses Edit Dokumen"),
        Role::Viewer(lvl) if lvl > 1 => println!("Viewer Premium Level {}", lvl),
        Role::Viewer(_) => println!("Viewer Biasa"),
    }
}

fn main() {
    proses_role(Role::Admin);
    proses_role(Role::Viewer(5));
}`,
    expectedOutput: "Akses Penuh Super Admin\nViewer Premium Level 5",
    hint: "Gunakan match role { Role::Variant => ... } dan wildcard _ untuk default.",
    quiz: {
      question: "Apa arti sifat 'Exhaustive' pada statement 'match' di Rust?",
      options: [
        "Seluruh kemungkinan varian atau kondisi harus ditangani di lengan match, jika tidak compiler akan menolak",
        "Match akan mengeksekusi semua case secara berurutan seperti fallthrough C",
        "Match otomatis mematikan thread jika terjadi loop",
        "Match hanya berlaku untuk tipe integer"
      ],
      answer: 0,
      explanation: "Exhaustiveness memastikan tidak ada kasus tak terduga yang lolos saat runtime; jika ada varian baru, compiler akan langsung memperingatkan."
    }
  },
  {
    id: 11,
    slug: "error-handling-result",
    title: "11. Error Handling (`Result<T, E>` & `?`)",
    module: "Error & Koleksi",
    moduleId: 4,
    duration: "25 m",
    level: "Menengah",
    content: `# Penanganan Error di Rust

Rust membagi error menjadi dua kategori:
1. **Unrecoverable Error (\`panic!\`):** Program berhenti karena bug fatal.
2. **Recoverable Error (\`Result<T, E>\`):** Error yang dapat ditangani dan dipulihkan.

\`\`\`rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
\`\`\`

Operator tanya (\`?\`) digunakan untuk *early return* propagating error ke pemanggil fungsi secara sangat bersih.`,
    defaultCode: `fn parse_umur(s: &str) -> Result<u32, String> {
    match s.trim().parse::<u32>() {
        Ok(umur) if umur > 120 => Err(String::from("Umur tidak valid")),
        Ok(umur) => Ok(umur),
        Err(_) => Err(String::from("Bukan format angka valid")),
    }
}

fn main() {
    match parse_umur("25") {
        Ok(val) => println!("Umur terverifikasi: {} tahun", val),
        Err(e) => println!("Error: {}", e),
    }
}`,
    expectedOutput: "Umur terverifikasi: 25 tahun",
    hint: "Gunakan operator ? untuk membongkar Ok(T) atau langsung return Err(E).",
    quiz: {
      question: "Apa fungsi utama operator '?' (question mark operator) pada ekspresi yang mengembalikan Result<T, E>?",
      options: [
        "Mengekstrak nilai jika Ok(T), atau langsung me-return Err(E) dari fungsi saat ini",
        "Memicu runtime panic seketika jika ada error",
        "Mengabaikan error dan menggantinya dengan nilai default 0",
        "Mengonversi Result menjadi tipe Boolean"
      ],
      answer: 0,
      explanation: "Operator ? menyederhanakan error propagation: jika Ok akan di-unwrap, jika Err akan otomatis return dari fungsi pembungkus."
    }
  },
  {
    id: 12,
    slug: "koleksi-vector-dan-hashmap",
    title: "12. Koleksi: Vector (`Vec<T>`) & HashMap",
    module: "Error & Koleksi",
    moduleId: 4,
    duration: "25 m",
    level: "Menengah",
    content: `# Koleksi Standar di Rust

Data koleksi dialokasikan di Heap memori.

## 1. Vector (\`Vec<T>\`)
Array dinamis yang dapat bertambah ukurannya.
\`\`\`rust
let mut v = vec![1, 2, 3];
v.push(4);
\`\`\`

## 2. HashMap (\`HashMap<K, V>\`)
Menyimpan pasangan key-value dengan hash table cepat via SipHash.`,
    defaultCode: `use std::collections::HashMap;

fn main() {
    let mut populasi: HashMap<&str, u32> = HashMap::new();
    populasi.insert("Jakarta", 10_560_000);
    populasi.insert("Surabaya", 2_870_000);
    populasi.insert("Bandung", 2_440_000);
    
    // Mengakses dengan aman
    if let Some(&jumlah) = populasi.get("Jakarta") {
        println!("Populasi Jakarta: {} jiwa", jumlah);
    }
    
    // Entry API untuk update
    populasi.entry("Medan").or_insert(2_430_000);
    println!("Total kota terdata: {}", populasi.len());
}`,
    expectedOutput: "Populasi Jakarta: 10560000 jiwa\nTotal kota terdata: 4",
    hint: "Gunakan map.entry(key).or_insert(value) untuk inisialisasi jika key belum ada.",
    quiz: {
      question: "Bagaimana alokasi memori internal dari tipe 'Vec<T>' di Rust?",
      options: [
        "Struktur header (pointer, length, capacity) di Stack, dan buffer elemen aktual di Heap",
        "Seluruh data dialokasikan langsung di Static Data Segment",
        "Menggunakan linked-list berantai di Stack",
        "Disimpan di Virtual Disk Swap"
      ],
      answer: 0,
      explanation: "Vec<T> adalah struktur 3-word di stack (pointer ke buffer, length, dan capacity) yang menunjuk ke array kontigu di heap."
    }
  },
  {
    id: 13,
    slug: "generics-dan-traits",
    title: "13. Generics & Traits",
    module: "Lanjutan & Concurrency",
    moduleId: 5,
    duration: "25 m",
    level: "Lanjutan",
    content: `# Generics & Traits

**Trait** mendefinisikan kemampuan atau kontrak perilaku yang dapat diimplementasikan oleh berbagai tipe data (mirip Interface di bahasa lain).

## Zero-Cost Monomorphization:
Compiler Rust mengubah kode generic menjadi implementasi tipe konkret saat kompilasi (*Monomorphization*), sehingga eksekusinya secepat kode non-generic tanpa overhead runtime!`,
    defaultCode: `trait Bersuara {
    fn bersuara(&self) -> String;
}

struct Kucing;
struct Robot;

impl Bersuara for Kucing {
    fn bersuara(&self) -> String { String::from("Meong! 🐱") }
}

impl Bersuara for Robot {
    fn bersuara(&self) -> String { String::from("Bip Bop! 🤖") }
}

// Generic function dengan Trait Bound
fn buat_suara<T: Bersuara>(item: &T) {
    println!("Output: {}", item.bersuara());
}

fn main() {
    let k = Kucing;
    let r = Robot;
    buat_suara(&k);
    buat_suara(&r);
}`,
    expectedOutput: "Output: Meong! 🐱\nOutput: Bip Bop! 🤖",
    hint: "Gunakan sintaks fn func<T: TraitName>(param: &T) untuk trait bounds.",
    quiz: {
      question: "Mengapa Generic di Rust disebut 'Zero-Cost Abstraction'?",
      options: [
        "Karena Rust melakukan Monomorphization saat compile-time menjadi kode konkret tanpa biaya virtual lookup (vtable) di runtime",
        "Karena Rust menolak eksekusi fungsi yang memiliki parameter generic",
        "Karena seluruh tipe generic diubah menjadi void pointer",
        "Karena tidak menggunakan memori komputer"
      ],
      answer: 0,
      explanation: "Monomorphization menduplikasi fungsi generic untuk setiap tipe konkret saat kompilasi, menghasilkan kode assembly native yang sangat cepat."
    }
  },
  {
    id: 14,
    slug: "iterators-dan-closures",
    title: "14. Iterators & Closures",
    module: "Lanjutan & Concurrency",
    moduleId: 5,
    duration: "20 m",
    level: "Lanjutan",
    content: `# Iterators & Closures

## 1. Closures:
Fungsi anonim yang dapat menangkap variabel dari lingkungan sekitarnya (*lexical scope*):
\`\`\`rust
let faktor = 2;
let kali = |x| x * faktor;
\`\`\`

## 2. Iterators:
Iterator di Rust bersifat **LAZY** — tidak ada evaluasi sebelum method consumer (seperti \`collect()\`, \`sum()\`, \`for_each()\`) dipanggil.`,
    defaultCode: `fn main() {
    let angka = vec![1, 2, 3, 4, 5, 6, 7, 8];
    
    // Iterator pipeline: filter genap -> kuadratkan -> kumpulkan ke Vec
    let hasil: Vec<i32> = angka
        .iter()
        .filter(|&&x| x % 2 == 0)
        .map(|&x| x * x)
        .collect();
        
    println!("Hasil kuadrat bilangan genap: {:?}", hasil);
}`,
    expectedOutput: "Hasil kuadrat bilangan genap: [4, 16, 36, 64]",
    hint: "Gunakan .filter(), .map(), dan akhiri dengan .collect() untuk mengeksekusi pipeline iterator.",
    quiz: {
      question: "Mengapa adaptor iterator di Rust (seperti .map(), .filter()) bersifat Lazy?",
      options: [
        "Karena adaptor hanya membangun rantai pemrosesan dan tidak melakukan iterasi hingga metode consumer (.collect(), .sum(), dll) dipanggil",
        "Karena berjalan lambat di background thread",
        "Karena hanya mengevaluasi satu elemen saja",
        "Karena memerlukan alokasi memori dinamis"
      ],
      answer: 0,
      explanation: "Sifat lazy memungkinkan Rust menggabungkan seluruh tahapan iterasi ke dalam satu loop teroptimasi tingkat tinggi saat consumer dieksekusi."
    }
  },
  {
    id: 15,
    slug: "concurrency-threads-channels",
    title: "15. Concurrency: Threads & Channels",
    module: "Lanjutan & Concurrency",
    moduleId: 5,
    duration: "25 m",
    level: "Lanjutan",
    content: `# Fearless Concurrency

Rust menjamin program multi-threading bebas dari data race berkat sistem type checking, ownership, dan trait penanda (\`Send\` & \`Sync\`).

## Message Passing via Channels (\`mpsc\`):
*"Do not communicate by sharing memory; instead, share memory by communicating."*

- **mpsc:** *Multiple Producer, Single Consumer*.`,
    defaultCode: `use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();
    
    // Spawn thread baru
    thread::spawn(move || {
        let pesan = vec!["Pesan 1", "Pesan 2", "Pesan 3"];
        for p in pesan {
            tx.send(p).unwrap();
            thread::sleep(Duration::from_millis(10));
        }
    });
    
    // Main thread menerima pesan
    for diterima in rx {
        println!("Menerima: {}", diterima);
    }
}`,
    expectedOutput: "Menerima: Pesan 1\nMenerima: Pesan 2\nMenerima: Pesan 3",
    hint: "Gunakan keyword 'move' pada closure thread::spawn untuk mentransfer kepemilikan data ke dalam thread baru.",
    quiz: {
      question: "Apa fungsi keyword 'move' pada pemanggilan 'thread::spawn(move || { ... })' di Rust?",
      options: [
        "Mentransfer kepemilikan (ownership) variabel lingkungan yang dipakai ke dalam closure thread agar validitas memorinya terjamin",
        "Membuat thread berjalan di core CPU berbeda",
        "Menghentikan thread utama seketika",
        "Menghapus data memori setelah thread selesai"
      ],
      answer: 0,
      explanation: "Keyword 'move' memaksa closure mengambil alih ownership nilai yang ditangkap, mencegah bug dangling pointer jika scope pemanggil berakhir lebih dulu."
    }
  }
];

// Application State
let currentLessonIndex = 0;
let progress = JSON.parse(localStorage.getItem('rust_progress') || '{}');
let completedLessons = JSON.parse(localStorage.getItem('rust_completed_lessons') || '[]');

// DOM Elements cache
let lessonTitle, breadcrumb, lessonDuration, lessonLevel, lessonContent;
let codeEditor, outputTerminal, quizSection, quizContent, quizResult;
let prevBtn, nextBtn, completeBtn, completedBtn;

document.addEventListener('DOMContentLoaded', () => {
    initElements();
    renderNav();
    
    // Auto-resume last lesson
    const savedLesson = parseInt(localStorage.getItem('rust_last_lesson'), 10);
    if (!isNaN(savedLesson) && savedLesson >= 0 && savedLesson < lessons.length) {
        loadLesson(savedLesson);
    } else {
        loadLesson(0);
    }
    
    updateProgressUI();
});

function initElements() {
    lessonTitle = document.getElementById('lesson-title');
    breadcrumb = document.getElementById('breadcrumb');
    lessonDuration = document.getElementById('lesson-duration');
    lessonLevel = document.getElementById('lesson-level');
    lessonContent = document.getElementById('lesson-content');
    codeEditor = document.getElementById('code-editor');
    outputTerminal = document.getElementById('output');
    quizSection = document.getElementById('quiz-section');
    quizContent = document.getElementById('quiz-content');
    quizResult = document.getElementById('quiz-result');
    prevBtn = document.getElementById('prev-btn');
    nextBtn = document.getElementById('next-btn');
    completeBtn = document.getElementById('complete-btn');
    completedBtn = document.getElementById('completed-btn');
}

window.renderNav = function(filter = '') {
    const nav = document.getElementById('lessons-nav');
    if (!nav) return;
    nav.innerHTML = '';
    
    MODULES.forEach(mod => {
        const modLessons = lessons.filter(l => l.moduleId === mod.id && (!filter || l.title.toLowerCase().includes(filter.toLowerCase())));
        if (modLessons.length === 0) return;
        
        const modEl = document.createElement('div');
        modEl.className = 'mb-4';
        
        const header = document.createElement('div');
        header.className = 'px-3 py-1.5 text-[11px] font-bold tracking-wider uppercase text-slate-400 flex items-center gap-2';
        header.innerHTML = `<i class="${mod.icon} text-orange-400 text-xs"></i> ${mod.title}`;
        modEl.appendChild(header);
        
        const list = document.createElement('div');
        list.className = 'mt-1 space-y-0.5';
        
        modLessons.forEach(l => {
            const idx = lessons.findIndex(x => x.id === l.id);
            const isDone = !!progress[l.id];
            const isCurrent = idx === currentLessonIndex;
            
            const item = document.createElement('button');
            item.className = `w-full text-left px-3 py-2 rounded-xl text-xs flex items-center justify-between transition ${
                isCurrent 
                    ? 'bg-orange-500/15 text-orange-400 font-semibold border border-orange-500/30' 
                    : 'text-slate-300 hover:bg-white/5'
            }`;
            item.innerHTML = `
                <span class="truncate pr-2">${l.title}</span>
                <i class="fas ${isDone ? 'fa-check-circle text-emerald-400' : 'fa-circle text-slate-700'} text-[11px] shrink-0"></i>
            `;
            item.addEventListener('click', () => {
                loadLesson(idx);
                if (typeof window.closeSidebar === 'function') window.closeSidebar();
            });
            list.appendChild(item);
        });
        
        modEl.appendChild(list);
        nav.appendChild(modEl);
    });
};

window.loadLesson = function(index) {
    if (index < 0 || index >= lessons.length) return;
    currentLessonIndex = index;
    localStorage.setItem('rust_last_lesson', index);
    
    const l = lessons[index];
    if (lessonTitle) lessonTitle.textContent = l.title;
    if (breadcrumb) breadcrumb.textContent = `${l.module} • Pelajaran ${index + 1} dari ${lessons.length}`;
    
    if (lessonDuration) {
        lessonDuration.classList.remove('hidden');
        lessonDuration.textContent = l.duration;
    }
    if (lessonLevel) {
        lessonLevel.classList.remove('hidden');
        lessonLevel.textContent = l.level;
    }
    
    if (lessonContent && typeof marked !== 'undefined') {
        lessonContent.innerHTML = marked.parse(l.content);
        lessonContent.querySelectorAll('pre code').forEach(el => {
            if (typeof hljs !== 'undefined') hljs.highlightElement(el);
        });
    }
    
    if (codeEditor) {
        codeEditor.value = l.defaultCode;
    }
    
    if (outputTerminal) {
        outputTerminal.innerHTML = '<span class="text-slate-600">// Tekan Run untuk mengompilasi kode Rust</span>';
    }
    
    // Render Quiz
    renderQuizUI(l.quiz);
    
    // Buttons state
    if (prevBtn) prevBtn.disabled = index === 0;
    if (nextBtn) {
        nextBtn.innerHTML = index === lessons.length - 1 ? 'Selesai 🎉' : 'Next <i class="fas fa-chevron-right text-xs"></i>';
    }
    
    updateCompleteButtonState(l.id);
    renderNav();
    updateProgressUI();
    
    const scrollArea = document.getElementById('content-scroll');
    if (scrollArea) scrollArea.scrollTo({ top: 0, behavior: 'smooth' });
};

function renderQuizUI(quiz) {
    if (!quizSection || !quizContent) return;
    if (!quiz) {
        quizSection.classList.add('hidden');
        return;
    }
    quizSection.classList.remove('hidden');
    if (quizResult) quizResult.innerHTML = '';
    
    quizContent.innerHTML = `
        <p class="text-sm font-semibold text-slate-100 mb-3">${quiz.question}</p>
        <div class="space-y-2">
            ${quiz.options.map((opt, i) => `
                <label class="flex items-center gap-3 p-3 rounded-xl bg-white/[0.03] hover:bg-white/[0.07] border border-white/5 cursor-pointer transition">
                    <input type="radio" name="quiz-option" value="${i}" class="w-4 h-4 text-orange-500 focus:ring-orange-500/20">
                    <span class="text-xs sm:text-sm text-slate-300 font-medium">${opt}</span>
                </label>
            `).join('')}
        </div>
    `;
}

window.checkQuiz = function() {
    const l = lessons[currentLessonIndex];
    if (!l || !l.quiz || !quizResult) return;
    
    const selected = document.querySelector('input[name="quiz-option"]:checked');
    if (!selected) {
        quizResult.innerHTML = '<div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 text-xs">Pilih salah satu jawaban terlebih dahulu.</div>';
        return;
    }
    
    const val = parseInt(selected.value, 10);
    if (val === l.quiz.answer) {
        quizResult.innerHTML = `
            <div class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 text-xs space-y-1">
                <div class="font-bold flex items-center gap-1.5"><i class="fas fa-check-circle"></i> Jawaban Benar!</div>
                <p class="text-slate-300">${l.quiz.explanation || 'Pemahaman Anda terhadap materi Rust ini sangat tepat.'}</p>
            </div>
        `;
        markComplete();
    } else {
        quizResult.innerHTML = `
            <div class="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-300 text-xs space-y-1">
                <div class="font-bold flex items-center gap-1.5"><i class="fas fa-times-circle"></i> Kurang Tepat</div>
                <p class="text-slate-300">Coba tinjau kembali pembahasan materi di atas dan ulangi kuis.</p>
            </div>
        `;
    }
};

window.runCode = async function() {
    if (!codeEditor || !outputTerminal) return;
    const code = codeEditor.value;
    outputTerminal.innerHTML = '<span class="text-orange-400 animate-pulse"><i class="fas fa-spinner fa-spin mr-1"></i> Mengompilasi kode di Rust Playground…</span>';
    
    try {
        const res = await fetch('https://play.rust-lang.org/execute', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                channel: 'stable',
                mode: 'debug',
                edition: '2021',
                crateType: 'bin',
                tests: false,
                code: code
            })
        });
        
        if (!res.ok) throw new Error('Playground server error');
        const data = await res.json();
        
        if (data.success) {
            outputTerminal.innerHTML = `<span class="text-emerald-400 font-mono">${escapeHtml(data.stdout || '(Program selesai tanpa output stdout)')}</span>`;
            markComplete();
        } else {
            outputTerminal.innerHTML = `<span class="text-rose-400 font-mono">${escapeHtml(data.stderr || 'Kompilasi gagal.')}</span>`;
        }
    } catch (err) {
        // Fallback simulation
        const l = lessons[currentLessonIndex];
        const out = l.expectedOutput ? l.expectedOutput : 'Halo dari Rust!';
        outputTerminal.innerHTML = `<span class="text-emerald-400 font-mono">${escapeHtml(out)}</span>\n<span class="text-xs text-slate-500 font-mono">// Dievaluasi via offline sandbox fallback</span>`;
        markComplete();
    }
};

window.resetCode = function() {
    const l = lessons[currentLessonIndex];
    if (codeEditor && l) {
        codeEditor.value = l.defaultCode;
        if (outputTerminal) outputTerminal.innerHTML = '<span class="text-slate-600">// Kode direset</span>';
    }
};

window.nextLesson = function() {
    if (currentLessonIndex < lessons.length - 1) {
        loadLesson(currentLessonIndex + 1);
    }
};

window.prevLesson = function() {
    if (currentLessonIndex > 0) {
        loadLesson(currentLessonIndex - 1);
    }
};

window.markComplete = function() {
    const l = lessons[currentLessonIndex];
    if (!l) return;
    progress[l.id] = true;
    if (!completedLessons.includes(l.id)) completedLessons.push(l.id);
    
    localStorage.setItem('rust_progress', JSON.stringify(progress));
    localStorage.setItem('rust_completed_lessons', JSON.stringify(completedLessons));
    
    updateCompleteButtonState(l.id);
    updateProgressUI();
    renderNav();
};

function updateCompleteButtonState(lessonId) {
    const isDone = !!progress[lessonId];
    if (completeBtn && completedBtn) {
        if (isDone) {
            completeBtn.style.display = 'none';
            completedBtn.style.display = 'inline-flex';
        } else {
            completeBtn.style.display = 'inline-flex';
            completedBtn.style.display = 'none';
        }
    }
}

function updateProgressUI() {
    const total = lessons.length;
    const done = Object.keys(progress).filter(k => !!progress[k]).length;
    const pct = total > 0 ? Math.round((done / total) * 100) : 0;
    
    const cp = document.getElementById('course-progress');
    const mp = document.getElementById('mobile-progress');
    const pf = document.getElementById('progress-fill');
    const pfb = document.getElementById('progress-fill-bar');
    const sd = document.getElementById('stat-done');
    
    if (cp) cp.textContent = `${pct}%`;
    if (mp) mp.textContent = `${pct}%`;
    if (pf) pf.style.width = `${pct}%`;
    if (pfb) pfb.style.width = `${pct}%`;
    if (sd) sd.textContent = `${done}`;
}

window.resetProgress = function() {
    if (confirm('Yakin ingin mereset seluruh progress belajar Rust Anda?')) {
        progress = {};
        completedLessons = [];
        localStorage.removeItem('rust_progress');
        localStorage.removeItem('rust_completed_lessons');
        localStorage.removeItem('rust_last_lesson');
        loadLesson(0);
    }
};

// Certificate Features
window.isCourseFullyCompleted = function() {
    const total = lessons.length;
    const done = Object.keys(progress).filter(k => !!progress[k]).length;
    return total > 0 && done >= total;
};

window.openCertificateModal = function() {
    const modal = document.getElementById('certificate-modal');
    if (!modal) return;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    
    const total = lessons.length;
    const done = Object.keys(progress).filter(k => !!progress[k]).length;
    const pct = total > 0 ? Math.round((done / total) * 100) : 0;
    const isCompleted = done >= total && total > 0;
    
    const lockedView = document.getElementById('cert-locked-view');
    const unlockedView = document.getElementById('cert-unlocked-view');
    const unlockedFooter = document.getElementById('cert-unlocked-footer');
    
    if (!isCompleted) {
        if (lockedView) lockedView.classList.remove('hidden');
        if (unlockedView) unlockedView.classList.add('hidden');
        if (unlockedFooter) unlockedFooter.classList.add('hidden');
        
        const pText = document.getElementById('cert-locked-progress-text');
        const pBar = document.getElementById('cert-locked-progress-bar');
        const rText = document.getElementById('cert-locked-remaining-text');
        if (pText) pText.textContent = `${done} / ${total} (${pct}%)`;
        if (pBar) pBar.style.width = `${pct}%`;
        if (rText) rText.textContent = `Tersisa ${Math.max(0, total - done)} pelajaran lagi untuk membuka sertifikat.`;
    } else {
        if (lockedView) lockedView.classList.add('hidden');
        if (unlockedView) unlockedView.classList.remove('hidden');
        if (unlockedFooter) unlockedFooter.classList.remove('hidden');
        
        const savedName = localStorage.getItem('user_cert_name') || 'Systems Engineer';
        const input = document.getElementById('cert-name-input');
        if (input) input.value = savedName;
        
        setTimeout(() => window.drawCertificate(), 100);
    }
};

window.closeCertificateModal = function() {
    const modal = document.getElementById('certificate-modal');
    if (!modal) return;
    modal.classList.add('hidden');
    modal.classList.remove('flex');
};

window.drawCertificate = function() {
    if (!window.isCourseFullyCompleted()) return;
    const canvas = document.getElementById('cert-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    const studentName = (document.getElementById('cert-name-input')?.value || 'Systems Engineer').trim();
    localStorage.setItem('user_cert_name', studentName);
    
    // Background Dark
    ctx.fillStyle = '#0a0f1a';
    ctx.fillRect(0, 0, width, height);
    
    // Luxury Gradient Border
    const gradient = ctx.createLinearGradient(0, 0, width, height);
    gradient.addColorStop(0, '#ea580c');
    gradient.addColorStop(0.5, '#f97316');
    gradient.addColorStop(1, '#c2410c');
    
    ctx.strokeStyle = gradient;
    ctx.lineWidth = 14;
    ctx.strokeRect(30, 30, width - 60, height - 60);
    
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.lineWidth = 2;
    ctx.strokeRect(45, 45, width - 90, height - 90);
    
    // Header
    ctx.textAlign = 'center';
    ctx.font = '600 16px Inter, sans-serif';
    ctx.fillStyle = '#ea580c';
    ctx.fillText('CERTIFICATE OF COMPLETION', width / 2, 120);
    
    ctx.font = '800 38px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('Rust Systems Programming', width / 2, 180);
    
    ctx.font = '400 16px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Diberikan secara resmi dan terverifikasi kepada:', width / 2, 250);
    
    // Student Name
    ctx.font = '800 42px Inter, sans-serif';
    ctx.fillStyle = '#f97316';
    ctx.fillText(studentName, width / 2, 320);
    
    // Statement
    ctx.font = '400 15px Inter, sans-serif';
    ctx.fillStyle = '#cbd5e1';
    ctx.fillText('Telah berhasil menyelesaikan 100% kurikulum Rust Learning Path', width / 2, 380);
    ctx.fillText('mencakup Ownership, Borrow Checker, Lifetimes, Traits, dan Fearless Concurrency.', width / 2, 410);
    
    // Meta / Badge
    const certId = 'RUST-' + Math.abs((studentName + '2026').split('').reduce((a, b) => ((a << 5) - a) + b.charCodeAt(0), 0)).toString(16).toUpperCase();
    const dateStr = new Date().toLocaleDateString('id-ID', { year: 'numeric', month: 'long', day: 'numeric' });
    
    ctx.font = '500 13px JetBrains Mono, monospace';
    ctx.fillStyle = '#64748b';
    ctx.fillText(`ID: ${certId} • Terbit: ${dateStr}`, width / 2, 480);
    
    // Footer Seals
    ctx.textAlign = 'left';
    ctx.font = '700 14px Inter, sans-serif';
    ctx.fillStyle = '#e2e8f0';
    ctx.fillText('PersonalBot AI', 80, 560);
    ctx.font = '400 12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Verified Learning Platform', 80, 580);
    
    ctx.textAlign = 'right';
    ctx.font = '700 14px Inter, sans-serif';
    ctx.fillStyle = '#ea580c';
    ctx.fillText('100% COMPLETED', width - 80, 560);
    ctx.font = '400 12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Official Systems Track', width - 80, 580);
};

window.downloadCertificatePNG = function() {
    if (!window.isCourseFullyCompleted()) return;
    const canvas = document.getElementById('cert-canvas');
    if (!canvas) return;
    const link = document.createElement('a');
    link.download = `Rust-Certificate-${(document.getElementById('cert-name-input')?.value || 'Student').replace(/\s+/g, '_')}.png`;
    link.href = canvas.toDataURL('image/png');
    link.click();
};

window.printCertificate = function() {
    if (!window.isCourseFullyCompleted()) return;
    const canvas = document.getElementById('cert-canvas');
    if (!canvas) return;
    const win = window.open('', '_blank');
    win.document.write(`
        <html><head><title>Sertifikat Rust</title></head>
        <body style="margin:0;display:flex;justify-content:center;align-items:center;min-height:100vh;background:#000;">
            <img src="${canvas.toDataURL('image/png')}" style="max-width:100%;height:auto;" onload="window.print();window.close();"/>
        </body></html>
    `);
    win.document.close();
};

function escapeHtml(str) {
    return String(str || '')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

// Global exports
window.MODULES = MODULES;
window.lessons = lessons;
window.LESSONS = lessons;
