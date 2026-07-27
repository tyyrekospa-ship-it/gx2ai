import streamlit as st
import requests
from user_agent import generate_user_agent

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="LeoFame Story Views - gx1ai & gx2ai",
    page_icon="⚡",
    layout="centered"
)

# تصميم الواجهة باستخدام CSS باللون الأزرق والمؤثرات البصرية
st.markdown("""
<style>
    /* خلفية الصفحة بدراجات اللون الأزرق */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0284c7 100%);
        color: #ffffff;
    }
    
    /* تصميم بطاقة المحتوى (Glassmorphism Effect) */
    .main-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
    }
    
    /* الحقوق والشعار */
    .rights-header {
        text-align: center;
        font-weight: 800;
        font-size: 24px;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    .rights-sub {
        text-align: center;
        color: #93c5fd;
        font-size: 14px;
        margin-bottom: 25px;
    }
    
    /* زر الإرسال */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #2563eb, #0284c7);
        color: white;
        font-weight: bold;
        font-size: 18px;
        border-radius: 12px;
        border: none;
        padding: 12px 24px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #0369a1);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(2, 132, 199, 0.6);
    }
    
    /* خانة الإدخال */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.07) !important;
        color: #ffffff !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# رأس الواجهة والحقوق
st.markdown('<div class="rights-header">🚀 IG Story Views Booster</div>', unsafe_allow_html=True)
st.markdown('<div class="rights-sub">Powered by <b>gx1ai</b> & <b>gx2ai</b></div>', unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# إدخال اسم المستخدم
username = st.text_input("أدخل اسم المستخدم (Username):", placeholder="مثال: instagram")

if st.button("إرسال الطلب ⚡"):
    if not username:
        st.warning("⚠️ يرجى إدخال اسم المستخدم أولاً.")
    else:
        with st.spinner("جاري تنفيذ الطلب والاتصال بالسيرفر..."):
            try:
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

                params = {'api': '1'}

                data = {
                    'token': '00bae069a44c19e57b123978b36af6b6',
                    'timezone_offset': 'Asia/Baghdad',
                    'free_link': username,
                }

                response = requests.post(
                    'https://leofame.com/free-instagram-story-views',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                ).text

                if '"error":"We have a limit on free orders. Please try again in 20 hours."' in response:
                    st.error("❌ وصلت للحد الأقصى للطلبات المجانية. يرجى المحاولة بعد 20 ساعة.")
                else:
                    st.success("☑️ DONE - تم إرسال الطلب بنجاح!")
                    st.balloons()  # مؤثرات إحتفالية بصرياً عند النجاح

            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال: {e}")

st.markdown('</div>', unsafe_allow_html=True)

# حقوق أسفل الصفحة
st.markdown(
    "<div style='text-align: center; color: #64748b; font-size: 12px; margin-top: 20px;'>"
    "Official Rights Reserved © <b>gx1ai</b> | <b>gx2ai</b>"
    "</div>", 
    unsafe_allow_html=True
)
