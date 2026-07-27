import streamlit as st
import requests
from user_agent import generate_user_agent

# إعدادات الصفحة
st.set_page_config(
    page_title="زيادة مشاهدات ستوري - gx1ai & gx2ai",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم الـ CSS وحذف شريط جيتها والتأكد من إظهار HTML بشكل صحيح
st.markdown("""
<style>
    #MainMenu, footer, header, .stAppHeader, div[data-testid="stToolbar"] {
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
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #00b4d8;
        box-shadow: 0 0 20px rgba(0, 180, 216, 0.6);
        margin-bottom: 15px;
    }
    
    .main-title {
        color: #90e0ef;
        font-weight: 800;
        font-size: 24px;
        margin-bottom: 8px;
    }
    
    .telegram-btn {
        display: inline-block;
        background: linear-gradient(135deg, #0088cc 0%, #005f73 100%);
        color: #ffffff !important;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 14px;
        box-shadow: 0 4px 15px rgba(0, 136, 204, 0.4);
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

# رأس الصفحة والصورة وروابط القنوات
st.markdown("""
<div class="main-card">
    <img src="https://files.catbox.moe/868tll.jpg" class="channel-logo-img">
    <div class="main-title">🚀 أداة زيادة مشاهدات ستوري انستغرام</div>
    <div style="color: #8d99ae; font-size: 14px; margin-bottom: 15px;">مشاهدات استوري انستكرام الى اي حساب عن طريق اليوزر</div>
    <div>
        <a href="https://t.me/gx1ai" target="_blank" class="telegram-btn"> قناة 1 gx1ai</a>
        <a href="https://t.me/gx2ai" target="_blank" class="telegram-btn"> قناة 2 gx2ai</a>
    </div>
</div>
""", unsafe_allow_html=True)

# إدخال اليوزر
username = st.text_input("يوزر الحساب (Username):", placeholder="أدخل اسم المستخدم")

if st.button("⚡ بدء إرسال مشاهدات الستوري"):
    if not username:
        st.error("⚠️ يرجى إدخال اسم المستخدم أولاً!")
    else:
        with st.spinner("جاري إرسال الطلب للسيرفر..."):
            cookies = {
                'token': '00bae069a44c19e57b123978b36af6b6',
                'ci_session': 'a0d141ca691e47c5a358a98554df38301864611c',
                'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1800543670515%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1769007675006%2C%22e%22%3A1800543675008%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2212%22%2C%22e%22%3A1800543670515%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%221741539026%22%2C%22e%22%3A1769009470515%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%221%22%2C%22e%22%3A1800543670515%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%222fd4a2bd-d604-4661-8b9d-fc1447404fdb%22%2C%22e%22%3A1800543670515%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221769007670515%22%2C%22e%22%3A1800543670515%7D%7D',
            }

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
                'user-agent': str(generate_user_agent()),
            }

            params = {
                'api': '1',
            }

            data = {
                'token': '00bae069a44c19e57b123978b36af6b6',
                'timezone_offset': 'Asia/Baghdad',
                'free_link': username,
            }

            try:
                response = requests.post(
                    'https://leofame.com/free-instagram-story-views',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                ).text

                if '"error":"We have a limit on free orders. Please try again in 20 hours."' in response:
                    st.warning("⚠️ وصلت للحد الأقصى المجاني! يرجى المحاولة بعد 20 ساعة.")
                else:
                    st.success(f"☑️ DONE! تم إرسال مشاهدات الستوري بنجاح للحساب: {username}")
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال: {e}")
