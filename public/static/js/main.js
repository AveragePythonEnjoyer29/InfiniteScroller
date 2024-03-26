document.addEventListener("DOMContentLoaded", async function () {
    async function appendContent() {
        const content_body = document.getElementById("content");

        let response = await fetch("mock.php");
        let content = await response.json();

        content.forEach(item => {
            const userCard = document.createElement("div");
            userCard.id = "cards";

            userCard.classList.add("card");
            userCard.innerHTML = `
                <div class="card--top">
                    <div class="pfp">
                        <img class="pfp--img" src='/static/img/${item.pfp}'/>
                    </div>
                    <h1 class="username">${item.username}</h1>
                </div>
                <div class="card--body">
                    <p class="card--content">${item.content}</p>
                    <h2 class="card--timestamp">Gepost op: ${item.time}</h2>
                </div>
            `;

            content_body.appendChild(userCard);
        });

        let last = document.createElement("span");
        content_body.appendChild(last);

        const observer = new IntersectionObserver(
            entries => {
                entries.forEach(entry => {    
                    if (entry.isIntersecting) {
                        last.remove();
                        appendContent();
                    }
                });
            }
        );
    
        // one does not simply observe
        observer.observe(last);
    }
    
    await appendContent();
});
