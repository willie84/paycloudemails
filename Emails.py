import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Paycloud – Sign Up", page_icon="☁️", layout="centered")

WEBHOOK_URL = "https://nairobiaicommunity.app.n8n.cloud/webhook/758e61f2-7f1a-440c-903f-b2e9e606fb0f"

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

    /* ── Page background ─────────────────────── */
    .stApp {
        font-family: 'DM Sans', sans-serif;
        background: linear-gradient(160deg, #0B1120 0%, #0F1A2E 40%, #0B1120 100%);
        min-height: 100vh;
    }

    /* ── Hide defaults ───────────────────────── */
    #MainMenu, header, footer, .stDeployButton { display: none !important; }
    .stTextInput > label { display: none !important; }

    /* ── Inputs ───────────────────────────────── */
    .stTextInput > div > div > input {
        background-color: #0F1A2E !important;
        border: 1.5px solid #1E2D45 !important;
        border-radius: 12px !important;
        padding: 0.8rem 1rem !important;
        font-size: 0.9rem !important;
        color: #E2E8F0 !important;
        font-family: 'DM Sans', sans-serif !important;
        transition: all 0.2s ease !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #14B8A6 !important;
        box-shadow: 0 0 0 2px rgba(20, 184, 166, 0.15) !important;
        background-color: #111D33 !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #475569 !important;
    }

    /* ── Field labels ─────────────────────────── */
    .field-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #94A3B8;
        margin-bottom: 0.3rem;
        letter-spacing: 0.3px;
    }

    /* ── Continue button ──────────────────────── */
    .stButton > button {
        background: linear-gradient(135deg, #14B8A6 0%, #0D9488 100%) !important;
        color: #0B1120 !important;
        border: none !important;
        padding: 0.85rem !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        width: 100% !important;
        margin-top: 0.75rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.25s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 32px rgba(20, 184, 166, 0.3) !important;
        background: linear-gradient(135deg, #2DD4BF 0%, #14B8A6 100%) !important;
    }

    /* ── Card ─────────────────────────────────── */
    .signup-card {
        background: linear-gradient(180deg, #111D33 0%, #0F1A2E 100%);
        border: 1px solid #1E2D45;
        border-radius: 20px;
        padding: 2.5rem 2.25rem 1.5rem;
        max-width: 440px;
        margin: 3rem auto 0 auto;
        box-shadow: 0 4px 40px rgba(0, 0, 0, 0.3), 0 0 80px rgba(20, 184, 166, 0.04);
    }

    /* ── Logo & header ────────────────────────── */
    .brand-logo {
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0.15rem;
    }
    .brand-pay { color: #14B8A6; }
    .brand-cloud { color: #E2E8F0; }
    .brand-sub {
        font-size: 0.85rem;
        color: #64748B;
        margin-bottom: 2rem;
    }

    /* ── Divider ──────────────────────────────── */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #1E2D45, transparent);
        margin: 1.5rem 0;
    }

    /* ── Bottom link ──────────────────────────── */
    .signin-link {
        text-align: center;
        margin: 1.5rem auto 2rem;
        font-size: 0.85rem;
        color: #64748B;
    }
    .signin-link a { color: #14B8A6; text-decoration: none; font-weight: 700; }
    .signin-link a:hover { text-decoration: underline; }

    /* ── Success / Error ──────────────────────── */
    .stSuccess > div {
        background-color: rgba(20, 184, 166, 0.08) !important;
        border-color: rgba(20, 184, 166, 0.3) !important;
        color: #2DD4BF !important;
    }
    .stError > div {
        background-color: rgba(239, 68, 68, 0.08) !important;
        border-color: rgba(239, 68, 68, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

if "result" not in st.session_state:
    st.session_state.result = None

# ── Card Header ──────────────────────────────────────────────
st.markdown("""
<div class="signup-card">
    <div class="brand-logo"><span class="brand-pay">Pay</span><span class="brand-cloud">cloud</span></div>
    <div class="brand-sub">Create your account to get started</div>
</div>
""", unsafe_allow_html=True)

# ── Form ─────────────────────────────────────────────────────
with st.container():
    col = st.columns([0.75, 3.5, 0.75])[1]
    with col:
        with st.form("signup", clear_on_submit=False):
            st.markdown('<p class="field-label">Full Name</p>', unsafe_allow_html=True)
            name = st.text_input("name", placeholder="e.g. Mike Odhiambo", label_visibility="collapsed")

            st.markdown('<p class="field-label">Email Address</p>', unsafe_allow_html=True)
            email = st.text_input("email", placeholder="e.g. mike@example.com", label_visibility="collapsed")

            st.markdown('<p class="field-label">Phone Number</p>', unsafe_allow_html=True)
            phone = st.text_input("phone", placeholder="e.g. +254 712 345 678", label_visibility="collapsed")

            st.markdown('<p class="field-label">Password</p>', unsafe_allow_html=True)
            password = st.text_input("password", type="password", placeholder="Min. 6 characters", label_visibility="collapsed")

            st.markdown("")
            submitted = st.form_submit_button("Continue")

        if submitted:
            errors = []
            if not name.strip(): errors.append("Name is required.")
            if not email.strip() or "@" not in email: errors.append("Valid email is required.")
            if not phone.strip(): errors.append("Phone number is required.")
            if not password or len(password) < 6: errors.append("Password must be at least 6 characters.")

            if errors:
                for e in errors:
                    st.error(e)
            else:
                payload = {
                    "full_name": name.strip(),
                    "email": email.strip(),
                    "phone": phone.strip(),
                    "password": password,
                    "registered_at": datetime.utcnow().isoformat() + "Z",
                }
                try:
                    r = requests.post(WEBHOOK_URL, json=payload, timeout=15)
                    st.session_state.result = ("ok", r.status_code, r.text, payload)
                except Exception as ex:
                    st.session_state.result = ("err", 0, str(ex), payload)

        if st.session_state.result:
            status, code, text, payload = st.session_state.result
            if status == "ok" and 200 <= code < 300:
                st.success(f"✅ Account created! Webhook responded {code}.")
            else:
                st.error(f"⚠️ Failed — {text[:150]}")
            with st.expander("📦 JSON Payload Sent"):
                st.json({**payload, "password": "••••••"})

        st.markdown('<div class="signin-link">Already have an account? <a href="#">Sign In</a></div>', unsafe_allow_html=True)