document.querySelectorAll(".comment-btn, .view-comments").forEach(btn => {

    btn.onclick = function(e){

        e.preventDefault();

        document
            .getElementById("comments-" + this.dataset.post)
            .classList.add("show");
    };

});

document.querySelectorAll(".close-comments").forEach(btn=>{

    btn.onclick=function(){

        this.closest(".comments-modal")
            .classList.remove("show");

    };

});

document.querySelectorAll(".comments-modal").forEach(modal=>{

    modal.onclick=function(e){

        if(e.target===modal)
            modal.classList.remove("show");

    };

});

document.querySelectorAll(".like-btn").forEach(btn => {

    btn.addEventListener("click", async function(e){

        e.preventDefault();

        const response = await fetch(this.href);
        const data = await response.json();

        const icon = this.querySelector("i");

        icon.className = data.liked
            ? "ri-heart-3-fill liked"
            : "ri-heart-3-line";

        this.closest(".post")
            .querySelector(".likes-count")
            .textContent = `${data.likes} Likes`;

    });

});