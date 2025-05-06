# 📰 PyGazette

**PyGazette** is a lightweight Python script that fetches the latest news articles using Google's Custom Search Engine (CSE) API. It allows users to search based on custom keywords and time filters, returning a personalized, chronological set of results.

---

## 🚀 Features

- Fetches real-time news articles from Google Search results.
- Filters results based on custom **keywords** and **date ranges** (recency).
- Automatically paginates through up to 100 results (Google's API limit).
- Outputs a clean, readable summary: **Title, snippet and article link**.

---

## 🛠️ Setup Instructions

### 1. 🔑 Get Google Custom Search API Key

- Go to the [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project or use an existing one.
- Navigate to **APIs & Services > Credentials**
- Click **Create Credentials > API Key**
- Copy and save this key safely.

### 2. 🔍 Set Up Google Custom Search Engine (CSE)

- Visit the [CSE Control Panel](https://programmablesearchengine.google.com/)
- Click **Add** to create a new search engine.
- In the “Sites to Search” field, enter: `www.google.com` (or leave empty to search the entire web)
- After creating it, go to **Control Panel > Search Engine ID**
- Copy your **Search Engine ID**

---

## 📦 Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/StrongCapybara/PyGazette.git
   cd PyGazette
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests
   ```

3. **Edit the script**:

   Open the Python script and replace the following lines with your own credentials:
   ```python
   api = "Insert your CSE API Key"
   sid = "Insert your Search Engine ID"
   ```

---

## 🧪 Usage

Run the script using:

```bash
python Clarky.py
```

You’ll be prompted to enter:
- A search query
- Number of results (max 100)
- Date restriction (e.g., past 3 days → enter `3`)
- Keywords (for filtering)

---

## 🧠 Example Output

```
Enter your search terms: AI in medicine
Enter the number of results that you want(≤100): 5
Enter the number of days you want to restrict the search to: 7
Enter Keywords (at least 1): AI,healthcare

========== Result #1 ==========
Title: How AI is Transforming Healthcare in 2024
Description: New developments in AI are enabling doctors to diagnose faster and more accurately.
URL: https://example.com/article1

...
```

---

## 🔧 Customization

You can change default sorting (`sort = "date"`) or extend the script to support other filtering options like:
- Language
- Country-specific results
- File types, etc.

Refer to the [Custom Search JSON API documentation](https://developers.google.com/custom-search/v1/using_rest) for more.

---

## 👨‍💻 Author

This project was developed as part of a learning module to explore Python scripting and web APIs.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
