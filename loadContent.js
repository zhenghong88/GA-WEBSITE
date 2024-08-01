function loadServices() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'services.html', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('services-placeholder').innerHTML = xhr.responseText;
        }
    };
    xhr.send();
}
