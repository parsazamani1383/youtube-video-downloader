# YouTube Video Downloader

[فارسی](#فارسی) | [English](#english)

---

## فارسی

یک دانلودر ساده YouTube با Python و `yt-dlp`.

### نصب

ابتدا وابستگی‌ها را نصب کنید:

```bash
pip install -r requirements.txt

همچنین برای ترکیب صدا و تصویر به FFmpeg نیاز دارید.

اجرا
python main.py

سپس لینک ویدیو را وارد کنید. برنامه حجم تقریبی ویدیو را نمایش می‌دهد، برای دانلود تأیید می‌گیرد و در نهایت از شما می‌خواهد پوشه ذخیره‌سازی را انتخاب کنید.

کاربران ایران

اگر در ایران هستید و YouTube از شبکه شما قابل دسترسی نیست، از یک VPN استفاده کنید.

توجه کنید که VPN باید برای اتصال Python نیز فعال باشد؛ صرفاً فعال بودن VPN داخل مرورگر ممکن است کافی نباشد.

English

A simple YouTube video downloader built with Python and yt-dlp.

Installation

Install the dependencies:

pip install -r requirements.txt

FFmpeg is also required to merge video and audio streams.

Usage

Run the program:

python main.py

Enter the YouTube video URL. The program shows the estimated file size, asks for confirmation, and lets you choose where to save the video.

Users in Iran

If you are using this project in Iran and YouTube is not accessible from your network, use a VPN.

Make sure the VPN also works for Python. A browser-only VPN extension may not be enough.

License

MIT
