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
});