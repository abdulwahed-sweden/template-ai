# DeepSeek Django Async Form

This Django app provides an async API integration with DeepSeek's chat API. Users can select a topic from a dropdown, submit it, and receive a response asynchronously via the frontend.

## 🔧 Features

- Dynamic select dropdown form
- Async Django view using `httpx`
- Integration with DeepSeek Chat API
- Loading state and error handling in frontend
- Environment-based API key management

## 🗂 Project Structure

```
myproject/
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── myapp/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── myapp/
│           └── form.html
├── .env
├── manage.py
└── README.md
```

## 🚀 Setup Instructions

### 1. Clone the repo & install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env` file
```env
DEEPSEEK_API_KEY=your_new_key_here
```

> 🔒 Keep your `.env` out of version control!

### 3. Run migrations & server
```bash
python manage.py migrate
python manage.py runserver
```

### 4. Visit the form
Open [http://localhost:8000/form/](http://localhost:8000/form/)

## 📦 Requirements

- Django >= 4.1
- httpx
- python-dotenv

Install with:
```bash
pip install django httpx python-dotenv
```

## ✅ Example API Flow

1. User selects "Python" from dropdown
2. Clicks submit — async POST request sent to `/api/query/`
3. Django view sends request to DeepSeek API
4. Response is returned and displayed on page

---

## ⚠️ Security Note
- Never expose your API keys publicly
- Always use environment variables for secrets
- Add `.env` to `.gitignore`

---

## 📄 License
MIT
