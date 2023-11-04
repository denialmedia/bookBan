var detailsBox = document.getElementById('details-box');

document.addEventListener('mouseover', function (e) {
    if (e.target.tagName == 'path') {
        var stateName = e.target.dataset.name;
        fetch('http://127.0.0.1:5000/states?q=' + stateName)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.books && data.books.length > 0) {
                    var content = "<div><strong>Books Banned in " + stateName + ":</strong></div>";
                    data.books.forEach(book => {
                        content += "<div>" + book.title + " by " + book.author + "</div>";
                    });
                    detailsBox.innerHTML = content;
                    detailsBox.style.opacity = "100%";
                } else {
                    throw new Error('No banned books found in the selected state');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    else {
        detailsBox.style.opacity = "0%";
    }
});

window.onmousemove = function (e) {
    var x = e.clientX,
        y = e.clientY;
    detailsBox.style.top = (y + 20) + 'px';
    detailsBox.style.left = (x) + 'px';
};