document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".movie-card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {
            card.style.boxShadow = "0 15px 30px rgba(244,63,94,.35)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.boxShadow = "";
        });

    });

});