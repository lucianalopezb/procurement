# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:16:29 2026

@author: O26421
"""

import streamlit as st

st.set_page_config(
    page_title="ProcureTrack",
    page_icon="📊",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.main .block-container{
    max-width:1300px;
    padding-top:1rem;
}

.card{
    border:1px solid #ddd;
    border-radius:10px;
    background:white;
    padding:20px;
    min-height:150px;
}

.card-dark{
    background:black;
    color:white;
    border-radius:10px;
    padding:20px;
    min-height:150px;
}

.activity{
    border:1px solid #ddd;
    border-radius:8px;
    padding:12px;
    margin-bottom:10px;
    background:white;
}

.metric-title{
    color:#777;
    font-size:12px;
}

.insight{
    border:1px solid #ddd;
    border-radius:10px;
    padding:30px;
    text-align:center;
    background:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.title("📊 ProcureTrack")

st.caption("DASHBOARD")

st.header("Welcome back, Jordan")

# ==========================
# KPI
# ==========================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <div class="metric-title">LIVE</div>
        <h1>5</h1>
        <p>In Progress</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <div class="metric-title">URGENT</div>
        <h1>3</h1>
        <p>Pending Approval</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card-dark">
        <h3>➕ New Process</h3>
        <p>Start requisition workflow</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================
# MAIN SECTION
# ==========================

left, right = st.columns([2,1])

with left:

    st.subheader("Recent Activities")

    st.markdown("""
    <div class="activity">
        <b>PO-4921 updated by Finance</b><br>
        14:20 • TECH SOLUTIONS INC.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="activity">
        <b>Requisition approved: Office Supplies</b><br>
        09:15 • JORDAN D.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="activity">
        <b>Vendor RFQ sent: Server Hardware</b><br>
        Yesterday
    </div>
    """, unsafe_allow_html=True)

with right:

    st.subheader("Monthly Throughput")

    st.bar_chart(
        {
            "Spend":[8,12,16,10,20]
        }
    )

    st.metric(
        "Total Spend",
        "$24,500",
        "+12%"
    )

    st.metric(
        "Compliance Score",
        "98%"
    )

# ==========================
# INSIGHT
# ==========================

st.write("")

st.markdown("""
<div class="insight">

<h3>Spend Optimization Insights</h3>

<p>
We've analyzed your recurring vendor costs.
You could save up to 12% by consolidating server maintenance contracts.
</p>

</div>
""", unsafe_allow_html=True)