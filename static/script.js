// Movie Recommender System - Frontend Script

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const input = document.querySelector('input[name="movie"]');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            if (input.value.trim() === '') {
                e.preventDefault();
                alert('Please enter a movie name');
            }
        });
    }
});
