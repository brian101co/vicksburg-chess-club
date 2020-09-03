document.addEventListener('DOMContentLoaded', function () {
    var request = new XMLHttpRequest();
    request.open('GET', 'https://chesspuzzle.net/Daily/Api', true);
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            var result = JSON.parse(request.responseText);
            document.getElementById("puzzleText").textContent = result.Text;
            document.getElementById("puzzleLink").href = result.Link;
            document.getElementById("puzzleImage").src = result.Image;
        }
    };
    request.send();

    document.querySelector('.join-us').addEventListener('click', function (e) {
        e.preventDefault();
        const href = this.getAttribute("href");
        const offsetTop = document.querySelector(href).offsetTop;

        scroll({
            top: offsetTop,
            behavior: 'smooth'
        })
    });
});