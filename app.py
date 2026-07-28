import streamlit as st
import requests
import random
import time
from uuid import uuid4

# إعدادات الصفحة
st.set_page_config(
    page_title="gx2ai | MIKHAEL Hunter",
    page_icon="👑",
    layout="centered"
)

# استخدام الجلسة لزيادة السرعة بأقصى درجة
if 'http_session' not in st.session_state:
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
        'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
        'Accept-Language': 'en-IQ, en-US',
    })
    st.session_state.http_session = session

# تصميم واجهة خرافية، فخمة، وألوان أنيقة مع حقوق gx2ai
st.markdown("""
<style>
    /* خلفية وألوان عامة */
    .stApp {
        background-color: #0b0e14;
        color: #e0e6ed;
    }
    
    /* العنوان الرئيسي */
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #FFD700 0%, #FF4500 50%, #8A2BE2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 0px;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.3);
    }
    
    /* الحقوق والشعار الفرعي */
    .rights-tag {
        text-align: center;
        color: #00E5FF;
        font-size: 1.2rem;
        font-weight: bold;
        letter-spacing: 4px;
        margin-top: 5px;
        margin-bottom: 10px;
        text-shadow: 0px 0px 10px rgba(0, 229, 255, 0.5);
    }
    
    .sub-title {
        text-align: center;
        color: #8b9bb4;
        font-size: 1rem;
        margin-bottom: 25px;
    }

    /* كروت الإحصائيات */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: bold;
    }
    
    /* تحسين زر التشغيل */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FFD700 0%, #FF4500 100%);
        color: #000000 !important;
        font-size: 1.2rem !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        height: 3.2em !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 215, 0, 0.6);
    }

    /* الشريط الجانبي */
    section[data-testid="stSidebar"] {
        background-color: #121824;
        border-right: 1px solid #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر الفخم
st.markdown('<div class="main-title">❖ MIKHAEL HUNTER 👑</div>', unsafe_allow_html=True)
st.markdown('<div class="rights-tag">POWERED BY gx2ai</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">أقوى وأسرع أداة فحص صيد يوزرات انستغرام التفاعلية</div>', unsafe_allow_html=True)

# إعداد الجلسات لحفظ الإحصائيات
if 'hits' not in st.session_state:
    st.session_state.hits = 0
if 'bad' not in st.session_state:
    st.session_state.bad = 0
if 'found_users' not in st.session_state:
    st.session_state.found_users = []

# الأحرف المسموحة والأرقام والحروف الكبيرة لبعض الأنماط
letters_lower = 'asfjl6387650123wertyuiopasdfghjklxzvnioprtvcxznv'
letters_upper = 'ASFJLIOhjklfdwqmnbvczytuiPRTVCXZNV'
digits = '0123456789'

def generate_username(pattern_choice):
    l_low = letters_lower
    l_up = letters_upper
    d = digits
    
    if pattern_choice == 1:
        # نمط a.ss1 (حرف . حرف حرف رقم)
        return f"{random.choice(l_low)}.{random.choice(l_low)}{random.choice(l_low)}{random.choice(d)}"
    elif pattern_choice == 2:
        # نمط s.uio (حرف . 3 أحرف)
        return f"{random.choice(l_low)}.{random.choice(l_low)}{random.choice(l_low)}{random.choice(l_low)}"
    elif pattern_choice == 3:
        # النمط المطلووب: AS_6f (حرفين كبار _ رقم وحرف)
        return f"{random.choice(l_up)}{random.choice(l_up)}_{random.choice(d)}{random.choice(l_low)}"
    elif pattern_choice == 4:
        # نمط عشوائي 1: _a1s_ (شخط جانبية + 3 خانات + شخط جانبية)
        return f"_{random.choice(l_low)}{random.choice(d)}{random.choice(l_low)}_"
    elif pattern_choice == 5:
        # نمط عشوائي 2: a1_s2 (حرف رقم _ حرف رقم)
        return f"{random.choice(l_low)}{random.choice(d)}_{random.choice(l_low)}{random.choice(d)}"
    elif pattern_choice == 6:
        # نمط عشوائي 3: a.1.s (حرف . رقم . حرف)
        return f"{random.choice(l_low)}.{random.choice(d)}.{random.choice(l_low)}"
    elif pattern_choice == 7:
        # نمط عشوائي 4: 99_as (رقمين _ حرفين)
        return f"{random.choice(d)}{random.choice(d)}_{random.choice(l_low)}{random.choice(l_low)}"
    elif pattern_choice == 8:
        # نمط عشوائي 5: a_s_1 (حرف _ حرف _ رقم)
        return f"{random.choice(l_low)}_{random.choice(l_low)}_{random.choice(d)}"
    else:
        # خليط عشوائي شامل لجميع الأنماط
        return generate_username(random.randint(1, 8))

def check_username(user):
    url = 'https://i.instagram.com/api/v1/accounts/create/'
    data = {
        "email": f"gx_{random.randint(10000,99999)}@gmail.com",
        "username": user,
        "password": "Password123@" + user,
        "device_id": "android-" + str(uuid4()),
        "guid": str(uuid4()),
    }
    try:
        res = st.session_state.http_session.post(url, data=data, timeout=5)
        if 'email_is_taken' in res.text:
            return True   # متاح (Good)
        elif 'username' in res.text:
            return False  # غير متاح (Bad)
        return None
    except:
        return None

def send_telegram(bot_token, chat_id, user):
    if bot_token and chat_id:
        try:
            msg = f"🔥 AVAILABLE USER FOUND!\n\n👑 User: @{user}\n⚡ Dev: gx2ai & MIKHAEL\n⏰ Time: {time.strftime('%H:%M:%S')}"
            requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={'chat_id': chat_id, 'text': msg}, timeout=4)
        except:
            pass

# الشريط الجانبي للإعدادات
st.sidebar.markdown("### ⚡ إعدادات التلغرام")
bot_token = st.sidebar.text_input("Bot Token", type="password")
chat_id = st.sidebar.text_input("Chat ID")

st.sidebar.markdown("---")
st.sidebar.markdown("### 👑 DEV: **gx2ai**")

# اختيار الأنماط
pattern = st.radio(
    "🎯 اختر نمط الصيد والتخمين:",
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    format_func=lambda x: {
        1: "1- نمط (a.ss1) -> (حرف . حرفين ورقم)",
        2: "2- نمط (s.uio) -> (حرف . 3 أحرف)",
        3: "3- نمط (AS_6f) -> (حرفين كبار _ رقم وحرف)",
        4: "4- نمط (_a1s_) -> (_3 خانات_)",
        5: "5- نمط (a1_s2) -> (حرف رقم _ حرف رقم)",
        6: "6- نمط (a.1.s) -> (حرف . رقم . حرف)",
        7: "7- نمط (99_as) -> (رقمين _ حرفين)",
        8: "8- نمط (a_s_1) -> (حرف _ حرف _ رقم)",
        9: "🔥 عشوائي شامل لكل الأنماط أعلاه"
    }[x]
)

st.write("---")

# العدادات والشاشات
col1, col2, col3 = st.columns(3)
metric_good = col1.metric("🔥 المتاحة (Good)", st.session_state.hits)
metric_bad = col2.metric("❌ المستعملة (Bad)", st.session_state.bad)
status_box = col3.empty()

start_button = st.button("🚀 ابدأ الصيد والتخمين الآن")

if start_button:
    st.info("⚡ تم تشغيل المحرك بواسطة gx2ai.. جاري الفحص السريع...")
    
    while True:
        user = generate_username(pattern)
        status_box.markdown(f"🔍 **جاري فحص:** `{user}`")
        
        result = check_username(user)
        
        if result is True:
            st.session_state.hits += 1
            st.session_state.found_users.append(user)
            
            # إطلاق الاحتفالات والفرح عند إيجاد يوزر! 🎉
            st.balloons()
            st.snow()
            
            st.success(f"🎉 🎉 MIKHAEL & gx2ai WON! يوزر متاح: @{user}")
            send_telegram(bot_token, chat_id, user)
            metric_good.metric("🔥 المتاحة (Good)", st.session_state.hits)
            
        elif result is False:
            st.session_state.bad += 1
            metric_bad.metric("❌ المستعملة (Bad)", st.session_state.bad)
            
        # سرعة فحص ممتازة مع تقليل الضغط
        time.sleep(0.1)

if st.session_state.found_users:
    st.write("### 📋 قائمة الصيد المقبولة (Hits):")
    st.text_area("Hits", value="\n".join(st.session_state.found_users), height=180)

