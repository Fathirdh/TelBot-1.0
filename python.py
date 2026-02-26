import json
from difflib import SequenceMatcher

# 1. DATA FAQ (Tetap sama)
faq_data = [
    {"Category": "Administrasi", "Question": "Bagaimana cara ganti email karena email lama tidak aktif?", "Answer": "Silakan kirimkan data (Nama, No KTP, Email Lama/Baru, Foto KTP) melalui email ke Helpdesk kami.", "Link_URL": "mailto:helpdesk.recruitment@telkom.co.id"},
    {"Category": "Administrasi", "Question": "Bagaimana cara input data pendidikan terakhir?", "Answer": "Isi data di menu Profil/CV pada website recruitment sesuai kondisi saat ini. Login untuk update data.", "Link_URL": "https://recruitment.telkom.co.id/login"},
    {"Category": "Administrasi", "Question": "Bisakah meminta file Surat Pernyataan?", "Answer": "Anda dapat mengunduh template Surat Pernyataan melalui link Google Drive berikut ini.", "Link_URL": "[LINK_GDRIVE_KAMU_DISINI]"},
    {"Category": "Teknis Tes", "Question": "Berapa lama durasi online test?", "Answer": "Durasi sesuai jadwal di email/website (WIB). Silakan login untuk mengecek detail jadwal Anda.", "Link_URL": "https://recruitment.telkom.co.id/login"},
    {"Category": "Teknis Tes", "Question": "Bisakah saya reschedule jadwal tes?", "Answer": "Mohon maaf, tidak bisa reschedule dengan alasan apapun. Jadwal bersifat mutlak. Cek jadwal Anda disini.", "Link_URL": "https://recruitment.telkom.co.id/login"},
    {"Category": "Teknis Tes", "Question": "Soal tes essay bidang tidak muncul, solusinya?", "Answer": "Refresh halaman website recruitment, lalu coba login ulang. Pastikan koneksi stabil.", "Link_URL": "https://recruitment.telkom.co.id"},
    {"Category": "Teknis Tes", "Question": "Belum terima email trial psikotes, harus gimana?", "Answer": "Cek folder SPAM. Cari pengirim 'Admin E-Psikotes'. Jika masih tidak ada, silakan hubungi Helpdesk.", "Link_URL": "https://t.me/HelpdeskTelkom"},
    {"Category": "Teknis Tes", "Question": "Bagaimana jika belum mengerjakan essay?", "Answer": "Tetap ikuti tahapan Assessment Days selanjutnya sesuai jadwal. Cek jadwal berikutnya di dashboard.", "Link_URL": "https://recruitment.telkom.co.id/login"},
    {"Category": "Jadwal", "Question": "Kapan jadwal Psikotes dan Assessment Day?", "Answer": "Jadwal diinfokan via email dan notifikasi dashboard website recruitment. Cek secara berkala.", "Link_URL": "https://recruitment.telkom.co.id"}
]

# Ambil input user
user_query = _input.item.json.get('body', {}).get('query', '').lower()

# Cari Top 3 FAQ yang relevan
scored_faqs = []
for item in faq_data:
    question = item['Question'].lower()
    score = SequenceMatcher(None, user_query, question).ratio()
    if user_query in question: score += 0.2
    scored_faqs.append((score, item))

# Urutkan dari score tertinggi dan ambil 3 teratas
scored_faqs.sort(key=lambda x: x[0], reverse=True)
top_matches = scored_faqs[:3]

# Format Context String untuk LLM
context_text = ""
for score, match in top_matches:
    # Hanya masukkan ke context jika kemiripan minimal 20%
    if score > 0.2:
        context_text += f"Q: {match['Question']}\nA: {match['Answer']}\nLink: {match['Link_URL']}\n---\n"

# Jika tidak ada context yang relevan sama sekali
if not context_text:
    context_text = "Tidak ada data spesifik di database mengenai hal ini."

return {'json': {'context': context_text, 'user_query': user_query}}