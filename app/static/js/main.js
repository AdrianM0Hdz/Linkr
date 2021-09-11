const form = document.querySelector('form#url-form');
const alias = document.querySelector('form#url-form input#alias');

const preventSubmit = (event) => {
    event.preventDefault();
    alert('The Input Must be 20 characters Maximum');
};

form.addEventListener('input', (event) => {
    if (alias.value.length > 20) {
        form.addEventListener('submit', preventSubmit);
    } else {
        form.removeEventListener('submit', preventSubmit);
    }
});