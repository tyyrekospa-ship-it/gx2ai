import streamlit as st
import requests
from user_agent import generate_user_agent
import re
import time
import random
import concurrent.futures

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="زيادة مشاهدات ستوري - gx1ai & gx2ai",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم الـ CSS الخاص بالتطبيق وإخفاء حقوق GitHub والهيدر
st.markdown("""
<style>
    #MainMenu, footer, header, .stAppHeader, div[data-testid="stToolbar"], div[data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #090e17 0%, #0d1b2a 50%, #1b263b 100%);
        color: #e0e1dd;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(0, 180, 216, 0.3);
        border-radius: 20px;
        padding: 25px 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        text-align: center;
    }
    
    .channel-logo-img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #00b4d8;
        box-shadow: 0 0 20px rgba(0, 180, 216, 0.6);
        margin-bottom: 15px;
    }
    
    .main-title {
        color: #90e0ef;
        font-weight: 800;
        font-size: 22px;
        margin-bottom: 8px;
    }
    
    .telegram-btn {
        display: inline-block;
        background: linear-gradient(135deg, #0088cc 0%, #005f73 100%);
        color: #ffffff !important;
        padding: 8px 18px;
        margin: 5px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 13px;
        box-shadow: 0 4px 12px rgba(0, 136, 204, 0.4);
    }
    
    div[data-baseweb="input"] {
        background-color: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid rgba(0, 180, 216, 0.4) !important;
        border-radius: 12px !important;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #0077b6 0%, #00b4d8 100%);
        color: white;
        font-weight: bold;
        font-size: 16px;
        border: none;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 5px 15px rgba(0, 180, 216, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# واجهة الهيدر والقنوات والصورة
st.markdown("""
<div class="main-card">
    <img src="https://files.catbox.moe/868tll.jpg" class="channel-logo-img">
    <div class="main-title">🚀 أداة زيادة مشاهدات ستوري انستغرام</div>
    <div style="color: #8d99ae; font-size: 13px; margin-bottom: 15px;">نظام هجوم البروكسيات المتعددة والأجهزة المختلفة (Multi-Threading)</div>
    <div>
        <a href="https://t.me/gx1ai" target="_blank" class="telegram-btn">✈️ قناة gx1ai</a>
        <a href="https://t.me/gx2ai" target="_blank" class="telegram-btn">✈️ قناة gx2ai</a>
    </div>
</div>
""", unsafe_allow_html=True)

# قائمة بروكسيات عامة سريعة ومفتوحة للتغيير التلقائي
PUBLIC_PROXIES = [
    "http://188.166.220.129:3128",
    "http://165.225.206.20:80",
    "http://51.159.22.190:80",
    "http://138.68.60.8:8080",
    "http://45.152.188.243:3128",
    "http://159.65.133.153:80"
]

def generate_random_device():
    """توليد جهاز، نظام، وإصدار متصفح مختلف في كل طلب"""
    platforms = ['"Android"', '"Linux"', '"Windows"', '"iOS"']
    versions = ['120', '121', '122', '123', '124', '125', '126']
    
    device_info = {
        'user-agent': str(generate_user_agent()),
        'sec-ch-ua': f'"Chromium";v="{random.choice(versions)}", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': f'?{random.choice([0, 1])}',
        'sec-ch-ua-platform': random.choice(platforms)
    }
    return device_info

def send_story_request(target_username):
    """دالة تنفيذ طلب الرشق عبر جهاز مختلف وبانسجام مع السيرفر"""
    device = generate_random_device()
    session = requests.Session()
    
    # اختيار بروكسي عشوائي من القائمة أو الاتصال المباشر المتجدد
    use_proxy = random.choice([True, False])
    proxy_dict = {}
    if use_proxy:
        p = random.choice(PUBLIC_PROXIES)
        proxy_dict = {"http": p, "https": p}
        
    try:
        init_headers = {
            'authority': 'leofame.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': device['user-agent'],
        }
        
        # 1. جلب الصفحة لإنشاء جلسة توكن
        get_resp = session.get(
            'https://leofame.com/free-instagram-story-views',
            headers=init_headers,
            proxies=proxy_dict,
            timeout=8
        )
        
        token_match = re.search(r'name=["\']token["\']\s+value=["\']([^"\']+)["\']', get_resp.text)
        dynamic_token = token_match.group(1) if token_match else '00bae069a44c19e57b123978b36af6b6'

        # 2. إرسال الهجوم بالبيانات ورأس الجهاز القادم من بيئة مختلفة
        headers = {
            'authority': 'leofame.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://leofame.com',
            'referer': 'https://leofame.com/free-instagram-story-views',
            'sec-ch-ua': device['sec-ch-ua'],
            'sec-ch-ua-mobile': device['sec-ch-ua-mobile'],
            'sec-ch-ua-platform': device['sec-ch-ua-platform'],
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': device['user-agent'],
        }

        params = {'api': '1'}
        data = {
            'token': dynamic_token,
            'timezone_offset': 'Asia/Baghdad',
            'free_link': target_username,
        }

        response = session.post(
            'https://leofame.com/free-instagram-story-views',
            params=params,
            headers=headers,
            data=data,
            proxies=proxy_dict,
            timeout=10
        ).text

        if 'DONE' in response or '"success"' in response or 'success' in response.lower():
            return True, "DONE"
        else:
            return False, response
            
    except Exception as ex:
        return False, str(ex)

# أدخل اليوزر
username = st.text_input("Enter Your username =>", placeholder="أدخل اسم المستخدم هنا")

if st.button("⚡ بدء الرشق عبر بروكسيات وأجهزة متعددة"):
    if not username:
        st.error("⚠️ يرجى إدخال اسم المستخدم أولاً!")
    else:
        status_box = st.empty()
        log_box = st.empty()
        
        target = username.strip()
        attempts = 0
        success = False
        
        status_box.info("🚀 جاري بدء نظام المحاولات المتعددة والأجهزة المختلفة...")
        
        # حلقة تكرار بالخلفية مستمرة حتى ينجح الطلب 100%
        while not success:
            attempts += 1
            log_box.info(f"🔄 محاولة رقم [{attempts}]: جاري تغيير الأي بي (IP) والجهاز وإرسال الطلب...")
            
            # تنفيذ المحاولات متوازية الخيوط (Multi-threading) لتسريع العملية
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                futures = [executor.submit(send_story_request, target) for _ in range(3)]
                
                for future in concurrent.futures.as_completed(futures):
                    is_ok, res_text = future.result()
                    if is_ok:
                        success = True
                        break
            
            if success:
                status_box.empty()
                log_box.empty()
                st.success(f"🎉 DONE☑ - تم نجاح إرسال مشاهدات الستوري بعد {attempts} محاولة للحساب: {target}")
                st.balloons()
                break
            else:
                time.sleep(1)
