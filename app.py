import streamlit as st
import asyncio
import aiohttp
import re
import random
import uuid
import os
import sys

# محاولة استيراد SignerPy أو العمل بالدالة البديلة تلقائياً
try:
    import SignerPy
    HAS_SIGNER = True
except ImportError:
    HAS_SIGNER = False

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="gx1ai & gx2ai | TikTok Views Booster",
    page_icon="💀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تصميم الواجهة وإخفاء شريط Streamlit/GitHub
st.markdown("""
<style>
    #MainMenu, footer, header, .stAppHeader, div[data-testid="stToolbar"], div[data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    .stApp {
        background: radial-gradient(circle at center, #0f051d 0%, #05010a 70%, #000000 100%);
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .dark-scary-card {
        background: rgba(10, 5, 20, 0.9);
        border: 2px solid #8a00c4;
        border-radius: 25px;
        padding: 30px 20px;
        box-shadow: 0 0 35px rgba(138, 0, 196, 0.5), inset 0 0 15px rgba(255, 0, 85, 0.3);
        text-align: center;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
    }

    .profile-img-frame {
        width: 125px;
        height: 125px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #ff0055;
        box-shadow: 0 0 25px #ff0055, 0 0 50px #8a00c4;
        margin-bottom: 15px;
        animation: scaryGlow 3s infinite alternate;
    }

    @keyframes scaryGlow {
        0% { box-shadow: 0 0 15px #ff0055, 0 0 30px #8a00c4; transform: scale(1); }
        100% { box-shadow: 0 0 30px #00f0ff, 0 0 60px #ff0055; transform: scale(1.03); }
    }

    .main-scary-title {
        font-size: 26px;
        font-weight: 900;
        background: linear-gradient(90deg, #ff0055, #00f0ff, #ff0055);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255,0,85,0.5);
        margin-bottom: 15px;
        letter-spacing: 1px;
    }

    .tg-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 15px;
        flex-wrap: wrap;
    }

    .neon-btn {
        display: inline-block;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 15px;
        color: #fff !important;
        text-decoration: none !important;
        border-radius: 50px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .btn-gx1 {
        background: linear-gradient(45deg, #ff0055, #8a00c4);
        box-shadow: 0 0 15px #ff0055;
    }

    .btn-gx2 {
        background: linear-gradient(45deg, #00f0ff, #0044ff);
        box-shadow: 0 0 15px #00f0ff;
    }

    div[data-baseweb="input"] {
        background-color: rgba(15, 5, 25, 0.95) !important;
        border: 1px solid #8a00c4 !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ff0055 0%, #8a00c4 50%, #00f0ff 100%);
        background-size: 200% auto;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        border-radius: 12px;
        padding: 14px;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.5);
    }

    .counter-display {
        background: rgba(0, 0, 0, 0.8);
        border: 1px solid #00f0ff;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
    }

    .counter-number {
        font-size: 42px;
        font-weight: 900;
        color: #00f0ff;
        text-shadow: 0 0 15px #00f0ff, 0 0 30px #00f0ff;
    }
</style>
""", unsafe_allow_html=True)

