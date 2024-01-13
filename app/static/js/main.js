

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
    url.searchParams.delete('page');
    if (breed.checked) {
        url.searchParams.append('breed', breed.value);
    }else {
        all = url.searchParams.getAll('breed');
        all.splice(all.indexOf(breed.value), 1);
        url.searchParams.delete('breed');
        all.forEach(b => {
            url.searchParams.append('breed', b);
        })

    }
    location.href = url.toString()

  });
});