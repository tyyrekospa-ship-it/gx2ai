import streamlit as st
import requests
import random
import time
from uuid import uuid4

# إعدادات الصفحة (تم تصحيح الخطأ هنا)
st.set_page_config(
    page_title="MIKHAEL Hunter",
    page_icon="👑",
    layout="centered"
)

# تصميم واجهة فخمة باستخدام CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #888;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">❖ MIKHAEL HUNTER 👑</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">تطبيق فحص وتخمين يوزرات انستغرام بأحدث الأنماط</div>', unsafe_allow_html=True)

# إعداد الجلسات لحفظ الإحصائيات
if 'hits' not in st.session_state:
    st.session_state.hits = 0
if 'bad' not in st.session_state:
    st.session_state.bad = 0
if 'found_users' not in st.session_state:
    st.session_state.found_users = []

# الأحرف المسموحة فقط والأرقام
letters = 'asfjlioprtvcxznv'
digits = '0123456789'

def generate_username(pattern_choice):
    if pattern_choice == 1:
        # نمط a.ss1 (حرف . حرف حرف رقم)
        return f"{random.choice(letters)}.{random.choice(letters)}{random.choice(letters)}{random.choice(digits)}"
    elif pattern_choice == 2:
        # نمط s.uio (حرف . 3 أحرف)
        return f"{random.choice(letters)}.{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}"
    else:
        # خليط عشوائي
        if random.choice([True, False]):
            return f"{random.choice(letters)}.{random.choice(letters)}{random.choice(letters)}{random.choice(digits)}"
        else:
            return f"{random.choice(letters)}.{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}"

def check_username(user):
    url = 'https://i.instagram.com/api/v1/accounts/create/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
        'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
        'Accept-Language': 'en-IQ, en-US',
    }
    data = {
        "email": f"test_{random.randint(1000,9999)}@gmail.com",
        "username": user,
        "password": "Password123@" + user,
        "device_id": "android-" + str(uuid4()),
        "guid": str(uuid4()),
    }
    try:
        res = requests.post(url, headers=headers, data=data, timeout=7)
        if 'email_is_taken' in res.text:
            return True # متاح
        elif 'username' in res.text:
            return False # غير متاح
        return None
    except:
        return None

def send_telegram(bot_token, chat_id, user):
    if bot_token and chat_id:
        try:
            msg = f"✅ Available Instagram User: @{user}\nBy MIKHAEL"
            requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={'chat_id': chat_id, 'text': msg}, timeout=5)
        except:
            pass

# الواجهة الرئيسية
st.sidebar.header("⚙️ إعدادات الإرسال")
bot_token = st.sidebar.text_input("Bot Token", type="password")
chat_id = st.sidebar.text_input("Chat ID")

pattern = st.radio(
    "اختر نمط التخمين:",
    [1, 2, 3],
    format_func=lambda x: {
        1: "1- نمط (a.ss1) -> (حرف . حرفين ورقم)",
        2: "2- نمط (s.uio) -> (حرف . 3 أحرف)",
        3: "3- خليط عشوائي بين النمطين"
    }[x]
)

st.write("---")

col1, col2, col3 = st.columns(3)
metric_good = col1.metric("المتاحة (Good)", st.session_state.hits)
metric_bad = col2.metric("المستعملة (Bad)", st.session_state.bad)
status_box = col3.empty()

start_button = st.button("🚀 بدء الصيد والتخمين")

if start_button:
    st.info("جاري الفحص الآن...")
    
    while True:
        user = generate_username(pattern)
        status_box.markdown(f"**جاري فحص:** `{user}`")
        
        result = check_username(user)
        
        if result is True:
            st.session_state.hits += 1
            st.session_state.found_users.append(user)
            st.success(f"🎯 تم إيجاد يوزر متاح: @{user}")
            send_telegram(bot_token, chat_id, user)
            metric_good.metric("المتاحة (Good)", st.session_state.hits)
        elif result is False:
            st.session_state.bad += 1
            metric_bad.metric("المستعملة (Bad)", st.session_state.bad)
            
        time.sleep(0.5)

if st.session_state.found_users:
    st.write("### 📋 اليوزرات المقبولة:")
    st.text_area("Hits", value="\n".join(st.session_state.found_users), height=150)

