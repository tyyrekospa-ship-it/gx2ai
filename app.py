import streamlit as st
import time
import datetime

# إعدادات الصفحة الهيكلية
st.set_page_config(
    page_title="زيادة مشاهدات انستغرام - gx1ai & gx2ai",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم الأنماط والـ CSS الفاخر الملكي بدون حقوق جيتها في الأعلى
st.markdown("""
<style>
    /* إخفاء عناصر Streamlit الافتراضية وشريط GitHub / Header بالكامل */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppHeader {display: none !important;}
    div[data-testid="stToolbar"] {display: none !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    div[data-testid="stStatusWidget"] {display: none !important;}
    
    /* خلفية متدرجة ملكية مظلمة */
    .stApp {
        background: linear-gradient(135deg, #090e17 0%, #0d1b2a 50%, #1b263b 100%);
        color: #e0e1dd;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* الحاوية الرئيسية بطاقة زجاجية معتمة */
    .main-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 180, 216, 0.25);
        border-radius: 24px;
        padding: 30px 25px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 180, 216, 0.15);
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* صورة القناة الدائرية مع توهج ملكي */
    .channel-logo-img {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #00b4d8;
        box-shadow: 0 0 25px rgba(0, 180, 216, 0.6), 0 0 10px rgba(0, 119, 182, 0.8);
        transition: transform 0.3s ease;
        margin-bottom: 15px;
    }
    .channel-logo-img:hover {
        transform: scale(1.06);
    }
    
    /* العناوين والتصميم الفاخر */
    .main-title {
        background: linear-gradient(90deg, #90e0ef, #00b4d8, #48cae4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 26px;
        margin-bottom: 8px;
        text-shadow: 0 20px 30px rgba(0, 180, 216, 0.2);
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 20px;
    }
    
    /* شارات وقنوات التليجرام */
    .telegram-badge-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    
    .telegram-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, #0088cc 0%, #005f73 100%);
        color: #ffffff !important;
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 14px;
        box-shadow: 0 4px 15px rgba(0, 136, 204, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .telegram-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 136, 204, 0.7);
        background: linear-gradient(135deg, #00a8e8 0%, #0077b6 100%);
    }
    
    /* تحسين تصميم مدخلات البيانات */
    div[data-baseweb="input"] {
        background-color: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid rgba(0, 180, 216, 0.4) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }
    
    div[data-baseweb="input"]:focus-within {
        border-color: #00b4d8 !important;
        box-shadow: 0 0 12px rgba(0, 180, 216, 0.5) !important;
    }
    
    /* أزرار Streamlit */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #0077b6 0%, #00b4d8 50%, #03045e 100%);
        background-size: 200% auto;
        color: white;
        font-weight: 700;
        font-size: 16px;
        border: none;
        border-radius: 14px;
        padding: 14px 20px;
        box-shadow: 0 6px 20px rgba(0, 180, 216, 0.4);
        transition: all 0.4s ease;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        background-position: right center;
        box-shadow: 0 8px 30px rgba(0, 180, 216, 0.7);
        transform: translateY(-2px);
    }
    
    /* شريط التقدم الفاخر */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #0077b6, #00b4d8, #90e0ef);
        border-radius: 10px;
    }
    
    /* صندوق الإشعارات الممتاز */
    .custom-success-box {
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 16px;
        padding: 20px;
        color: #34d399;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.1);
    }
    
    .footer-rights {
        text-align: center;
        margin-top: 30px;
        padding-top: 15px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #64748b;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر والواجهة الفاخرة المخصصة
st.markdown("""
<div class="main-card">
    <img src="https://files.catbox.moe/868tll.jpg" class="channel-logo-img" alt="Channel Logo">
    <div class="main-title">🚀 أداة زيادة مشاهدات ستوري وريلز انستغرام</div>
    <div class="subtitle">النظام التلقائي الأسرع والآمن لإرسال المشاهدات الحقيقية</div>
    
    <div class="telegram-badge-container">
        <a href="https://t.me/gx1ai" target="_blank" class="telegram-btn">
            ✈️ قناة gx1ai
        </a>
        <a href="https://t.me/gx2ai" target="_blank" class="telegram-btn">
            ✈️ قناة gx2ai
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# استمارة إدخال البيانات
with st.container():
    st.markdown("### 📥 بيانات الطلب")
    
    username = st.text_input("اسم المستخدم (Username) أو رابط الحساب / المقطع:", placeholder="مثال: username أو https://instagram.com/...")
    
    service_type = st.selectbox(
        "اختر نوع الخدمة المطلوبة:",
        ["مشاهدات ستوري (Instagram Story Views)", "مشاهدات ريلز (Instagram Reels Views)", "مشاهدات فيديو عامة"]
    )
    
    views_count = st.slider("حدد عدد المشاهدات المطلوبة:", min_value=1000, max_value=50000, value=10000, step=1000)
    
    st.write("")
    
    start_btn = st.button("⚡ بدء إرسال المشاهدات الآن")

# تنفيذ عملية الإرسال المحاكية بكامل المنطق الأصلي
if start_btn:
    if not username:
        st.error("⚠️ يرجى إدخال اسم المستخدم أو الرابط أولاً!")
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            "🔍 جاري الاتصال بالسيرفرات والتحقق من الحساب...",
            "⚙️ جاري تجهيز حزمة المشاهدات المطلوب إرسالها...",
            "🚀 جاري ضخ المشاهدات تدريجياً عبر البروكسيات...",
            "✨ جاري إتمام العملية وتثبيت المشاهدات..."
        ]
        
        for i in range(100):
            time.sleep(0.04)
            progress_bar.progress(i + 1)
            if i == 10:
                status_text.info(steps[0])
            elif i == 35:
                status_text.info(steps[1])
            elif i == 65:
                status_text.info(steps[2])
            elif i == 90:
                status_text.info(steps[3])
                
        status_text.empty()
        
        st.markdown(f"""
        <div class="custom-success-box">
            <h3 style="margin:0 0 10px 0; color:#34d399;">🎉 تم إرسال الطلب بنجاح!</h3>
            <p style="margin:5px 0;"><b>الحساب / الرابط:</b> {username}</p>
            <p style="margin:5px 0;"><b>نوع الخدمة:</b> {service_type}</p>
            <p style="margin:5px 0;"><b>الكمية المضافة:</b> +{views_count:,} مشاهدة</p>
            <p style="margin:10px 0 0 0; font-size:12px; opacity:0.8;">ستبدأ المشاهدات بالظهور في حسابك خلال بضع دقائق.</p>
        </div>
        """, unsafe_allow_html=True)

# الفوتر وحقوق الملكية
st.markdown("""
<div class="footer-rights">
    جميع الحقوق محفوظة © 2026 | تطوير بدعم من قنوات التليجرام 
    <a href="https://t.me/gx1ai" target="_blank" style="color:#00b4d8; text-decoration:none; font-weight:bold;">gx1ai</a> & 
    <a href="https://t.me/gx2ai" target="_blank" style="color:#00b4d8; text-decoration:none; font-weight:bold;">gx2ai</a>
</div>
""", unsafe_allow_html=True)
