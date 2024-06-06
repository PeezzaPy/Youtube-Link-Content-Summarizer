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
                setTimeout(() => {
                    console.log("RESPONSE: ", response);
                }, 5000);
                window.location.href = "/summary";
            },
            error: function(error) {
                console.log(error);
                $('#modal').hide(); 
            }
        });
    });

    // Download and copy clipboard listeners
    $("#downloadTranscript").click(function() {
        console.log("dlts")
        $.get("http://127.0.0.1:5000/summary/download_transcript", function(data) {
            console.log(data);
        });
    });

    $("#downloadSummary").click(function() {
        console.log("dlsummary")
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

