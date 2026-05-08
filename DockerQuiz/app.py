from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from datetime import datetime, timezone
import os, time, uuid

app = Flask(__name__)
app.secret_key = "docker-quiz-secret-2024-xyz"

# ── MongoDB ─────────────────────────────────────────────────────────────────
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")

def get_db():
    for i in range(5):
        try:
            c = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
            c.admin.command("ping")
            print(f"✅ MongoDB connected")
            return c["dockerquiz"]
        except ServerSelectionTimeoutError:
            print(f"⏳ MongoDB not ready ({i+1}/5)...")
            time.sleep(2)
    print("⚠️  Running without MongoDB")
    return MongoClient(MONGO_URI, serverSelectionTimeoutMS=500)["dockerquiz"]