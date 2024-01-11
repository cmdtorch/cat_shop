

function increase_counter() {
    document.getElementById("meow_counter").value = parseInt(document.getElementById("meow_counter").value) + 1;
}

function change_sort() {
    let select = document.getElementById("sort_by").value
    let url = new URL(location.href);
    url.searchParams.set('sort', select);
    url.searchParams.delete('page');
    location.href = url.toString()
}



const breeds = document.querySelectorAll(".breed-input");
breeds.forEach(breed => {
  breed.addEventListener('change', () => {
    let url = new URL(location.href);
    if (breed.checked) {
        url.searchParams.append('breed', breed.value);
    }else {
        url.searchParams.delete('breed');
    }
    location.href = url.toString()

  });
});