# 3. العرض العلوي
st.markdown("""
<div class="dark-scary-card">
    <img src="https://files.catbox.moe/868tll.jpg" class="profile-img-frame">
    <div class="main-scary-title">🔥 أداة زيادة مشاهدات تيك توك الفائقة 🔥</div>
    <div style="color: #b8b8b8; font-size: 14px; margin-bottom: 10px;">نظام الرشق التلقائي السريع والمعزز</div>
    <div class="tg-container">
        <a href="https://t.me/gx1ai" target="_blank" class="neon-btn btn-gx1">⚡ قناة gx1ai</a>
        <a href="https://t.me/gx2ai" target="_blank" class="neon-btn btn-gx2">🚀 قناة gx2ai</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. المنطق البرمجي
VIDEO_ID_PATTERN = re.compile(r'/video/(\d+)')

class SayidBooster:
    def __init__(self, url, threads=200):
        self.url = url
        self.threads = threads
        self.API = "https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/"
        self.counter = 0
        self.lock = asyncio.Lock()
        self.session = None
        self.video_id = None
        
        self.static_headers = {
            'User-Agent': "com.zhiliaoapp.musically.go",
            'Accept-Encoding': "gzip",
            'rpc-persist-pyxis-policy-v-tnc': "1",
            'x-ss-stub': "80867B02FBD2ECA6BA9AA62239D3B1EB",
            'x-tt-req-timeout': "90000",
            'sdk-version': "2",
            'x-tt-token': "039d6f2aba58cb9dbd28dc1e9db2ff355d0291bae03464a6c3fb0cc8df9871bf4f74a8e386c55b5d805c496a78fcf838ff309b97885ecb4cda244e6997aee72f64ba2b61de022e0e9df57f2298a47798ed0b6c9f4d495c56793fbb658044dcc3e3008--0a4e0a201266a032bd35419f3b5dde919e4745ca32b784b956a1d2ee19e5ec79d874f2281220eae667e86a053d169b45d4a44a6dd914e846c78bff2f80647b899c3a1902284d1801220674696b746f6b-3.0.0",
            'passport-sdk-version': "30990",
            'x-tt-ultra-lite': "1",
            'x-vc-bdturing-sdk-version': "2.3.2.i18n",
            'x-tt-store-region': "iq",
            'x-tt-store-region-src': "uid",
            'x-ladon': "abrYTrssSD1CwVlPF9RDXSuywcMgvDEm9png1gwUFF22S8v9",
            'x-khronos': "1750173135",
            'x-argus': "tQMfoeL2aSF5jwjvAyYZVA9PuLLbYe73yEdyRXTe2Vd860DTV5P4vgO0DJN0qp/Ys+Slb2Bb79+s++ppBCSZTT5mzL6KB/irb13VhiIpNf7dz/AQUXdtR5yTTKEIivnl9q+jDOJMkSDE9D2+4zW/PrOKqhprYwjUD1NetyG1Oam38wp/fJekNB75vLYTc9Xj4uHiJVuGuCKoUCM2YLi0sBp2mVGfMkPpgdn5f8Mjmp7b0X9/Q7kg2aifITbReckgvjcjZ/8orHwdGi5qm4jLDJoV",
            'x-gorgon': "840440f41080c1f89eacdece36d9481df459ac26a0f9f1fd5beb",
            'Cookie': "store-idc=alisg; store-country-code=iq; install_id=7516928038623151879; ttreq=1$5f3bc0fcb73296e39d74f6d161b1e2dfed2914e2; passport_csrf_token=0f2d2a82bd6027000f1cd87356a7c725; passport_csrf_token_default=0f2d2a82bd6027000f1cd87356a7c725; tt-target-idc=useast1a; msToken=QLxCStq-Kg2xmFBlVJujXSieGFaVkNNNlcpITZ64BrAHOpbQkFDLtCsUgkOeIvzAzVInDfq9kGli2Ez6hDV8fDvNPyVRPDn1ZBjswjNLB2w=; d_ticket=b5721737f5130c31a6838273ef8cce2bd033b; odin_tt=e5f3b0179d3ce2bf82dd4cc6f3390f77ccbad0b515cba639de5a239e6dcb9a73c2127a337a92a7aa97dba800b0ec2e428c03e1721d83e6c6a215ea2a1f9b685adb3489fac33fca47eee90e13b5aaa583; cmpl_token=AgQQAPPdF-ROXbF9U18up508_eMmwUgJv4csYN6Peg; sid_guard=9d6f2aba58cb9dbd28dc1e9db2ff355d%7C1750173049%7C15552000%7CSun%2C+14-Dec-2025+15%3A10%3A49+GMT; uid_tt=35618c1bd532338f95223c90d9e0761f882243bf9f8e6c3adac8e381d0de26a4; uid_tt_ss=35618c1bd532338f95223c90d9e0761f882243bf9f8e6c3adac8e381d0de26a4; sid_tt=9d6f2aba58cb9dbd28dc1e9db2ff355d; sessionid=ba9145164e3e0cf2ade170251307a327; sessionid_ss=9d6f2aba58cb9dbd28dc1e9db2ff355d; store-country-code-src=uid; tt-target-idc-sign=Vx96gYES8RTFDCY_PFVspKKHrqjQcO0VFxyGCL0tyyof1Gr54t8ljI3lt3Rm7jBD1DHO-vDAhN5HlanTZ0iGjnzaOPjqIGaQWSbjWaxnI92Y8WEsIuH10dKOVKlY5T8QpvH1_agORf6_CQoXrzJMg_hgKnWbTayMEr29jVGxnoEhJqHRItGbJ2oSpvgHH77jvQjIrgmRFF142K5MSJn7P-IUKVfhbF36EeJq1QzOOI0Ewr3wkCeNCH2juQUhnBiJA3m_U4OZD1EZrFWVUB8vC8yRzK63bgEKYwpkNU5zuKjV5DQwhWDh2iUL9-VLmmG-PJy4pEbtkIfsvMzuSCW3baFdQqgibSZkiNd59CNx0gf8hsX8gkaxxVv0_2E1ITwSsMI74t45MJX6k9YeBSWZU2NzRLShPCLSrD-KyEn0wld-hwaD0on1jb61XqRMPSi4G2nkIrC8oS0paVmf0ZhClcB41fhS0mUp8uDnY-3jKBx-7dUsu5S_2jEC4qXINWmw;store-country-sign=MEIEDNmFtblKy5x9QxT77AQgUNh27q2sLl-QbOIBLgB4xUEbZ2oboEtrtOqmBLYhhOwEEKF-pTVSphnhIiWj_Jt12X0"
        }
        
        self.base_payload = {
            'pre_item_playtime': "",
            'first_install_time': "1737204216",
            'is_ad': "false",
            'follow_status': "0",
            'sync_origin': "false",
            'follower_status': "0",
            'action_time': "1750173135",
            'tab_type': "3",
            'pre_hot_sentence': "",
            'play_delta': "1",
            'request_id': "",
            'aweme_type': "0",
            'order': "",
            'pre_item_id': ""
        }

    def gen_dynamic_params(self):
        params_dict = {
            "manifest_version_code": "350302",
            "_rticket": str(int(random.random() * 10**16)),
            "app_language": "en",
            "app_type": "normal",
            "iid": str(random.randint(7000000000000000000, 9000000000000000000)),
            "channel": "googleplay",
            "device_type": "RMX3941",
            "language": "en",
            "host_abi": "arm64-v8a",
            "locale": "en",
            "resolution": "1080*2290",
            "openudid": str(uuid.uuid4().hex[:16]),
            "update_version_code": "350302",
            "ac2": "wifi5g",
            "cdid": str(uuid.uuid4()),
            "sys_region": "US",
            "os_api": "34",
            "timezone_name": "America/New_York",
            "dpi": "480",
            "carrier_region": "US",
            "ac": "wifi",
            "device_id": str(random.randint(7000000000000000000, 9000000000000000000)),
            "os_version": "12",
            "timezone_offset": "10800",
            "version_code": "350302",
            "app_name": "musically_go",
            "ab_version": "35.3.2",
            "version_name": "35.3.2",
            "device_brand": "realme",
            "op_region": "US",
            "ssmix": "a",
            "device_platform": "android",
            "build_number": "35.3.2",
            "region": "US",
            "aid": "1340",
            "ts": str(int(random.random() * 10**10))
        }
        if HAS_SIGNER:
            return SignerPy.get(params=params_dict)
        return params_dict

    async def worker(self):
        session = self.session
        video_id = self.video_id
        base_payload = self.base_payload.copy()
        base_payload['item_id'] = video_id
        api_url = self.API
        
        while st.session_state.get('is_running', False):
            try:
                payload = base_payload.copy()
                async with session.post(
                    api_url, 
                    data=payload, 
                    params=self.gen_dynamic_params()
                ) as response:
                    if response.status == 200:
                        json_data = await response.json()
                        if json_data.get('status_code') == 0:
                            async with self.lock:
                                self.counter += 1
                                st.session_state['total_sent'] = self.counter
                    elif response.status in [400, 403, 429]:
                        await asyncio.sleep(0.1)
            except Exception:
                await asyncio.sleep(0.01)
                continue

    async def start(self, status_box, counter_box):
        async with aiohttp.ClientSession() as temp_session:
            try:
                # تتبع إعادة التوجيه للحصول على الـ Video ID حتى لو كان الرابط مختصر
                async with temp_session.get(self.url, allow_redirects=True, timeout=10) as response:
                    full_url = str(response.url)
                
                match = VIDEO_ID_PATTERN.search(full_url)
                if not match:
                    # محاولة ثانية باستخراج الأرقام إذا كان الرابط مكتمل
                    match_alt = re.search(r'(\d{18,19})', full_url)
                    if match_alt:
                        self.video_id = match_alt.group(1)
                    else:
                        status_box.error("❌ لم يتم العثور على ID الفيديو. تأكد من صحة الرابط!")
                        st.session_state['is_running'] = False
                        return
                else:
                    self.video_id = match.group(1)

                status_box.success(f"✅ تم استخراج ID الفيديو: {self.video_id}")
                
                connector = aiohttp.TCPConnector(
                    limit=0,
                    limit_per_host=0,
                    ttl_dns_cache=300,
                    enable_cleanup_closed=True,
                    force_close=False
                )
                
                timeout = aiohttp.ClientTimeout(total=10, connect=5, sock_read=5)
                
                async with aiohttp.ClientSession(
                    connector=connector,
                    timeout=timeout,
                    headers=self.static_headers
                ) as session:
                    self.session = session
                    tasks = [asyncio.create_task(self.worker()) for _ in range(self.threads)]
                    
                    while st.session_state.get('is_running', False):
                        await asyncio.sleep(0.3)
                        counter_box.markdown(f"""
                        <div class="counter-display">
                            <div style="color: #ff0055; font-size: 16px; font-weight: bold; margin-bottom: 5px;">⚡ المرسل حالياً ⚡</div>
                            <div class="counter-number">{st.session_state.get('total_sent', 0):,}</div>
                        </div>
                        """, unsafe_allow_html=True)

            except Exception as e:
                status_box.error(f"حدث خطأ أثناء الاتصال: {e}")
                st.session_state['is_running'] = False

# 5. عناصر التحكم بالواجهة
video_url = st.text_input("رابط الفيديو (TikTok URL):", value=st.session_state.get('url_val', ''), placeholder="https://vt.tiktok.com/...")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 بدء إرسال المشاهدات"):
        if video_url.strip():
            st.session_state['is_running'] = True
            st.session_state['total_sent'] = 0
            st.session_state['url_val'] = video_url.strip()
        else:
            st.warning("الرجاء وضع رابط الفيديو أولاً!")

with col2:
    if st.button("🛑 إيقاف الإرسال"):
        st.session_state['is_running'] = False

status_spot = st.empty()
counter_spot = st.empty()

# تشغيل عملية الإرسال عند تفعيل الزر
if st.session_state.get('is_running', False):
    booster = SayidBooster(url=st.session_state.get('url_val', ''))
    try:
        asyncio.run(booster.start(status_spot, counter_spot))
    except Exception:
        pass

