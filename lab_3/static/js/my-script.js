document.onload = () => {
    form = document.forms.filter_form

    form.onsubmit = (e) => {
        e.preventDefault();
    }
}