@echo off
REM Script untuk Start N8N Chatbot Services
REM Jalankan Command Prompt as Administrator

setlocal enabledelayedexpansion

REM Ubah ke directory project
cd /d "%~dp0"

REM Check jika Docker sudah berjalan
docker ps >nul 2>&1
if errorlevel 1 (
    echo.
    echo ============================================
    echo ERROR: Docker Desktop tidak sedang berjalan!
    echo ============================================
    echo.
    echo Silakan:
    echo 1. Buka Docker Desktop application
    echo 2. Tunggu sampai Docker fully loaded
    echo 3. Jalankan script ini lagi
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Starting N8N Chatbot Services...
echo ============================================
echo.

REM Start services
docker-compose up -d

if errorlevel 1 (
    echo.
    echo ERROR: Gagal start services!
    echo.
    pause
    exit /b 1
)

echo.
echo ✓ Services started successfully!
echo.
echo Akses aplikasi:
echo   - N8N Dashboard: http://localhost:5678
echo   - Chatbot Website: http://localhost
echo.
echo Username: admin
echo Password: telkom@2026!secure
echo.
echo Untuk melihat logs: docker-compose logs -f
echo Untuk stop services: docker-compose down
echo.

pause