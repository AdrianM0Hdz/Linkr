const form = document.querySelector('form#url-form');
const alias = document.querySelector('form#url-form input#alias');

form.onsubmit = (event) => {
    if (alias.value.lenght > 20) {   
        alert('Alias must be at most 20 characters');
        event.preventDefault();
    }
}