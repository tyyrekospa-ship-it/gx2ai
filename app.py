import streamlit as st
import requests
from user_agent import generate_user_agent
import re

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="زيادة مشاهدات ستوري - gx1ai & gx2ai",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تحسينات CSS لإخفاء هيدر وحقوق جيتها مع تطبيق التصميم الأزرق
st.markdown("""
<style>
    /* إخفاء عناصر Streamlit و GitHub الافتراضية */
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

# واجهة القنوات والصورة
st.markdown("""
<div class="main-card">
    <img src="https://files.catbox.moe/868tll.jpg" class="channel-logo-img">
    <div class="main-title"> أداة زيادة مشاهدات ستوري انستغرام</div>
    <div style="color: #8d99ae; font-size: 13px; margin-bottom: 15px;">رشق حقيقي ومباشر - سيرفر leofame</div>
    <div>
        <a href="https://t.me/gx1ai" target="_blank" class="telegram-btn"> قناة 2 gx1ai</a>
        <a href="https://t.me/gx2ai" target="_blank" class="telegram-btn">✈️ قناة 1 gx2ai</a>
    </div>
</div>
""", unsafe_allow_html=True)

# مدخل اسم المستخدم
username = st.text_input("Enter Your username =>", placeholder="أدخل اسم المستخدم هنا")

if st.button("⚡ بدء إرسال مشاهدات الستوري"):
    if not username:
        st.error("⚠️ يرجى إدخال اسم المستخدم أولاً!")
    else:
        with st.spinner("جاري الاتصال بالسيرفر وتوليد الجلسة..."):
            try:
                # إنشاء جلسة ديناميكية لجلب الكوكيز والتوكن الحقيقي
                session = requests.Session()
                ua = generate_user_agent()
                
                # Step 1: فتح الصفحة الرئيسية لجلب الجلسة الحقيقية
                init_headers = {
                    'authority': 'leofame.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'user-agent': ua,
                }
                
                get_resp = session.get('https://leofame.com/free-instagram-story-views', headers=init_headers, timeout=10)
                
                # استخراج التوكن Dynamic Token من استجابة الصفحة
                token_match = re.search(r'name=["\']token["\']\s+value=["\']([^"\']+)["\']', get_resp.text)
                if token_match:
                    dynamic_token = token_match.group(1)
                else:
                    dynamic_token = '00bae069a44c19e57b123978b36af6b6'

                # Step 2: إرسال طلب الرشق بالبيانات الحية
                headers = {
                    'authority': 'leofame.com',
                    'accept': '*/*',
                    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://leofame.com',
                    'referer': 'https://leofame.com/free-instagram-story-views',
                    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': ua,
                }

                params = {'api': '1'}

                data = {
                    'token': dynamic_token,
                    'timezone_offset': 'Asia/Baghdad',
                    'free_link': username.strip(),
                }

                response = session.post(
                    'https://leofame.com/free-instagram-story-views',
                    params=params,
                    headers=headers,
                    data=data,
                    timeout=15
                ).text

                # التحقق من استجابة الكود
                if '"error":"We have a limit on free orders. Please try again in 20 hours."' in response or 'limit on free orders' in response:
                    st.warning('"error":"We have a limit on free orders. Please try again in 20 hours."')
                elif 'DONE' in response or '"success"' in response or 'success' in response.lower():
                    st.success(f'DONE☑')
                else:
                    # إظهار النتيجة كما هي في بايثون
                    if '"error"' in response:
                        st.error(f"تنبيه السيرفر: {response}")
                    else:
                        st.success(f'DONE☑')
                        
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال بالسيرفر: {e}")
