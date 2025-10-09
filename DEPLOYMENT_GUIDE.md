# 🚀 Deployment Guide - VSB Engineering College Feedback System

This guide provides step-by-step instructions to deploy the Faculty Feedback System on **Render.com** with **Supabase** as the database.

---

## 📋 Prerequisites

Before starting the deployment, ensure you have:

1. **GitHub Account** - To host your code repository
2. **Render Account** - Sign up at [render.com](https://render.com) (free tier available)
3. **Supabase Account** - Sign up at [supabase.com](https://supabase.com) (free tier available)
4. **Git installed** on your local machine

---

## 🗄️ Part 1: Setting Up Supabase Database

### Step 1: Create a Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign in
2. Click **"New Project"**
3. Fill in the project details:
   - **Name**: `vsbec-feedback-system`
   - **Database Password**: Create a strong password (save this!)
   - **Region**: Choose closest to your users
   - **Plan**: Free tier is sufficient
4. Click **"Create new project"** and wait for setup (2-3 minutes)

### Step 2: Create Database Tables

1. In your Supabase project, go to **SQL Editor** (left sidebar)
2. Click **"New Query"**
3. Copy and paste this SQL schema:

```sql
-- Create departments table
CREATE TABLE departments (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create semesters table
CREATE TABLE semesters (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create staff table
CREATE TABLE staff (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create subjects table
CREATE TABLE subjects (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create students table
CREATE TABLE students (
    id BIGSERIAL PRIMARY KEY,
    registerno TEXT NOT NULL UNIQUE,
    department TEXT NOT NULL,
    semester TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create admin_mappings table
CREATE TABLE admin_mappings (
    id BIGSERIAL PRIMARY KEY,
    department TEXT NOT NULL,
    semester TEXT NOT NULL,
    staff TEXT NOT NULL,
    subject TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create ratings table
CREATE TABLE ratings (
    id BIGSERIAL PRIMARY KEY,
    registerno TEXT NOT NULL,
    department TEXT NOT NULL,
    semester TEXT NOT NULL,
    staff TEXT NOT NULL,
    subject TEXT NOT NULL,
    q1 REAL NOT NULL,
    q2 REAL NOT NULL,
    q3 REAL NOT NULL,
    q4 REAL NOT NULL,
    q5 REAL NOT NULL,
    q6 REAL NOT NULL,
    q7 REAL NOT NULL,
    q8 REAL NOT NULL,
    q9 REAL NOT NULL,
    q10 REAL NOT NULL,
    average REAL NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create submitted_feedback table
CREATE TABLE submitted_feedback (
    id BIGSERIAL PRIMARY KEY,
    registerno TEXT NOT NULL UNIQUE,
    submission_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX idx_students_registerno ON students(registerno);
CREATE INDEX idx_students_dept_sem ON students(department, semester);
CREATE INDEX idx_mappings_dept_sem ON admin_mappings(department, semester);
CREATE INDEX idx_ratings_staff ON ratings(staff);
CREATE INDEX idx_ratings_dept_sem ON ratings(department, semester);
CREATE INDEX idx_submitted_registerno ON submitted_feedback(registerno);
```

4. Click **"Run"** to execute the SQL
5. Verify all tables are created by checking **"Table Editor"** (left sidebar)

### Step 3: Get Supabase Connection Details

1. In Supabase, go to **Project Settings** (gear icon, bottom left)
2. Click **"API"** in the settings menu
3. Copy these values (you'll need them later):
   - **Project URL** (looks like: `https://xxxxx.supabase.co`)
   - **Project API Key** (anon/public key)

### Step 4: Insert Initial Data (Optional)

You can add some initial departments and semesters:

```sql
-- Insert sample departments
INSERT INTO departments (name) VALUES 
('Computer Science - A'),
('Computer Science - B'),
('Electrical Engineering'),
('Mechanical Engineering'),
('Civil Engineering');

-- Insert sample semesters
INSERT INTO semesters (name) VALUES 
('1'), ('2'), ('3'), ('4'), ('5'), ('6'), ('7'), ('8');
```

---

## 🐙 Part 2: Preparing Your GitHub Repository

### Step 1: Initialize Git Repository (if not done)

```bash
cd C:\Shyamnath\Feedback-System
git init
git add .
git commit -m "Initial commit for deployment"
```

### Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click **"+"** (top right) → **"New repository"**
3. Name it: `vsbec-feedback-system`
4. Set to **Public** or **Private** (your choice)
5. **DO NOT** initialize with README
6. Click **"Create repository"**

### Step 3: Push Code to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/vsbec-feedback-system.git
git branch -M main
git push -u origin main
```

**⚠️ IMPORTANT**: Make sure `.env` file is in `.gitignore` so secrets aren't pushed!

---

## 🚀 Part 3: Deploying to Render

### Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with GitHub (recommended) or email
4. Verify your email if required

### Step 2: Create a New Web Service

1. On Render Dashboard, click **"New +"** (top right)
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - Click **"Connect account"** if first time
   - Authorize Render to access GitHub
   - Select the repository: `vsbec-feedback-system`

### Step 3: Configure Web Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `vsbec-feedback-system` (or any name you prefer)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app:asgi_app --host 0.0.0.0 --port $PORT`

**Plan:**
- Select **"Free"** tier (or paid if you need better performance)

### Step 4: Configure Environment Variables

Scroll down to **"Environment Variables"** section and add the following:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `SUPABASE_URL` | `https://xxxxx.supabase.co` | From Supabase Project API settings |
| `SUPABASE_KEY` | `your-anon-key` | From Supabase Project API settings |
| `SECRET_KEY` | Generate random string | Used for Flask sessions |
| `FLASK_SECRET_KEY` | Generate random string | Same as above or different |
| `ADMIN_PASSWORD` | `your-secure-password` | Admin login password |
| `HOD_USERNAME` | `hod` | HOD login username |
| `HOD_PASSWORD` | `your-hod-password` | HOD login password |
| `ENCRYPTION_SECRET_KEY` | Generate random string | For data encryption |

**How to generate random keys** (use Python):
```python
import secrets
print(secrets.token_hex(32))
```

Or use an online generator: [randomkeygen.com](https://randomkeygen.com)

### Step 5: Deploy!

1. Click **"Create Web Service"** at the bottom
2. Render will start building and deploying your app
3. Watch the logs for any errors
4. Build should complete in 2-5 minutes
5. Once deployed, you'll see a URL like: `https://vsbec-feedback-system.onrender.com`

---

## ✅ Part 4: Post-Deployment Verification

### Step 1: Test the Application

1. Open your Render URL: `https://your-app.onrender.com`
2. You should see the student login page
3. Test admin login: `https://your-app.onrender.com/admin_login`
   - Use the `ADMIN_PASSWORD` you set in environment variables
4. Test HOD login: `https://your-app.onrender.com/hod_login`
   - Use `HOD_USERNAME` and `HOD_PASSWORD` you set

### Step 2: Add Initial Students

1. Login as admin
2. Go to **"Student Management"**
3. Upload an Excel file with student data (format: registerno, department, semester)
4. Or manually add students via Supabase Table Editor

### Step 3: Add Staff-Subject Mappings

1. Login as admin
2. Go to **"Staff-Subject Mapping"**
3. Add staff and subjects
4. Create mappings for each department/semester

---

## 🔧 Troubleshooting

### Issue 1: Build Failed

**Error**: `Failed to install requirements`

**Solution**:
- Check `requirements.txt` is present in root directory
- Ensure Python version is 3.11.0 or compatible
- Check Render logs for specific error messages

### Issue 2: Application Crash on Start

**Error**: `Web service exited with code 1`

**Solution**:
- Verify all environment variables are set correctly
- Check Supabase URL and KEY are correct
- Review Render logs for Python errors
- Ensure `uvicorn` is in requirements.txt

### Issue 3: Database Connection Error

**Error**: `Failed to connect to Supabase`

**Solution**:
- Verify `SUPABASE_URL` and `SUPABASE_KEY` are correct
- Check Supabase project is active (not paused)
- Ensure tables are created in Supabase
- Check Supabase service status

### Issue 4: Can't Login

**Error**: Incorrect password even with correct credentials

**Solution**:
- Verify environment variables are set in Render
- Check for extra spaces in password values
- Re-deploy after updating env vars

### Issue 5: Free Tier Inactivity

**Note**: Render free tier services spin down after 15 minutes of inactivity

**Solution**:
- First request after inactivity may take 30-60 seconds
- Consider upgrading to paid tier for always-on service
- Use a uptime monitor service to keep it alive (e.g., UptimeRobot)

---

## 📊 Monitoring and Logs

### Viewing Logs

1. Go to Render Dashboard
2. Click on your service: `vsbec-feedback-system`
3. Click **"Logs"** tab
4. View real-time application logs
5. Use search to filter errors or specific events

### Metrics

1. In service dashboard, click **"Metrics"** tab
2. View CPU, Memory, Bandwidth usage
3. Monitor response times
4. Check for errors and crashes

---

## 🔄 Updating Your Application

### Method 1: Push to GitHub (Automatic)

```bash
# Make changes to your code
git add .
git commit -m "Update feature"
git push origin main
```

Render will automatically detect the push and redeploy!

### Method 2: Manual Deploy

1. Go to Render Dashboard
2. Click your service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**

---

## 🔒 Security Best Practices

### 1. Secure Environment Variables
- Never commit `.env` file to GitHub
- Use strong, unique passwords
- Rotate secrets periodically

### 2. Enable HTTPS
- Render provides automatic HTTPS (already enabled!)
- Always use `https://` URLs

### 3. Database Security
- Keep Supabase API keys secret
- Use Row Level Security (RLS) in Supabase for additional protection
- Regularly backup database

### 4. Rate Limiting (Optional)
- Consider adding Flask-Limiter for protection against abuse
- Configure in `app.py`:

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

---

## 💰 Cost Optimization

### Free Tier Limits

**Render Free Tier:**
- 750 hours/month (enough for 1 app running 24/7)
- 512 MB RAM
- Spins down after 15 min inactivity
- Auto-deploys from GitHub

**Supabase Free Tier:**
- 500 MB database storage
- 2 GB file storage
- 2 GB bandwidth
- Up to 50 MB file uploads
- Unlimited API requests

### When to Upgrade

Consider paid plans when:
- Need always-on service (no spin-down)
- Database grows beyond 500 MB
- Need more than 512 MB RAM
- High traffic requirements
- Need custom domain

---

## 🌐 Custom Domain Setup (Optional)

### Step 1: Add Custom Domain in Render

1. Go to your service in Render
2. Click **"Settings"** tab
3. Scroll to **"Custom Domains"**
4. Click **"Add Custom Domain"**
5. Enter your domain: `feedback.vsbec.edu.in`

### Step 2: Configure DNS

In your domain registrar (e.g., GoDaddy, Namecheap):

1. Add a **CNAME record**:
   - **Name**: `feedback` (or `@` for root domain)
   - **Value**: Your Render URL (e.g., `vsbec-feedback-system.onrender.com`)
   - **TTL**: 3600 or Auto

2. Wait for DNS propagation (5 minutes to 48 hours)

3. Render will automatically provision SSL certificate

---

## 📞 Support and Resources

### Official Documentation
- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Supabase Docs**: [supabase.com/docs](https://supabase.com/docs)
- **Flask Docs**: [flask.palletsprojects.com](https://flask.palletsprojects.com)

### Community Support
- Render Community: [community.render.com](https://community.render.com)
- Supabase Discord: [discord.supabase.com](https://discord.supabase.com)

### Application Support
- GitHub Issues: Open an issue in your repository
- Contact: [Your support email]

---

## 🎉 Congratulations!

Your VSB Engineering College Faculty Feedback System is now live and accessible globally!

**Next Steps:**
1. Share the URL with students and staff
2. Monitor application logs for issues
3. Regularly backup database
4. Collect user feedback for improvements

---

**Created and Maintained by GenrecAI**  
Website: [Genrec.AI](https://revolvo-ai.netlify.app)
