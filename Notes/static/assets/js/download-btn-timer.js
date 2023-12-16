// ei javascript note details page mai jo download timer button hai uske liye. ei notes download krne se peheleek timer chalata hai 

document.getElementById('downloadButton').addEventListener('click', function() {
    // Change button text to "Downloading..."
    document.getElementById('buttonText').innerText = 'Downloading...';

    // Show loading icon
    document.getElementById('loadingIcon').style.display = 'block';

    // Get the dynamic download link from the data-download attribute
    var dynamicDownloadLink = this.getAttribute('data-download');

    // Start a 10-second countdown
    var countdown = 10;
    var countdownInterval = setInterval(function() {
        countdown--;

        if (countdown <= 0) {
            // Navigate to the download link
            window.location.href = dynamicDownloadLink;

            // Hide loading icon
            document.getElementById('loadingIcon').style.display = 'none';

            // Change button text to "Download Now"
            document.getElementById('buttonText').innerText = 'Download Now';

            // Clear the countdown interval
            clearInterval(countdownInterval);
        }
    }, 1000); // 1 second interval
});

