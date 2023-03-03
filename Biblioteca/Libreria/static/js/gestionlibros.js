document.querySelector('.delete-button').addEventListener('click', function(event) {
    event.preventDefault();
    const url = event.currentTarget.parentNode.getAttribute('action');
    const nombre = event.currentTarget.getAttribute('data-nombre');
    const id = event.currentTarget.getAttribute('data-id');
    Swal.fire({
        title: `Estas seguro de eliminar el libro ${nombre} con id ${id}?`,
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'No, Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({
                    'id': id
                })
            }).then((response) => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok.');
                }
            }).then((data) => {
                Swal.fire(
                    'Deleted!',
                    'El libro ha sido eliminado.',
                    'success'
                ).then(() => {
                    window.location.reload();
                });
            }).catch((error) => {
                console.error('There has been a problem with your fetch operation:', error);
            });
        }
    });
});