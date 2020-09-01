document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.body br').forEach(function (elem) {
        elem.remove();
    });
});