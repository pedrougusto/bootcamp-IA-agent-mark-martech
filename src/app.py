# -*- coding: utf-8 -*-
import json
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import streamlit as st


# ============================
# CONFIGURAÇÃO
# ============================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

DATA_DIR = Path(r"C:\Users\F39860419825\Downloads")
CSV_PATH = DATA_DIR / "marketing_campaign_english.csv"
JSON_PATH = DATA_DIR / "marketing_campaign_english.json"


# ============================
# CARREGAR DADOS
# ============================
@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    if CSV_PATH.exists():
        df = pd.read_csv(CSV_PATH)
    elif JSON_PATH.exists():
        df = pd.read_json(JSON_PATH)
    else:
        st.error(
            f"❌ Arquivo não encontrado em: {DATA_DIR}\n"
            "Coloque 'marketing_campaign_english.csv' ou '.json' nessa pasta."
        )
        st.stop()

    # Tipagens
    if "post_time" in df.columns:
        df["post_time"] = pd.to_datetime(df["post_time"], errors="coerce")

    for col in ["reach", "likes", "comments", "shares", "conversion", "quality_score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Métricas derivadas educativas
    if all(c in df.columns for c in ["likes", "comments", "shares"]):
        df["engagement"] = df[["likes", "comments", "shares"]].sum(axis=1, skipna=True)

    if "reach" in df.columns:
        df["engagement_rate"] = np.where(df["reach"] > 0, df["engagement"] / df["reach"], np.nan)
        if "conversion" in df.columns:
            df["conversion_rate"] = np.where(df["reach"] > 0, df["conversion"] / df["reach"], np.nan)

    if "caption" in df.columns:
        df["caption_short"] = df["caption"].astype(str).str.slice(0, 120)

    return df


# ============================
# MONTAR CONTEXTO
# ============================
def build_context(df: pd.DataFrame) -> str:
    # Resumo por plataforma
    if "platform" in df.columns:
        cols = [c for c in ["reach", "likes", "comments", "shares", "conversion", "engagement"] if c in df.columns]
        plat_summary = df.groupby("platform")[cols].agg(["sum", "mean"]).round(2)
        plat_summary.columns = ["_".join(col) for col in plat_summary.columns]
        plat_md = plat_summary.reset_index().to_markdown(index=False)
    else:
        plat_md = "_Sem dados de plataforma_"

    # Posts recentes
    recent = df.copy()
    if "post_time" in recent.columns:
        recent = recent.sort_values("post_time", ascending=False)

    cols_recentes = [c for c in ["platform", "post_time", "reach", "likes", "comments",
                                  "shares", "conversion", "engagement_rate",
                                  "conversion_rate", "caption_short"] if c in recent.columns]
    recent_md = recent[cols_recentes].head(8).to_markdown(index=False)

    contexto = f"""
RESUMO POR PLATAFORMA:
{plat_md}

POSTS RECENTES (amostra de 8):
{recent_md}

OBSERVAÇÕES:
- Não há colunas de cliques, custo ou receita no dataset.
- Métricas calculadas:
  - engagement = likes + comments + shares
  - engagement_rate = engagement / reach
  - conversion_rate = conversion / reach
"""
    return contexto


# ============================
# SYSTEM PROMPT
# ============================
SYSTEM_PROMPT = """Você é o Mark, um educador martech amigável, paciente e didático.

OBJETIVO:
Ensinar conceitos de marketing digital, martech e mídia paga de forma simples,
usando os dados das campanhas fornecidos como exemplos práticos.

REGRAS:
- NUNCA gerencie campanhas, configure contas ou faça ações operacionais;
- JAMAIS responda perguntas fora do tema de marketing digital, mídia paga e martech.
  Quando isso acontecer, relembre educadamente seu papel de educador martech;
- Use apenas os dados fornecidos para gerar exemplos personalizados;
- Linguagem simples, leve e acessível, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar o conceito...";
- Sempre pergunte ao final se o usuário entendeu;
- Responda de forma sucinta e direta, em no máximo 3 parágrafos.
"""


# ============================
# CHAMAR OLLAMA
# ============================
def perguntar(msg: str, contexto: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DAS CAMPANHAS:
{contexto}

Pergunta: {msg}
"""
    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt, "stream": False},
            timeout=60,
        )
        r.raise_for_status()
        return r.json().get("response", "").strip()
    except Exception as e:
        return f"❌ Erro ao consultar o modelo: {e}"


# ============================
# INTERFACE
# ============================
def main():
    st.set_page_config(page_title="🎯 Mark — Educador Martech", page_icon="🎯")
    st.title("🎯 Mark — Educador Martech")
    st.caption("Agente educativo para explicar Ads, métricas e martech usando seus dados de campanha.")

    df = load_dataset()
    contexto = build_context(df)

    with st.expander("👀 Ver contexto enviado ao modelo"):
        st.markdown(contexto)

    if "chat" not in st.session_state:
        st.session_state.chat = []

    for role, text in st.session_state.chat:
        st.chat_message(role).write(text)

    if pergunta := st.chat_input("Pergunte sobre métricas, funil, criativos, segmentação..."):
        st.session_state.chat.append(("user", pergunta))
        st.chat_message("user").write(pergunta)

        with st.spinner("Mark está pensando..."):
            resposta = perguntar(pergunta, contexto)

        st.session_state.chat.append(("assistant", resposta))
        st.chat_message("assistant").write(resposta)

    st.markdown(
        "<hr/><small>⚠️ Mark é um agente <b>educativo</b>. "
        "Não realiza ações operacionais nem prevê resultados.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()