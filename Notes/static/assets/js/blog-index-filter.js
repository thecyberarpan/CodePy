// ei blog-indexedDB.html mai jo categorywise post filter ho raha hai ei js file uske liye hai 


$(document).ready(function() {
    $('#categoryFilter').change(function() {
        var selectedCategory = $(this).val();
        if (selectedCategory === 'all') {
            window.location.href = '/blog/';
        } else {
            window.location.href = '/blog/?category=' + encodeURIComponent(selectedCategory);
        }
    });
});




// // Wait for the document (HTML) to be fully loaded
// $(document).ready(function() {
//     // Attach an event listener to the category dropdown with id 'categoryFilter'
//     $('#categoryFilter').change(function() {
//         // Get the selected value from the dropdown
//         var selectedCategory = $(this).val();
        
//         // Check if the selected category is 'all'
//         if (selectedCategory === 'all') {
//             // If 'all', redirect to the '/blog/' page (showing all categories)
//             window.location.href = '/blog/';
//         } else {
//             // If a specific category is selected, include the 'category' parameter in the URL
//             // and redirect to the '/blog/' page with the selected category
//             window.location.href = '/blog/?category=' + encodeURIComponent(selectedCategory);
//         }
//     });
// });
