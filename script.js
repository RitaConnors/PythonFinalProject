document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("bookForm");

    form.addEventListener("submit", (e) => {
        const genres = document.getElementById("genres").value.trim();
        const authors = document.getElementById("authors").value.trim();
        const type = document.getElementById("type").value.trim();
        const image = document.getElementById("image").files[0];

        const allowedExtensions = ['jpg', 'jpeg', 'png', 'gif'];
        const fileExtension = image ? image.name.split('.').pop().toLowerCase() : '';

        if (!genres || !authors || !type || !image) {
            alert("All fields are required.");
            e.preventDefault();
            return;
        }

        if (!allowedExtensions.includes(fileExtension)) {
            alert("Only image files (jpg, jpeg, png, gif) are allowed.");
            e.preventDefault();
            return;
        }
    });
});