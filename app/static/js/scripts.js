const navToggle = document.querySelector('#navToggle');
const nav = document.querySelector('.nav-links');
const buttons = document.querySelector('#navButtons');

navToggle.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
    buttons.classList.toggle('buttons-open');
});


$(document).ready(function() {
    // Loading modal while summarizing listener
    $('#youtubeForm').on('submit', function(e) {
        e.preventDefault();
        $('#modal').css('display', 'flex');

        $.ajax({
            type: 'POST',
            url: '/summary',
            data: $(this).serialize(),
            success: function(response) {
                $('#modal').hide(); 
                window.location.href = "/summary";
            },
            error: function(error) {
                console.log(error);
                $('#modal').hide(); 
            }
        });
    });

    // Download and copy clipboard listeners
    $("#downloadSummary").click(function() {
        $.get("http://127.0.0.1:5000/summary/download_summary", function(data) {
            console.log(data);
        });
    });

    $("#copySummary").click(function() {
        $.get("http://127.0.0.1:5000/summary/copy_summary", function(data) {
            console.log(data);
        });
    });
});


// Check if connection is online or offline
function checkInternet() {
    if (!(navigator.onLine)) {
        if (document.getElementById('modal')) {
            document.getElementById('modal').style.display = 'none';
        }
        document.getElementById('connectionModal').style.display = 'flex';
        return;
    }

    fetch('https://www.google.com/', { 
        mode: 'no-cors' 
    })
    .then(function(response) {
        if (navigator.onLine) {
            document.getElementById('connectionModal').style.display = 'none';
        }
    })
    .catch(function(error) {
        if (!(navigator.onLine)) {
            if (document.getElementById('modal')) {
                document.getElementById('modal').style.display = 'none';
            }
            document.getElementById('connectionModal').style.display = 'flex';
        }
    });
}

// Check internet connection every seconds
setInterval(checkInternet, 100);