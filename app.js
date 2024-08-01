function showHome() {
    document.getElementById('home').style.display = 'block';
    document.getElementById('login').style.display = 'none';
    document.getElementById('services').style.display = 'none';
    document.getElementById('dashboard').style.display = 'none';
}

function showLogin() {
    document.getElementById('home').style.display = 'none';
    document.getElementById('login').style.display = 'block';
    document.getElementById('services').style.display = 'none';
    document.getElementById('dashboard').style.display = 'none';
}

function showServices() {
    document.getElementById('home').style.display = 'none';
    document.getElementById('login').style.display = 'none';
    document.getElementById('services').style.display = 'block';
    document.getElementById('dashboard').style.display = 'none';
}

function showDashboard() {
    document.getElementById('home').style.display = 'none';
    document.getElementById('login').style.display = 'none';
    document.getElementById('services').style.display = 'none';
    document.getElementById('dashboard').style.display = 'block';
}
